from flask import Flask,render_template,request
from flask.helpers import make_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

###############################################################################
############################   BUY         ####################################
###############################################################################
@app.route('/buy-1')
def buy1():
    return render_template('buy/buy1.html')

@app.route('/buy-2')
def buy2():
    return render_template('buy/buy2.html')

@app.route('/buy-3')
def buy3():
    return render_template('buy/buy3.html')

@app.route('/buy-4')
def buy4():
    return render_template('buy/buy4.html')

@app.route('/buy-5')
def buy5():
    return render_template('buy/buy5.html')

@app.route('/buy-6')
def buy6():
    return render_template('buy/buy6.html')

@app.route('/buy-7')
def buy7():
    return render_template('buy/buy7.html')

@app.route('/buy-8')
def buy8():
    return render_template('buy/buy8.html')
###############################################################################
###############################################################################
@app.route('/about')
def about():
    return render_template('index.html')


#################### courses
# limnk 
@app.route('/get-course-1',methods=['POST','GET'])
def course1():
    if request.method == 'POST':
        amount = request.form['amount']
        if int(amount) <= 0:
            return render_template('thanks.html',courselink='/static/courses/coursessss1.mp4')
        else:
            return render_template('unsuccessful.html')
    else:
        return render_template('unsuccessful.html')

@app.route('/get-course-2',methods=['POST','GET'])
def course2():
    if request.method == 'POST':
        amount = request.form['amount']
        if int(amount) <= 0:
            return render_template('thanks.html',courselink='/static/courses/2nddcourseeeee.mp4')
        else:
            return render_template('unsuccessful.html')
    else:
        return render_template('unsuccessful.html')

@app.route('/get-course-3',methods=['POST','GET'])
def course3():
    if request.method == 'POST':
        amount = request.form['amount']
        if int(amount) <= 0:
            return render_template('thanks.html',courselink='/static/courses/thirdcourseeee.mp4')
        else:
            return render_template('unsuccessful.html')
    else:
        return render_template('unsuccessful.html')

@app.route('/get-course-4',methods=['POST','GET'])
def course4():
    if request.method == 'POST':
        amount = request.form['amount']
        if int(amount) <= 0:
            return render_template('thanks.html',courselink='/static/courses/4thhhcourseee.mp4')
        else:
            return render_template('unsuccessful.html')
    else:
        return render_template('unsuccessful.html')

@app.route('/get-course-5',methods=['POST','GET'])
def course5():
    if request.method == 'POST':
        amount = request.form['amount']
        if int(amount) <= 0:
            return render_template('thanks.html',courselink='/static/courses/fith555coursee.mp4')
        else:
            return render_template('unsuccessful.html')
    else:
        return render_template('unsuccessful.html')

@app.route('/get-course-6',methods=['POST','GET'])
def course6():
    if request.method == 'POST':
        amount = request.form['amount']
        if int(amount) <= 0:
            return render_template('thanks.html',courselink='/static/courses/sixth6courseeeee.mp4')
        else:
            return render_template('unsuccessful.html')
    else:
        return render_template('unsuccessful.html')

@app.route('/get-course-7',methods=['POST','GET'])
def course7():
    if request.method == 'POST':
        amount = request.form['amount']
        if int(amount) <= 0:
            return render_template('thanks.html',courselink='/static/courses/seven.mp4')
        else:
            return render_template('unsuccessful.html')
    else:
        return render_template('unsuccessful.html')

@app.route('/get-course-8',methods=['POST','GET'])
def course8():
    if request.method == 'POST':
        amount = request.form['amount']
        if int(amount) <= 0:
            return render_template('thanks.html',courselink='/static/courses/it\'s88.mp4')
        else:
            return render_template('unsuccessful.html')
    else:
        return render_template('unsuccessful.html')



#### admin
@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/hackadmin',methods=['POST','GET'])
def hackadmin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']
        if email == 'admin@tamilctf' and password == 'imakepaidcringecourses':
            try:
                special = request.cookies.get('special_person')
                if str(special) == 'true':
                    return render_template('panel.html',flag='TamilCTF{N3v3r_th1nk_p41D_Cr1ng3_c0urs3s_m4k3_U_h4mck3r}')
            except:
                pass
            resp = make_response(render_template('panel.html'))
            resp.set_cookie('special_person','false')
            return resp
        else:
            return render_template('admin.html')
    else:
        return render_template('admin.html')
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002)
