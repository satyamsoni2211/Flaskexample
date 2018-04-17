from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy as s


#getting data 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\satyam\Documents\intro_to_flask\satyam.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = s(app)

class Comments(db.Model):
	"""docstring for Comments"""
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	comment = db.Column(db.String(1000))
		
@app.route('/') #To run route the function called 
def index():
	result = Comments.query.all()

	return render_template('index.html',result=result)

@app.route('/sign') #To run route the function called 
def sign():
	return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	comment = request.form['comment']
	signature = Comments(name=name,comment=comment)
	db.session.add(signature)
	db.session.commit()

	return redirect(url_for('index'))

links = ['https://www.google.com','https://www.facebook.com','https://www.linkedin.com']
@app.route('/home/',methods=[ 'GET','POST'])
def home():
	return render_template('example.html', links=links ) #jinja replaces things with variables 

# @app.route('/home/<place>',methods=[ 'GET','POST'])
# def home(place):
# 	return render_template('example.html', myvar=place) #jinja replaces things with variables 

if __name__=='__main__':
	app.run(debug=True)
