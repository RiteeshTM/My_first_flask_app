from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/form',methods = ["GET","POST"])
def home():
    if request.method == "GET":
        return render_template('get-details.html')
    elif request.method == "POST":
        username = request.form["user_name"]
        return render_template("display-details.html",output_name=username)
    else:
        print("Console error")


if __name__ == '__main__':
    app.run(debug=True)
    
