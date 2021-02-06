from app import app
from datetime import datetime, date
import sqlite3

def dbGetAll():
    DBFILE = app.config['DBFILE']
    
    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()
    c.execute('SELECT date, time, from_currency, form_quantity, to_currency, to_quantity FROM movements;')
    
    data = c.fetchall()
    conn.close()

    return data


def dbInsert(selectFrom, quantityFrom, selectTo, quantityTo):
    DBFILE = app.config['DBFILE']
    fullDate = datetime.now()

    date = fullDate.date()
    dateFormated = date.strftime('%d/%m/%Y')

    hour = fullDate.time()
    hourFormated = hour.strftime('%H:%M:%S')
    
    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()
    c.execute('INSERT INTO movements (date, time, from_currency, form_quantity, to_currency, to_quantity) VALUES (?,?,?,?,?,?);',
        (
            dateFormated, hourFormated, selectFrom, quantityFrom, selectTo, quantityTo
        ))
    
    conn.commit()
    data = c.fetchall()
    conn.close()

    return data
