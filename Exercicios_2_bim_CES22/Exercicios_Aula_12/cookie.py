from flask import Flask, request, make_response

#### Aplicação que conta o número de vezes que o usuário visitou a página
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')

def index():
    contador = int(request.cookies.get('contador_visita',0))
    contador += 1
    msg = 'Voce visitou essa pagina ' + str(contador) + ' vezes'

    resp = make_response(msg)
    resp.set_cookie('contador_visita', str(contador))
    return resp

app.run()