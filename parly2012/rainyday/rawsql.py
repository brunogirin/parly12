from django.db import connection

def execute(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    desc = cursor.description
    return {
        'header': [col[0] for col in desc],
        'data': [[cell for cell in row] for row in cursor.fetchall()]
    }
