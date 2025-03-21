from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Bienvenido'

@app.route('/wellcome')
@app.route('/wellcome/<string:name>')
@app.route('/wellcome/<int:ncontrol>')
@app.route('/wellcome/<string:name>/<int:ncontrol>')
def bienvenido(name=None, ncontrol=None):
    if name is None and ncontrol is None:
        return 'Bienvenido'
    if name is not None and ncontrol is None:
        return f'Bienvenido {name}'
    if name is None and ncontrol is not None:
        return f'El número recibido es: {ncontrol}'
    else:
        return f'Bienvenido {name}, tu número de control es: {ncontrol}'

if __name__ == '__main__':
    app.run(debug=True)