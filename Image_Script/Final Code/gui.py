import flask
from main import main

app = flask.Flask(__name__)
app.secret_key = "super secret key"

@app.route("/",methods=['GET','POST'])
def index():
	return flask.render_template('index.html',**locals())

@app.route("/result",methods=['GET','POST'])
def image():
	name = flask.request.form.get('name')
	flask.session['name'] = name
	test = "string"
	main(name)
	return flask.render_template('result.html',**locals())

if __name__ == "__main__":
    app.run(debug=True)
