# flask example script with sessions

from flask import Flask, request, session
import numpy as np
from processing import calculate_mode

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "lkmaslkdsldsamdlsdmasldsmkdd"

@app.route("/", methods=["GET", "POST"])
def mode_page():

    if "lat1" not in session:
        session["lat1"] = None
    if "lon1" not in session:
        session["lon1"] = None
        session["lon2"] = None
    if "distance" not in session:
        session["distance"] = None

    errors = ""
    if request.method == "POST":
        try:
            session["lat1"] = float(request.form["lat1"])
            session.modified = True
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["lat1"])
        try:
            session["lon1"] = float(request.form["lon1"])
            session.modified = True
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["lon1"])
        try:
            session["distance"] = float(request.form["distance"])
            session.modified = True
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["distance"])


        if request.form["action"] == "Show coordinates":
            result = session["lat1"], session["lon1"], session["distance"]
            session.modified = True
            second_link = "https://www.google.com/maps/search/?api=1&query=" + str(session["lat1"]) + "," + str(session["lon1"])
            return '''
                <html>
                    <body>
                        <p>{result}</p>
                        <p><a href="https://maps.app.goo.gl/ptqXpfeY6a9baWW19">Click here to open route in Google Maps!</a> Deze laat altijd dezelfde route zien</p>
                        <p><a href={second_link}> Click here to view starting point in Google Maps!</a> Deze werkt echt</p>
                        <p><a href="/">Click here to resubmit coordinates</a>
                    </body>
                </html>
            '''.format(result=result,second_link=second_link)


    return '''
        <html>
            <body>
                {errors}
                <p>Enter your coordinates:</p>
                <form method="post" action=".">
                    <p> Latitude <input name="lat1" /></p>
                    <p> Longitude <input name="lon1" /></p>
                    <p> Distance <input name="distance" /></p>
                    <p><input type="submit" name="action" value="Show coordinates" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)