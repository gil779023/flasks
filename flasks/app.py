from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello World</h1>"

@app.route("/home")
def home_page():
    return """<h2>homepage</h2>
<img width="150px"  src="data:image/jpeg;base64,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" alt="leao">
<a href="/">Ver mais</a><br/>
"""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')