"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
from wtforms import TextField, Form, IntegerField, validators

from app import db
from app.models import Profile

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

class ProfileForm(Form):
    username = TextField('username', [validators.Required()])  
    firstname = TextField('firstname', [validators.Required()])
    lastname = TextField('lastname', [validators.Required()])
    age = IntegerField('age', [validators.Required()])
    sex = TextField('sex', [validators.Required()])
  
@app.route('/profile', methods=('GET', 'POST'))
def add_profile():
    """route for adding profile"""
    form = ProfileForm(csrf_enabled=False)
    if request.method == "POST":
        if form.validate():
            username = request.form['username']
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            age = request.form['age']
            sex = request.form['sex']
            newprofile = Profile(username, firstname, lastname, age, sex)
            db.session.add(newprofile)
            db.session.commit()
        return redirect('/success')
    return render_template('profile.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/profiles')
def list_profiles():
    """route for viewing list of profiles"""
#     import pdb;pdb.set_trace()
    profiles = Profile.query.all()
    return render_template('profiles.html', profiles=profiles)  

@app.route('/profile/<int:id>')
def view_profile(id):
    """route for viewing a profile"""
    profile = Profile.query.get(id)
    return render_template('profile_view.html',profile=profile)
  
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
    app.run(debug=True, host="0.0.0.0", port="8888")