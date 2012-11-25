from django.http import HttpResponse
from django.shortcuts import render
import simplejson

from rainyday.models import VoteRecord, InstallStatus
from rainyday.install import DbInstaller
import rainyday.rawsql
from rainyday.charts import LineChart

def index(request):
    vote_record_count = VoteRecord.objects.count()
    if vote_record_count > 0:
        return chart_rain(request)
    else:
        context = {'vote_record_count': vote_record_count}
        return render(request, 'rainyday/index.html', context)

def install(request):
    install_type = request.POST['install_type']
    if install_type == "sample":
        fname = "./rainyday-sample.csv"
    elif install_type == "full":
        fname = "./rainyday-full.csv"
    else:
        return render(request, 'polls/index.html', {
            'error_message': "You didn't select an installation type.",
        })
    status = InstallStatus(pk=1, install_type = install_type, done = False, count = 0)
    status.save()
    context = {'install_type': install_type, 'loaded_count': 0}
    return render(request, 'rainyday/install.html', context)

def install_start(request):
    try:
        status = InstallStatus.objects.get(pk=1)
        installer = DbInstaller(status.install_type)
        installer.install(request)
        return HttpResponse('done', mimetype='text/plain')
    except (KeyError, InstallStatus.DoesNotExist):
        return HttpResponse('failed', mimetype='text/plain')
    
def install_status(request):
    try:
        status = InstallStatus.objects.get(pk=1)
        done = status.done
        count = status.count
    except (KeyError, InstallStatus.DoesNotExist):
        done = False
        count = 0
    context = {'done': done, 'loaded_count': count}
    return HttpResponse(simplejson.dumps(context), mimetype='application/javascript')
    
def chart_rain(request):
    data = rainyday.rawsql.execute('''
        SELECT rainfall, avg(count) as avg FROM (
            SELECT rainfall, date, count(*) as count
            FROM rainyday_voterecord
            GROUP BY rainfall, date
        ) GROUP BY rainfall
    ''')
    chart = LineChart(600, 400, "", "Rainfall (mm)", "Number of Votes", [data['data']])
    return render(request, 'rainyday/chart.html', {
        'data': data,
        'chart': chart,
        'width': 600,
        'height': 400,
        'title': "Are MPs waterproof?",
        'narrative': "They seem to be! No correllation between rainfall and number of votes.",
        'next_page': 'chart_dow'
    })
    
def chart_dow(request):
    data = rainyday.rawsql.execute('''
        SELECT day, avg(count) as avg FROM (
            SELECT strftime('%%w', date) as day, count(*) as count
            FROM rainyday_voterecord
            GROUP BY date
        ) GROUP BY day
    ''')
    series = []
    for d in data['data']:
        dow = (int(d[0]) + 6) % 7
        data = int(d[1])
        dpoint = (dow, data)
        series.append(dpoint)
    rseries = series[1:]
    rseries.append(series[0])
    chart = LineChart(600, 400, "", "Monday to Sunday", "Number of Votes", [rseries], ["M", "T", "W", "T", "F", "S", "S"])
    return render(request, 'rainyday/chart.html', {
        'data': data,
        'chart': chart,
        'width': 600,
        'height': 400,
        'title': "Do MPs work week-ends?",
        'narrative': "Yes they do! But the peak is still at the beginning of the week."
    })

