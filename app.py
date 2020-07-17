from flask import Flask, render_template, url_for, request, jsonify
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

app = Flask(__name__, template_folder='Templates', static_folder='static',  static_url_path='/static')

flask_debug = False

# global_circuit = [Circuit()]

@app.route('/sim', methods = ['GET'])
def page():
    # global global_circuit
    # del global_circuit[0]
    # global_circuit.append(Circuit())
    return render_template('index.html')


@app.route('/calculate', methods = ['POST'])
def calculate():
    pass
    # global global_circuit
    # calculated = global_circuit[0].calc()
    # result = getAnswers(global_circuit[0])
    # answer = {}
    # answer['Nodes Voltage'] = result[0]
    # answer['Circuit Independent Voltage Sources'] = result[1]
    # answer['Circuit OpAmps'] = result[2]
    # answer['Circuit Resistors'] = result[3]
    # answer['Circuit Capacitors'] = result[4]
    # answer['Circuit Inductors'] = result[5]
    # from MNA.ShowResults import printResults
    # printResults(global_circuit[0])
    # return jsonify(answer)

@app.route('/addelement/<name>', methods = ['POST'])
def addelement(name):
    pass
    # global global_circuit
    # data = request.get_json()
    # logging.debug(f'data: {data}')
    # add_element_to_circuit(circuit_list=global_circuit, **data)
    # printAddedElements(global_circuit[0])
    # return 'Success'


@app.route('/state/<string:statement>', methods = ['POST'])
def handle_statement(statement):
    pass
    # print(f'statement before change: {statement}')
    # statement = statement.replace('#', ' ')
    # print(f'statement: {statement}')
    # ans = UIans(circuit=global_circuit, statement=statement)
    # if ans is not None:
    #     ans.replace('\n', '<br />')
    #     return ans



@app.route('/reset', methods = ['POST'])
def reset():
    pass
    # global global_circuit
    # del global_circuit[0]
    # global_circuit.append(Circuit())
    # return jsonify(len(global_circuit) == 1 and type(global_circuit[0]) == Circuit)


if __name__ == '__main__':
    app.run(port=6666, debug=flask_debug)
