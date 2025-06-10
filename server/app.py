#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


# Index view
@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


# Print string view
@app.route("/print/<parameter>")
def print_string(parameter):
    print(parameter)  # Print to console
    return parameter

# Count view
@app.route("/count/<int:parameter>")
def count(parameter):
    print (parameter)
    return "\n".join(str(i) for i in range(parameter)) +"\n"


# Math view
@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    result = None
    if operation == '+' :
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'Cannot divide by zero'
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'
    
    return str(result)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
