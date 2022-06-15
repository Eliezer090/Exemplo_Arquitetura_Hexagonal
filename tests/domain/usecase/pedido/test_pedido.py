from unittest.mock import Mock
import pytest
import inject
from src.domain.actions.database.database import DatabaseActions
from src.domain.interfaces.database.database import DatabaseInterface
from src.domain.interfaces.pedido.pedido import Pedido
from src.domain.usecase.pedido.pedido import PedidoUseCase

@pytest.fixture
def database() -> Mock:
    # Mockando a base de dedos
    return Mock()

@pytest.fixture
def injector(database: Mock) -> None:
    inject.clear_and_configure(lambda binder: binder
                               .bind(DatabaseInterface, database))

@pytest.fixture
def pedido() -> Pedido:
    return Pedido(1, 'PedidoTeste')

class TestPedidoUseCase:

    def test_getPedidosList(self, injector: None, database: Mock, pedido: Pedido):
        #O "get_pedidos" abaixo é da interface do database
        database.get_pedidos.return_value = pedido
        result = PedidoUseCase(DatabaseActions()).getPedidosList()
        assert result == pedido

    def test_post_pedido(self, injector: None, database: Mock, pedido: Pedido):
        #O "post_pedido" abaixo é da interface do database
        database.post_pedido.return_value = pedido
        result = PedidoUseCase(DatabaseActions()).post_pedido(pedido)
        assert result == pedido

#if __name__ == '__main__':
#    pytest.main()