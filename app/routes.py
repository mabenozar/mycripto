from app import app
from app import query
from app.forms import FormPurchase
from app.query import dbGetAll, dbInsert
from app.api import getApi
from flask import render_template, request, redirect, url_for
import sqlite3
from datetime import datetime, date


@app.route('/')
def movimientos():
    data = dbGetAll()
    
    return render_template("movimientos.html", data=data)




@app.route('/purchase', methods=['GET', 'POST'])
def purchase():
    form = FormPurchase()
    btnDisabled = False

    if request.method == 'POST' and form.validate():
        selectFrom = form.selectFrom.data
        selectTo = form.selectTo.data
        quantityFrom = form.quantityFrom.data
        

        api = getApi(selectFrom, selectTo, quantityFrom)


        if api['status']['error_code'] == 0 and selectFrom != selectTo:
            form.selectFrom.choices = [selectFrom]
            form.selectTo.choices = [selectTo]

            price = float(api['data']['quote'][selectTo]['price'])
            quantityTo = float(quantityFrom)/price
            btnDisabled = True

            return render_template("purchase.html", form=form, quantityTo=quantityTo, price=price, btnDisabled=btnDisabled)
        else:
            if selectFrom == selectTo:
                error = 'Error, the currencies have to be different'
            else:
                error = api['status']['error_message']
            return render_template("purchase.html", form=form, error=error)


        if form.purchase:
            DBFILE = app.config['DBFILE']
            fullDate = datetime.now()

            date = fullDate.date()
            dateFormated = date.strftime('%d/%m/%Y')

            hour = fullDate.time()
            hourFormated = hour.strftime('%H:%M:%S')
                    
            conn = sqlite3.connect(DBFILE)
            c = conn.cursor()
            c.execute('INSERT INTO movements (date, time, from_currency,form_quantity, to_currency, to_quantity) VALUES (?,?,?,?,?,?);',
                (
                    dateFormated, hourFormated, selectFrom, quantityFrom, selectTo,quantityTo
                )
            )
                    
            conn.commit()
            conn.close()
            return redirect(url_for('movimientos'))

    else:
        print('GET')

    return render_template("purchase.html", form=form, btnDisabled=btnDisabled)

