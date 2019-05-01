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
	name = str(name)
	main(name)
	wavelengths = [410,490,565,625,730,808]
	img_names = []
	for i in range(0,6):
		wavelength = str(wavelengths[i])
		img_names.append(name+"_"+wavelength)

	print(img_names)
	#Need to send img files from static folder
	path = "/static/"
	img0 = path+img_names[0]
	img1 = path+img_names[1]
	img2 = path+img_names[2]
	img3 = path+img_names[3]
	img4 = path+img_names[4]
	img5 = path+img_names[5]
	# img0 = path+"mnpdouble_410_401.jpg"
	# img1 = path+"mnpdouble_490_401.jpg"
	# img2 = path+"mnpdouble_625_401.jpg"
	# img3 = path+"mnpdouble_730_401.jpg"
	# img4 = path+"mnpdouble_808_401.jpg"
	# img5 = path+"mnpdouble_940_401.jpg"

	return flask.render_template('result.html',**locals())

if __name__ == "__main__":
    app.run(debug=True)
