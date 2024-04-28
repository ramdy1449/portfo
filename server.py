from flask import Flask, render_template, url_for, request, redirect
import csv



app = Flask(__name__)

@app.route('/')
def my_home():
#	print(url_for('static', filename='satellite.ico'))
	return render_template('index.html')

# @app.route('/favicon.ico')
# def blog():
# 	return 'welcome to my blog... wanna know more!'

@app.route('/about.html')
def about():
	return render_template('about.html')

@app.route('/<string:package_name>')
def html_page(package_name):
	return render_template(package_name)


def write_to_file(data): 
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file= database.write(f'\n{email},{subject},{message}')

  
def write_to_csv(data): 
	with open('database.csv', mode='a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,)
		csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		return redirect('thankyou.html')
	else:
		return 'something went wrong. Try again!'
