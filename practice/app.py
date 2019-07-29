import json
from flask import (Flask, render_template, redirect,
                    make_response,request, url_for,flash )

# from options import DEFAULTS


app = Flask(__name__)
app.secret_key = 'esauhou>UO>au.sh35@<Uouo52%@#ouo.42!@#42'


def get_save_data():
    try:
        data = json.loads(request.cookies.get(''))
    except TypeError:
        data = {}
    return data

@app.route('/')
def index():
    data = get_save_data()
    return render_template("index.html", saves=data)

@app.route('/builder')
def builder():
    return render_template(
        'builder.html',
        saves=get_save_data(),
        # options=DEFAULTS
    )


@app.route('/save', methods=['POST'])
def save():
    flash("Alright! That looks awesome!")
    response = make_response(redirect(url_for('builder')))
    data = get_save_data()
    data.update(dict(request.form.items()))
    response.set_cookie('charactor', json.dumps(data))
    return response


app.run(debug=True, port=8000, host='0.0.0.0')