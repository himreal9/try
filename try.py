import json
from flask import Flask,render_template,request,redirect,session

app=Flask(__name__)
app.secret_key='man'


@app.route('/',methods=['POST','GET']) 
def con():
    if request.method=='POST':
        if request.form.get("se"):
           o = request.form['ser']
           a = request.form['ag']
           n = request.form['no']
           with open('new.json',"r") as f:
                k=json.load(f)
                
           with open('new.json',"w") as f:
                k[o]={'age':a,'no':n}
                d=json.dumps(k)
                f.write(d)
                
           with open('new.json',"r") as f:
                k=json.load(f)
                k=str(k)
                session['k']=k
           return redirect('/')
    else:        
        return render_template("temp.html")

if __name__=='__main__':
    app.run()
