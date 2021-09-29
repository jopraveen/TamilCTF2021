import random
from flask import Flask,render_template,request,make_response


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/solve')
def solve():
    return render_template('login.html')

@app.route('/login', methods=['POST','GET'])
def login():
    try:
        cook3i = request.cookies.get('user')
        if cook3i == 'please_stop_hamcking_my_account_PJ':
            return render_template('flag.html',flag="TamilCTF{f1nalLy_U_r3cov3reD_PJ's_4cCouN7}")
        else:
            return render_template('admin.html')
    except:
        pass
    return render_template('flag.html')

@app.route('/helppj')
def helppj():
    return render_template('challenges.html')

@app.route('/resetpass',methods=['POST','GET'])
def resetpass():
    if request.method == 'POST':
        email = request.form['email']
        lastpass = request.form['lastpass']
        captcha = request.form['captcha']
        if (email == 'pj@tamilctf') and (lastpass == 'tamilctf123') and (captcha == 'cyB3rpj'):
            resp = make_response(render_template('robot.html'))
            resp.headers['OneTimePassword'] = int(otp) 
            return resp
        else:
            return render_template('challenges.html') 
    else:
        return render_template('challenges.html')

@app.route('/otp',methods=['POST','GET'])
def otp():
    if request.method == 'POST':
        OneTimePassword = request.form['OTP']
        if OneTimePassword == str(otp):
            return render_template('pj.html')
        else:
            return render_template('robot.html')
    else:
        return render_template('robot.html')

if __name__ == '__main__':
    otp = random.randint(1000,9999)
    app.run(host='0.0.0.0',port=5004)
