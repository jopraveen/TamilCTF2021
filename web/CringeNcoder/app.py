from flask import Flask,render_template,request

app = Flask(__name__)

cringe_Dictionary = {
	'a':'cringe','b':'cr1nge','c':'cRinge','d':'crIng3','e':'cRimG3',
	'f':'cR1Ng3e','g':'criNgee','h':'CRINGE','i':'crinGE','j':'ccR1nge',
	'k':'CriNGE','l':'cRINGe','m':'cr1ngE','n':'cringE','o':'CRIng3',
	'p':'Cr1nGe','q':'cR1nnge','r':'cR1Ng3','s':'CrInGe','t':'cRingE',
	'u':'cR1NGE','v':'CRiNg3','w':'CRINGe','x':'CR1NGe','y':'cring3',
	'z':'CRIMNGE','1':'crinG3','2':'cRInge','3':'cRinG3','4':'criNG3',
	'5':'cr1NG3','6':'crinGe','7':'cRiNge','8':'CrInGE','9':'CRinGE',
	'0':'cRInGE'
	}
# f1nally1nn3rp34ce4f73rs0m3cr1ng3eeeeee
# TamilCTF{f1nally1nn3rp34ce4f73rs0m3cr1ng3eeeeee}
# cR1Ng3e crinG3 cringE cringe cRINGe cRINGe cring3 crinG3 cringE cringE cRinG3 cR1Ng3 Cr1nGe cRinG3 criNG3 cRinge cRimG3 criNG3 cR1Ng3e cRiNge cRinG3 cR1Ng3 CrInGe cRInGE cr1ngE cRinG3 cRinge cR1Ng3 crinG3 cringE criNgee cRinG3 cRimG3 cRimG3 cRimG3 cRimG3 cRimG3 cRimG3

def cringeNcoder(text):
	cringe = ''
	for i in text:
		if i != ' ':
			cringe += cringe_Dictionary[i]+ ' '
		else:
			cringe += ' '
	return cringe

@app.route("/")
def home():
  return render_template("index.html",result='None')

@app.route('/encode',methods=['POST','GET'])
def encode():
    text = request.form['text']
    try:
        encoded_text = str(cringeNcoder(text.lower()))
    except:
        return render_template('index.html',result='Only use lowercase letters and numbers')
    return render_template('index.html',result=str(encoded_text))

@app.route('/flag')
def robots():
    return '''
    <h1>Decode the cringes and wrap it inside TamilCTF{}</h1>
    <p>cR1Ng3e crinG3 cringE cringe cRINGe cRINGe cring3 crinG3 cringE cringE cRinG3 Cr1nGe cRimG3 criNG3 cRinge cRimG3 cringe cR1Ng3e cRiNge cRinG3 cR1Ng3 CrInGe cRInGE cr1ngE criNG3 cringE cring3 cRinge cR1Ng3 crinGE cringE criNgee cRinG3 CrInGe</p>
    <style>*{font-family: monospace;}h1{text-align:center;padding-top:50px}html{background:#000;color:white;}p{padding-top:50px;text-align:center;font-size: 30px;}</style>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
