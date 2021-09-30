from flask import Flask, request, render_template, render_template_string, redirect, url_for
import os
import random

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def chall():
	if request.method == "POST":
		name = request.form['user']
		template = '''
<html>
<head><title>Open Flag Challenge</title></head>
<body>
<center>

<h1>Open Flag Challenge</h1>
<br><br>

<h3>CTF is a challenge where flag will be hidden <br>
    somewhere, but this challenge is different from that <br>
    the flag location will be given in this challenge thats <br>
    why its called open flag challenge <br>
    <br><br>

<table border='1' cellpadding='10'>
<tr>
<td>flag location : ./flag.jpg </h3>
</tr>
</table>

</center>
<!-- Hello %s  -->
<!-- ======================================== -->
<!-- I asked the developer to keep the page as much as simple you can -->
<!-- ======================================== -->
<!-- But i didnt expect this, he made very simple -->
<!-- ======================================== -->
</body>
</html>
		''' % name

		return render_template_string(template)


@app.route("/logout")
def logout():
	return redirect(url_for('home'))

if __name__ == "__main__":
	app.run(port=5000)
