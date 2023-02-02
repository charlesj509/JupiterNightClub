# app.py

from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
def index():
    #images=['picture1.jpg','picture3.jpg','picture4.jpg','picture5.jpg','picture6.jpg','picture7.jpg']
    return render_template('index.html')

@application.route('/about')
def about():
    return render_template('about.html')

@application.route('/events')
def events():
    return render_template('events.html')

@application.route('/gallery')
def gallery():
    return render_template('gallery.html')

@application.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    application.run(debug=True)
