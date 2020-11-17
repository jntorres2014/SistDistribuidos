from flask import (
    Flask, 
    render_template, 
    make_response, 
    jsonify, 
    request,
) 

app = Flask(__name__)

PORT = 5000
HOST = '0.0.0.0'

json = {
    "languajes": {
        "es": "Spanish",
        "en": "English",
        "fr": "French",
    },
    "colors": {
        "r": "Red",
        "g": "Green",
        "b": "Blue",
   }
}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('session.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
#----------------------------------------------#

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/template")
def hola():
    return render_template("login.html")

@app.route("/json")
def get_json():
    print("LOGIN || get_json || init ")
    data = {"user": "pedro"}
    return make_response(jsonify(data), 200)

@app.route("/users/<user>")
def get_user(user):    
    data = {"user": user}
    return make_response(jsonify(data), 200)

@app.route("/users", methods=["POST"])
def post_user():    
    print(" === LOGIN || post_user ")        
    for i in dir(request):
        print(i)
    print(request.get_data())
    req = request.get_json()
    return make_response(jsonify(req), 200)   

if __name__ == '__main__':
    print(f"Login microservice runnning in port {PORT}")
    app.run(host=HOST, port=PORT)
