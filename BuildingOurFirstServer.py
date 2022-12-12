import csv
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/likes')
def likes():
    return 'I like watching Maizen, Axzyte, Thinknoodles, Hi5 Gamer'

@app.route('/<page_name>')
def html(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', 'a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', newline='', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def sumbit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong, Try Again Please'

# this is actually Setting Up Flask and Building A Flask Server Flask Templates
