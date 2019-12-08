from datetime import datetime

def createtimestamp():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

