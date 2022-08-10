from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return render_template('indexes.html') 

# @app.route("/go")
# def go_link():
#     return render_template('sux.html') 

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/index.html")
def hello1():
    return render_template('index.html')

@app.route("/resume.html")
def resume():
    return render_template('resume.html')

@app.route("/services.html")
def services():
    return render_template('services.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/portfolio.html")
def portfolio():
    return render_template('portfolio.html')

@app.route("/portfolio-details.html")
def portfolio_details():
    return render_template('portfolio-details.html')

@app.route('/info.html', methods=['GET', 'POST'])
def login_post():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        database = open('database.txt', 'a')
        database.write(f'\n {name} \n {email} \n {subject} \n {message}')
        return render_template('thankyou.html')








   

