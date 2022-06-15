import pytest
from typing import List
from src.adapters.database.mongo import MongoAdapter
from src.domain.interfaces.pedido.pedido import Pedido


@pytest.fixture
def database() -> MongoAdapter:
    return MongoAdapter()


@pytest.fixture
def pedido() -> Pedido:
    # Aqui será feito um post na base de dados mesmo para podermos testar
    fetched_post = MongoAdapter().post_pedido(Pedido(1, 'TileTeste'))
    return fetched_post


class TestMongoAdapter:
    def test_get_pedidos(self, database: MongoAdapter, pedido: Pedido):
        fetched_pedidos = database.get_pedidos()
        assert fetched_pedidos == pedido

    def test_post_pedido(self, database: MongoAdapter, pedido: Pedido):
        fetched_post = database.post_pedido(Pedido(1, 'TileTeste'))
        # Pega só o ultimo pedido e compara, pois a base de dados é fixo
        assert fetched_post[len(fetched_post)-1] == pedido[len(pedido)-1]

    def test_get_next_id(self, database: MongoAdapter):
        fetched_id = database.get_next_id()
        assert isinstance(fetched_id, int)
