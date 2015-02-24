"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

class MyForm(Form):
    name = StringField('name', validators=[DataRequired()])  
  
@app.route('/profile', methods=('GET', 'POST'))
def profile():
    """route for adding profile"""
    form = MyForm(csrf_enabled=False)
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('profile.html', form=form)

@app.route('/profiles')
def profiles():
    """route for viewing list of profiles"""
    return render_template('profiles.html')  

@app.route('/profile/<userid>')
def thing():
    """route for viewing a profile"""
  
@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
