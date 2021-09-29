from re import DEBUG
from flask import render_template,request
from flask.helpers import make_response
import requests as r
import json
import random
from flask.app import Flask

# TamilCTF{f1nallY_sh3_4cc3p7eD_y0u<3<3<3}
# 54 61 6d 69 6c 43 54 46 7b 66 31 6e 61 6c 6c 59 5f 73 68 33 5f 34 63 63 33 70 37 65 44 5f 79 30 75 3c 33 3c 33 3c 33 7d

# first part = TamilCTF{f1nallY_sh3_
# 54 61 6d 69 6c 43 54 46 7b 66 31 6e 61 6c 6c 59 5f 73 68 33 5f

def flagcutter():
    i = random.randint(0,20)
    flag = ['54', '61', '6d', '69', '6c', '43', '54', '46', '7b', '30', '2e', '30', '5f', '77', '30', '77', '5f', '53', '68', '33', '5f']
    return str(flag[i] +' '+str(i)).split() 

def aibot(msg):
   res = r.get('https://api.simsimi.net/v1/?text={}&lang=en&cf=true'.format(msg))
   res = json.loads(res.text)
   resp = res['messages'][0]['response']  
   return resp

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat-1')
def chat1():
    return render_template('chat1.html')

@app.route('/chat-2')
def chat2():
    return render_template('chat2.html')

@app.route('/sendmsg',methods=['GET','POST'])
def sendmsg():
    if request.method == 'GET':
        try:
            message = request.args.get('message').lower()
            if '../' in str(message):
                return render_template('index.html')
            elif 'i' in message and 'love' in message and 'you' in message:
                respmsg = flagcutter()
                return render_template('chat1.html',yourclass='you',yourmsg=str(message),respclass='she',respmsg=str('I hate you coz '+respmsg[0]),respclr=respmsg[1])
            else:
                try:
                    return render_template('chat1.html',yourclass='you',yourmsg=str(message),respclass='she',respmsg=str(aibot(message)))
                except:
                    return render_template('chat1.html')
        except:
            return render_template('chat1.html')
    else:
        return render_template('index.html')

@app.route('/secondpart',methods=['GET','POST'])
def secondpart():
    if request.method == 'GET':
        msg = request.args.get('message').lower()
        if 'flag' in str(msg):
            # 4cc3p7eD_y0u<3<3<3}
            resp = make_response(render_template('chat2.html',yourclass='you',yourmsg=str(msg),respclass='she',respmsg='_th1s_1s_f4k3'))
            resp.set_cookie("2nd part",value='4cC3P73D_uR_luV_<3}')
            return resp
        else:
            return render_template('chat2.html',yourclass='you',yourmsg=str(msg),respclass='she',respmsg='Bye')
            
    else:
        return render_template('chat2.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
