
from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pincode.html')

@app.route('/results', methods=['POST'])
def results():
    pincode = request.form['pincode']
    response = requests.get(f'https://api.postalpincode.in/pincode/{pincode}')
    data = response.json()

    if data[0]['Status'] == 'Success':
        post_office = data[0]['PostOffice'][0]['Name']
    else:
        post_office = 'Invalid Pincode'

    return render_template('results.html', pincode=pincode, post_office=post_office)

if __name__ == '__main__':
    app.run(debug=True)
