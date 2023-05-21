from flask import Flask, request, render_template, redirect, session


app = Flask(__name__)


@app.route('/')
def load():
    try:
        return render_template('home.html')
    except:
        return render_template('error.html')


@app.route('/home')
def home():
    try:
        return render_template('home.html', title="home")
    except:
        return render_template('error.html')

@app.route('/about')
def about():
    try:
        return render_template('about.html', title = "about")
    except:
        return render_template('error.html')
    
# @app.route('/socials')
# def socialMedia():
#     try:
#         return render_template('socialMedia.html', title = "socials")
#     except:
#         return render_template('error.html')
    

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()