

import pytest
import inject
from unittest.mock import Mock
from src.domain.actions.pedido.get_pedidos import GetPedido
from src.domain.actions.pedido.post_pedido import PostPedido
from src.domain.interfaces.pedido.pedido import Pedido

from src.domain.interfaces.pedido.pedidoInterface import PedidoInterface


@pytest.fixture
def pedidoMock() -> Mock:
    return Mock()

@pytest.fixture
def injector(pedidoMock:Mock) -> None:
    inject.clear_and_configure(lambda binder: binder
                               .bind(PedidoInterface, pedidoMock))


@pytest.fixture
def pedido() -> Pedido:
    return Pedido(1, 'PedidoTeste')
    
class TestActionGetPedido:
    def test_get_pedidos(self, injector: None, pedidoMock: Mock, pedido: Pedido):
        pedidoMock.getPedidosList.return_value = pedido
        result = GetPedido().execute()
        assert result == pedido
    
    def test_post_pedido(self, injector: None, pedidoMock: Mock, pedido: Pedido):
        pedidoMock.post_pedido.return_value = pedido
        result = PostPedido().execute(pedido)
        assert result == pedido

#if __name__ == '__main__':
#    pytest.main()