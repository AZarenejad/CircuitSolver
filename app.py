from flask import Flask, render_template, url_for, request, jsonify
from circuitSolver import *
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

app = Flask(__name__, template_folder='Templates', static_folder='static',  static_url_path='/static')

verbose = False
flask_debug = False
mycircuit = [circuit()]


@app.route('/', methods = ['GET'])
def page():
    global mycircuit
    # del mycircuit[0]
    # mycircuit.append(circuit())

    return render_template('index.html')


@app.route('/calculate', methods = ['GET'])
def calculate():
    global mycircuit
    results = mycircuit[0].solve_circuit()
    answer = {}
    print(">>>>>>>>>> ", type(results))
    for res in results:
        print(res, " = " , results[res])
        answer[res] = results[res]

#    return jsonify(answer)
    return results
    # return redirect(url_for('calculate'))

@app.route('/draw', methods = ['GET'])
def draw():
    global mycircuit
    mycircuit[0].drawCircuit()
#    redirect(url_for('/'))
#    redirect('/')
    # return redirect(url_for('draw'))

@app.route('/state/<string:statement>', methods = ['POST'])
def handle_statement(statement):
    global mycircuit
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.")
    inp = statement.split(' ')
    val = int(inp[3])
    if inp[0] == "IV":
        mycircuit[0].add_element(kind = "Voltage Independent Source", left_pos = inp[1] , right_pos = inp[2], value = val)
    elif inp[0] == "DV":
        mycircuit[0].add_element(kind = "Voltage Dependent Source", left_pos = inp[1] , right_pos = inp[2], value = val)
    elif inp[0] == "IC":
        mycircuit[0].add_element(kind = "Current Independent Source", left_pos = inp[1] , right_pos = inp[2], value = val)
    elif inp[0] == "DC":
        mycircuit[0].add_element(kind = "Current Dependent Source", left_pos = inp[1] , right_pos = inp[2], value = val)
    elif inp[0] == "C":
        mycircuit[0].add_element(kind = "Capacitor", left_pos = inp[1] , right_pos = inp[2], value = val)
    elif inp[0] == "R":
        mycircuit[0].add_element(kind = "Resistor", left_pos = inp[1] , right_pos = inp[2], value = val)
    elif inp[0] == "L":
        mycircuit[0].add_element(kind = "Inductor", left_pos = inp[1] , right_pos = inp[2], value = val)
    elif inp[0] == "W":
        mycircuit[0].add_element(kind = "Wire", left_pos = inp[1] , right_pos = inp[2])

    return 'Success'



@app.route('/reset', methods = ['GET'])
def reset():
    pass
    # global global_circuit
    # del global_circuit[0]
    # global_circuit.append(Circuit())
    # return jsonify(len(global_circuit) == 1 and type(global_circuit[0]) == Circuit)


if __name__ == '__main__':
    app.run(port=9956, debug=flask_debug)
