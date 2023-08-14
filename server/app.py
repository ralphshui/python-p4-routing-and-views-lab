#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:str>')
def print_string(str):
    print(f'{str}')
    return f'{str}'

@app.route('/count/<int:num>')
def count(num):
    result = ""  
    for i in range(num):
        result += str(i)+"\n"
    return result
        
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1,operation,num2):
    if operation == '+':
        return str(f'{num1+num2}')
    elif operation == '-':
        return str(f'{num1-num2}')
    elif operation == '*':
        return str(f'{num1*num2}')
    elif operation == 'div':
        return str(f'{num1/num2}')
    elif operation == '%':
        return str(f'{num1%num2}')
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
