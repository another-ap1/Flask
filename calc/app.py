from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# @app.route('/add')
# def Addition():
#     """Takes in a and b, converts to int and adds"""


#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = add(a,b)
#     return str(result)

# @app.route('/sub')
# def Subtraction():
#     """Takes in a and b, converts to int and subtracts b from a"""


#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = sub(a,b)
#     return str(result)

# @app.route('/mult')
# def Multiplication():
#     """Takes in a and b, converts into int and multiplys"""


#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = mult(a,b)
#     return str(result)

# @app.route('/div')
# def Division():
#     """Takes in a and b, converts to int and divides"""


#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = div(a,b)
#     return str(result)



functions = {
    "add" : add,
    "sub" : sub,
    "mult" : mult,
    "div" : div,
    }

@app.route("/math/<function>")
def Math(function):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = functions[function](a,b)
    return str(result)