from flask import Flask, redirect, url_for, render_template, request, make_response, Response, abort
import requests

app = Flask(__name__)

@app.route("/")
def home():
	resp = make_response(render_template("home.html"))
	resp.set_cookie('site_access', "yes")
	return resp

@app.route("/account")
def account():
	return render_template("login.html")

@app.route("/account/login" , methods=["GET", "POST"])
def login():
	if request.method == "POST":
		return render_template("login.html", info="Invalid username or password")
	if request.method == "GET":
		return  '''
                <title>403 Forbidden</title>
                <h1>Forbidden</h1>
                <p>You don't have the permission to access the requested resource.</p>
                '''

@app.route("/account/register")
def register():
	if request.cookies.get("site_access") == "yes":
		return render_template("register.html", info="Register with same credentials in home page")
	else:
		return '''
		<title>403 Forbidden</title>
		<h1>Forbidden</h1>
		<p>You don't have the permission to access the requested resource. Only one time is access is given to the users</p>
		'''

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
	if request.method == "POST":
		user = request.form['email']
		pas  = request.form['password']
		if user == "admin@tamilctf.com" and pas == "secret_password":
			return render_template("dashboard.html")
		else:
			return redirect('/account/register')

@app.route("/flagishere")
def del_cookie():
	resp = make_response(render_template("login2.html", info="That is the tricky button, admin has set the Automated script to reset password if we click that button, now you are kicked out ! sad laip"))
	resp.set_cookie('site_access', '', expires=0)
	return resp

@app.route("/passwordreset")
def reset_pass():
	return render_template("resetpass.html", info="Enter the mail to reset password")

@app.route("/passrecovery", methods=["GET", "POST"])
def recover():
	if request.method == "POST":
		if request.form['email'] == 'admin@tamilctf.com':
			host = request.headers['Host']
			resetlink = 'http://'+host+'/resetpassword?token=73c642bwe7gf87n9jgd'
			requests.get(resetlink)
			return render_template("resetpass.html", info="password reset link is sent to your mail")

		else:
			return render_template("resetpass.html", info="Are you trying someother email ?")

@app.route("/resetpassword")
def pass_reset():
	token = request.args.get("token")
	if token == '73c642bwe7gf87n9jgd':
		return render_template('passreset.html')


@app.route("/thisisthefinalpath")
def final():
	resp = Response(render_template("final.html"))
	resp.headers['flag'] = "TamilCTF{1_L0vE_H3ader5}"
	return resp

#main
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5005)
