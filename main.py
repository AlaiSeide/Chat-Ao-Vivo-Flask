# pip install python-socketio flask-socketio simple-websocket
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

# funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)


@app.route('/')
# uma funcao que vai ser executada quando um usuario entrar nessa rota
def homepage():
    return render_template('homepage.html')



socketio.run(app, host='localhost')