

import pytest
import inject

from flask import Flask
from flask.testing import FlaskClient
from unittest.mock import Mock
from pytest_mock import MockFixture

from src.domain.actions.pedido.get_pedidos import GetPedido
from src.domain.actions.pedido.post_pedido import PostPedido
from src.web.pedido.pedido import pedidos
from src.domain.interfaces.pedido.pedido import Pedido


@pytest.fixture
def get_pedido(mocker: MockFixture) -> Mock:
    return mocker.patch('src.web.pedido.pedido.GetPedido')

@pytest.fixture
def post_pedidos(mocker: MockFixture) -> Mock:
    return mocker.patch('src.web.pedido.pedido.PostPedido')

@pytest.fixture
def injector(get_pedido: Mock, post_pedidos: Mock) -> None:
    inject.clear_and_configure(lambda binder: binder
                               .bind(GetPedido, get_pedido)
                               .bind(PostPedido, post_pedidos))

@pytest.fixture
def client(injector: None) -> FlaskClient:
    application = Flask(__name__)
    application.register_blueprint(pedidos())
    application.testing = True
    return application.test_client()

@pytest.fixture
def pedido() -> Pedido:
    return Pedido(1,"Pedido 1")

class TestPedido:
    def test_get_pedidos(self, client: FlaskClient, get_pedido: Mock, pedido: Pedido) -> None:
        get_pedido.execute.return_value = pedido
        response = client.get('/get_pedidos')
        assert response.json == {'pedidos': pedido.to_dict()}
    
    def test_post_pedido(self, client: FlaskClient, post_pedidos: Mock, pedido: Pedido) -> None:
        post_pedidos.execute.return_value = pedido
        response = client.post('/post_pedido', json=pedido.to_dict())
        assert response.json == {'pedidos': pedido.to_dict()}
    
    def test_post_pedido_status_code_400_TypeErrror(self, client: FlaskClient, post_pedidos: Mock, pedido: Pedido) -> None:
        post_pedidos.execute.return_value = None
        response = client.post('/post_pedido', json={'id': 1, 'title': 'Pedido 1', 'campo':'valor'} )
        assert response.status_code == 400
    
    def test_post_pedido_not_dict(self, client: FlaskClient, post_pedidos: Mock, pedido: Pedido) -> None:
        post_pedidos.execute.return_value = pedido
        response = client.post('/post_pedido', json=pedido.to_json())
        assert response.json == {'pedidos': pedido.to_dict()}

#if __name__ == '__main__':
#    pytest.main()