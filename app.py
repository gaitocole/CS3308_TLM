from flask import Flask, request, make_response, render_template, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def landingPage():
    if request.method == 'POST':
        if #logic for login
            #code
            return redirect(url_for('taskPage'))
        elif #logic for new user
            #code
            return redirect(url_for('newUserPage'))
    else:
        return render_template('LandingPage.html')

@app.route('/new', methods=['GET','POST'])
def newUserPage():
    if request.method == 'POST':
        #code for user creation
        return redirect(url_for('taskPage'))
    else:
        return render_template('NewUser.html')

@app.route('/tasks')
def taskPage():
    return render_template('taskPage.html')
    
@app.route('/newTask', methods=['GET','POST'])
def newTask():
    if request.method == 'POST':
        testForm = request.form['time'] + request.form['freq'] + request.form['dayWk'] + request.form['msgTxt'] 
        app.logger.info('%s', testForm)
        return redirect(url_for('taskPage'))
    else:
        return render_template('newTask.html')

#@app.route('/tasks/<user>')
#def taskPage(user):
#   return render_template('taskPage.html')
#   return f'User {escape(username)}'

if __name__ == "__main__":
    app.run(debug = True)