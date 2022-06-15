from typing import List
import inject
from src.domain.interfaces.database.database import DatabaseInterface
from src.domain.interfaces.pedido.pedido import Pedido


class DatabaseActions:
    @inject.autoparams()
    def get_pedidos(self, database: DatabaseInterface) -> List[Pedido]:
        return database.get_pedidos(self)

    @inject.autoparams()
    def get_next_id(self, database: DatabaseInterface) -> int:
        return database.get_next_id(self)

    @inject.autoparams('database')
    def post_pedido(self, pedido: Pedido, database: DatabaseInterface) -> List[Pedido]:
        return database.post_pedido(self, pedido)
