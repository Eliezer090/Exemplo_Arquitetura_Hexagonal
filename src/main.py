from flask import Flask
from src.configuration import configure_inject
from src.web.pedido.pedido import pedidos

app = Flask(__name__)
configure_inject(app)
app.register_blueprint(pedidos(), url_prefix='/api')
