import csv
import dateutil.parser

from rainyday.models import Vote, Constituency, Party, Division, Person, VoteRecord, InstallStatus

class DbInstaller:
    def __init__(self, install_type):
        self.fname = "./rainyday-{0}.csv".format(install_type)
    
    def install(self, request):
        try:
            status = InstallStatus.objects.get(pk=1)
        except (KeyError, InstallStatus.DoesNotExist):
            status = InstallStatus(pk=1, install_type = self.install_type, done = False, count = 0)
            status.save()
        with open(self.fname, 'r') as csvfile:
            freader = csv.reader(csvfile)
            first = True
            for row in freader:
                if first:
                    first = False
                else:
                    # vote
                    try:
                        vote_pk = int(row[2])
                        vote = Vote.objects.get(pk=vote_pk)
                    except (KeyError, Vote.DoesNotExist):
                        vote = Vote(pk=vote_pk, text=row[3])
                        vote.save()
                    # constituency
                    try:
                        constituency_pk = int(row[29])
                        constituency = Constituency.objects.get(pk=constituency_pk)
                    except (KeyError, Constituency.DoesNotExist):
                        constituency = Constituency(pk=constituency_pk, name=row[30])
                        constituency.save()
                    # party
                    try:
                        party_pk = int(row[26])
                        party = Party.objects.get(pk=party_pk)
                    except (KeyError, Party.DoesNotExist):
                        party = Party(pk=party_pk, name=row[27])
                        party.save()
                    # division
                    try:
                        division_pk = int(row[7])
                        division = Division.objects.get(pk=division_pk)
                    except (KeyError, Division.DoesNotExist):
                        division = Division(pk=division_pk, div_no=int(row[8]), date=self.parse_date(row[9]), title=row[12])
                        division.save()
                    # person
                    try:
                        person_pk = int(row[1])
                        person = Person.objects.get(pk=person_pk)
                    except (KeyError, Person.DoesNotExist):
                        person = Person(pk=person_pk, name = row[24], party=party, constituency=constituency,
                            area_name = row[32], gender = row[22], date_of_birth = self.parse_date(row[20]), age = float(row[0]))
                        person.save()
                    # vote record
                    vote_record = VoteRecord(person = person, vote = vote, division = division,
                        date = self.parse_date(row[10]), rainfall = float(row[11]), deferred_vote = row[17])
                    vote_record.save()
                    status.count = status.count + 1
                    status.save()
        status.done = True
        status.save()
                    
    def parse_date(self, date):
        return dateutil.parser.parse(date)
