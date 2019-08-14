import os
import requests
import traceback

from flask import Flask
from flask import render_template
from flask import request

from Distance import distance

from wtforms import Form, DecimalField, validators

from math import pi

class RegistrationForm(Form):
    Latitude1 = DecimalField('Latitude 1', [validators.NumberRange(min=-90, max=90, message="Please enter a number")])
    Longitude1 = DecimalField('Longitude 1', [validators.NumberRange(min=-180, max=180, message="Please enter a number")])
    Latitude2 = DecimalField('Latitude 2', [validators.NumberRange(min=-90, max=90, message="Please enter a number")])
    Longitude2 = DecimalField('Longitude 2', [validators.NumberRange(min=-180, max=180, message="Please enter a number")])

app = Flask(__name__)

@app.route("/")

def home():
    return render_template('home.html')

@app.route('/ByCoordinate/', methods = ['POST', 'GET'])

def ByCoordinate():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            lat1 = float(form.Latitude1.data) * float(pi) / float(180)
            lon1 = float(form.Longitude1.data) * float(pi) / float(180)
            lat2 = float(form.Latitude2.data) * float(pi) / float(180)
            lon2 = float(form.Longitude2.data) * float(pi) / float(180)

            dis = str(round(distance(lat1, lon1, lat2, lon2),2))

            appID = "QV50Cg9nKusKIxU0xuxn"
            appCode = "MtWxs2XaYo4z_X8jc1n_9Q"

            imageurl = "https://image.maps.api.here.com/mia/1.6/route?r0=" + str(form.Latitude1.data) + "%2C" + str(form.Longitude1.data) + "%2C" + str(form.Latitude2.data) + "%2C" + str(form.Longitude2.data) + "&m0=" + str(form.Latitude1.data) + "%2C" + str(form.Longitude1.data) + "%2C" + str(form.Latitude2.data) + "%2C" + str(form.Longitude2.data) + "&lc0=dc85ff&sc0=000000&lw0=6&w=500&app_id=" + appID + "&app_code=" + appCode
            return render_template('ByCoordinate.html', form=form, dis = dis, url = imageurl)
        except:
            traceback.print_exc()
            return render_template('ByCoordinate.html', form=form, dis = "Error - please try again")
    else:
        return render_template('ByCoordinate.html', form=form, dis = "")

# port = int(os.environ.get('PORT', 5000))
# app.run(port = port)

