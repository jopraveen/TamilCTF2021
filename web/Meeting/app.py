from flask import Flask,render_template,request
from flask.helpers import make_response
import string,random,base64
import requests


app = Flask(__name__)

# adminbot
def admin_bot(recv_msg):
    try:
        url = recv_msg
        fkn_Admin_cookiesssss = {"justAsmallCo0ki33ForT3sTinG":"yehYouC4nG0In","user":"7his1s7h3C0oki3oFT4m1lCtfAdmin"}
        response = requests.get(url,cookies=fkn_Admin_cookiesssss)
    except:
        pass

@app.route('/',methods=['POST','GET'])
def home():
    char = string.ascii_lowercase + string.digits
    meet_code = ''.join(random.sample(char*3,3)) + '-' + ''.join(random.sample(char*4,4)) + '-' + ''.join(random.sample(char*3,3))
    enc_meet_code = 'The encoded meet code is\n\n' + base64.b64encode(meet_code.encode('ascii')).decode('utf-8')
    global post_meet_code
    post_meet_code = meet_code
    print(meet_code)
    if request.method == 'POST':
        return str(enc_meet_code)
    else:
        return render_template('index.html')
    
@app.route('/join-meet',methods=['POST','GET'])
def join_meet():
    mc = request.form['meet-code']
    if str(mc) == str(post_meet_code):
        resp = make_response(render_template('load.html'))
        resp.set_cookie('justAsmallCo0ki33ForT3sTinG','yehYouC4nG0In')
        return resp
    else:
        return render_template('index.html')

@app.route('/letmein')
def real_meet():
    if "post_meet_code" in locals():
                        pass
    else:
        post_meet_code = '1337_m337_c0d3'
    try:
        cuk = request.cookies.get('justAsmallCo0ki33ForT3sTinG')
        if str(cuk) == 'yehYouC4nG0In':
            try:
                usr = request.cookies.get('user')
                if str(usr) == 'Jopraveen':
                    return render_template('meeting.html',code=str(post_meet_code),who1='(You)',usr_logo='https://github.com/jopraveen/jopraveen.github.io/raw/main/img/fav-icon.png')
                elif str(usr) == 'CyberPJ':
                    return render_template('meeting.html',code=str(post_meet_code),who2='(You)',usr_logo='https://pbs.twimg.com/media/En7E4lkXcAAaV86.jpg')
                elif str(usr) == 'SIN_GREED':
                    return render_template('meeting.html',code=str(post_meet_code),who3='(You)',usr_logo='/static/sin.jpg')
                elif str(usr) == '0xAnnLynn':
                    return render_template('meeting.html',code=str(post_meet_code),who4='(You)',usr_logo='/static/ajay.jpg')
                elif str(usr) == '0xsakthi':
                    return render_template('meeting.html',code=str(post_meet_code),who6='(You)',usr_logo='https://1.bp.blogspot.com/-0qkwtPdA3-w/YEpFDj9a_6I/AAAAAAAAACU/g7K80xs2qvI3lqwe2a7LM-umBQTLolhmQCK4BGAYYCw/s84-pf/images%2B%252823%2529_1609246155887.jpeg')
                elif str(usr) == '7his1s7h3C0oki3oFT4m1lCtfAdmin':
                    return render_template('xss.html',code=str(post_meet_code),who0='(You)',sendmsg='[No messages]',video='/static/present.mp4',answer='Magic word: g1mM3_7h3_FLAG_1_h4ck3eD_T4m1l_C7F_m337',usr_logo='/static/exploiteverything.png')
                elif str(usr) == 'Gokul': 
                    return render_template('xss.html',code=str(post_meet_code),who5='(You)',sendmsg='[No messages]',video='/static/present.mp4',answer=' Exploit Everything is presenting to everyone...',usr_logo='/static/gokul.png') 
                else:
                    resp = make_response(render_template('meeting.html',code=str(post_meet_code),who1='(You)'))
                    resp.set_cookie('user','Jopraveen')
                    return resp
            except:
                pass
        else:
            return render_template('index.html')
    except:
        pass
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/sendmsg',methods=['POST','GET'])
def sendmsg():
    if request.method == 'GET':
        recv_msg = request.args.get('message')
        admin_bot(recv_msg)
        try:
            cuk = request.cookies.get('justAsmallCo0ki33ForT3sTinG')
            usr = request.cookies.get('user')
            if "post_meet_code" in locals():
                pass
            else:
                post_meet_code = '1337_m337_c0d3'

            if str(cuk) == 'yehYouC4nG0In':
                if str(usr) == '7his1s7h3C0oki3oFT4m1lCtfAdmin':
                    return render_template('xss.html',code=str(post_meet_code),who0='(You)',sendmsg='Gokul: {}'.format(recv_msg),video='/static/present.mp4',answer=' Magic word: g1mM3_7h3_FLAG_1_h4ck3eD_T4m1l_C7F_m337',usr_logo='/static/exploiteverything.png')

                elif str(usr) == 'Gokul':
                    return render_template('xss.html',code=str(post_meet_code),who5='(You)',sendmsg='Gokul: {}'.format(recv_msg),video='/static/present.mp4',answer=' Exploit Everything is presenting to everyone...',usr_logo='/static/gokul.png')
                
                else:
                    return render_template('index.html')
        except:
            pass
    else:
            
            return render_template('index.html')
    return render_template('index.html')

@app.route('/validate',methods=['GET','POST'])
def validate():
    if request.method == 'GET':
        word = request.args.get('word').replace(' ','')
        if str(word) == 'g1mM3_7h3_FLAG_1_h4ck3eD_T4m1l_C7F_m337':
            return render_template('form.html',flag='Flag: TamilCTF{f1n4llY_y0u_h4ck3D_Tam1lCTF_m337_1337}')
        else:
            return render_template('form.html',flag='Thankyou for your response <3')    
    else:
        return render_template('form.html')

# g1mM3_7h3_FLAG_1_h4ck3eD_T4m1l_C7F_m337
# TamilCTF{w3lCom3_70_T4m1L_CTF_meeeeeT_<3}

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5003)
