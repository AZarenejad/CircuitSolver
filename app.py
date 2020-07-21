from flask import Flask, render_template, url_for, request, jsonify ,  render_template, request , redirect
from circuitSolver import *
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

app = Flask(__name__, template_folder='Templates', static_folder='static',  static_url_path='/static')

flask_debug = False
mycircuit = [circuit()]


@app.route('/', methods = ['GET'])
def page():
    global mycircuit
    return render_template('index.html')


@app.route('/calculate', methods = ['GET'])
def calculate():
    global mycircuit
    results = mycircuit[0].solve_circuit()
    answer = {}
    print("in calc")
    for res in results:
        print(res, " = " , results[res])
        answer[res] = results[res]

    return redirect(request.referrer)


@app.route('/draw', methods = ['GET'])
def draw():
    global mycircuit
    mycircuit[0].drawCircuit()
    return redirect(request.referrer)


@app.route('/state/<string:statement>', methods = ['POST'])
def handle_statement(statement):
    global mycircuit
    inp = statement.split(' ')
    if inp[0] == "IV":
        mycircuit[0].add_element(kind = "Voltage Independent Source", left_pos = inp[1] , right_pos = inp[2], value = int(inp[3]))
    elif inp[0] == "DV":
        type_ = 'V'
        if int(inp[6]) == 1:
            type_ = 'I'
        mycircuit[0].add_element(kind = "Voltage Dependent Source", left_pos = inp[1] , right_pos = inp[2],
                value = int(inp[3]), dleft_pos = inp[4], dright_pos = inp[5], dtype = type_, a = int(inp[7]), b = int(inp[8]))
    elif inp[0] == "IC":
        mycircuit[0].add_element(kind = "Current Independent Source", left_pos = inp[1] , right_pos = inp[2], value = int(inp[3]))
    elif inp[0] == "DC":
        type_ = 'V'
        if int(inp[6]) == 1:
            type_ = 'I'
        mycircuit[0].add_element(kind = "Current Dependent Source", left_pos = inp[1] , right_pos = inp[2],
                value = int(inp[3]), dleft_pos = inp[4], dright_pos = inp[5], dtype = type_, a = int(inp[7]), b = int(inp[8]))
    elif inp[0] == "C":
        mycircuit[0].add_element(kind = "Capacitor", left_pos = inp[1] , right_pos = inp[2], value = int(inp[3]))
    elif inp[0] == "R":
        mycircuit[0].add_element(kind = "Resistor", left_pos = inp[1] , right_pos = inp[2], value = int(inp[3]))
    elif inp[0] == "L":
        mycircuit[0].add_element(kind = "Inductor", left_pos = inp[1] , right_pos = inp[2], value = int(inp[3]))
    elif inp[0] == "W":
        mycircuit[0].add_element(kind = "Wire", left_pos = inp[1] , right_pos = inp[2])

    return 'Success'


@app.route('/reset', methods = ['GET'])
def reset():
    global mycircuit
    del mycircuit[0]
    mycircuit.append(circuit())
    return redirect(request.referrer)


if __name__ == '__main__':
    app.run(port=8826, debug=flask_debug)
