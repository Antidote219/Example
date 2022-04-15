from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "azrfhaerhgtshsdg"
import random
@app.route("/")
def index():
    if "count" not in session:
        session["count"] = 0
        
    else:
        session ['count'] += 1
        
    return render_template('index.html', count = session["count"])


@app.route("/reset")
def reset_session():
    session.clear()
    return redirect("/")
if __name__=="__main__":
    app.run(debug=True)