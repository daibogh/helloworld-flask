#!/usr/bin/env python
 # -*- coding: utf-8 -*-
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/about')
def hello_world():
  return render_template('hello.html')
@app.route('/')
def get_count():
  with open('counter.txt', 'r') as f:
    t=f.read()
    return f'{t}'
@app.route('/stat')
def inc_count():
  t = 0
  with open('counter.txt', 'r') as f:
    t=int(f.read())
  with open('counter.txt', 'w') as f:
    f.write(str(int(t)+1))
  
  return f'{t}'

 
if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')
