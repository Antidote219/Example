from flask import Flask, render_template, redirect, request, session



app = Flask(__name__)
app.secret_key = "EFeragaegF"
## route to display users

@app.route('/')
def user():
    return render_template('index.html')
    

@app.route('/process', methods=["POST"])
def process():
    
    print(request.form)
    
    
    session["user"] = request.form
    
    return redirect('/result')

@app.route('/result')
def result():
    print(request.form)
    return render_template ('display.html', user_info = session['user'])
    


if __name__ == "__main__":
    app.run(debug=True)