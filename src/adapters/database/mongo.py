

from random import random
from typing import List
from src.domain.interfaces.database.database import DatabaseInterface
from src.domain.interfaces.pedido.pedido import Pedido

pedidos_db = [
    {'id': 0, 'title': 'Pastel'},
    {'id': 1, 'title': 'Pizza'},
    {'id': 2, 'title': 'Sushi'},
]


class MongoAdapter(DatabaseInterface):
    def get_pedidos(self) -> List[Pedido]:
        return [Pedido(**pedido) for pedido in pedidos_db]

    def post_pedido(self, pedido: Pedido) -> List[Pedido]:
        pedidos_db.append(pedido.__dict__)
        return [Pedido(**pedido) for pedido in pedidos_db]

    def get_next_id(self) -> int:
        # retorna id randomico interiro
        return int(random() * 100)
