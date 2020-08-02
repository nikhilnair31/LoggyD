import auto_joiner
import json
from flask import Flask, render_template, request

app = Flask(__name__)
with open('config.json', 'r') as f:
   config = json.load(f)
#app.config.from_object("multiscript_config")

def result2output(result):
   return render_template("output.html",result = result)

@app.route('/')
def student():
   return render_template('input.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      config['email'] = request.form['ID'] 
      config['password'] = request.form['Password']
      config['delay'] = request.form['RefreshRate']

      with open('config.json', 'w') as f:
         json.dump(config, f)
      auto_joiner.main()
      return render_template('success.html')

if __name__ == '__main__':
   app.run(debug = False)
   #app.run(host="0.0.0.0")