from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<h1>Hello World</h1>\
        
    <a href="/home">Ver mais</a><br/>"""

@app.route("/home")
def home_page():
    return """<h2>homepage</h2>
<img width="150px"  src="https://th.bing.com/th/id/OIP.Xj_XB9KGp8Oon6kxGo69OgHaE-?pid=ImgDet&rs=1"/>
<a href="/">Ver mais</a><br/>
"""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')