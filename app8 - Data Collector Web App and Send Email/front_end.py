from flask import Flask, render_template, request
import json

try:
    with open("data.json", "r") as read_file:
        data = json.load(read_file)
        print(data)
        print(type(data))
except:
    data = {}
    data['email'] = []
    data['height'] = []

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        data['email'].append( request.form["email_name"] )
        data['height'].append( request.form["height_name"] )
        with open("data.json", "w") as write_file:
            json.dump(data, write_file)
        return render_template("success.html")

@app.route("/sent")
def sent():
    import send_email
    render_template("sent.html")
    send_email.send_json(data)
    return render_template("sent.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
