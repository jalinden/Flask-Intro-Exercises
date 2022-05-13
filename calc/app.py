from flask import Flask,request
import operations

app = Flask(__name__)

@app.route('/add')
def add_nums():
    num_a = int(request.args.get("a"))
    num_b = int(request.args.get("b"))
    total= str(operations.add(num_a,num_b))
    return total
@app.route('/mult')
def add_nums():
    num_a = int(request.args.get("a"))
    num_b = int(request.args.get("b"))
    total= str(operations.mult(num_a,num_b))
    return total
@app.route('/divide')
def add_nums():
    num_a = int(request.args.get("a"))
    num_b = int(request.args.get("b"))
    total= str(operations.div(num_a,num_b))
    return total
@app.route('/sub')
def add_nums():
    num_a = int(request.args.get("a"))
    num_b = int(request.args.get("b"))
    total= str(operations.sub(num_a,num_b))
    return total