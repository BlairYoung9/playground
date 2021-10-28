from flask import Flask  

app = Flask(__name__)    

@app.route('/')         
def hello_world():
    return 'Hello World!' 

@app.route('/dojo')         
def dojo():
    return 'Dojo!' 

@app.route('/say/<name>')         
def say(name):
    return "Hello, " + name

@app.route('/repeat/<int:count>/<name>')         
def repeat(count,name):
    return f"Hello {name * count}"

if __name__=="__main__":   
    app.run(debug=True)    