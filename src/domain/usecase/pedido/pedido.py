
from typing import List
from src.domain.actions.database.database import DatabaseActions
from src.domain.interfaces.pedido.pedido import Pedido
from src.domain.interfaces.pedido.pedidoInterface import PedidoInterface


class PedidoUseCase(PedidoInterface):
    
    def __init__(self, database: DatabaseActions):
        self.databaseAction = database

    def getPedidosList(self) -> List[Pedido]:
        return self.databaseAction.get_pedidos()

    def post_pedido(self, pedido: Pedido) -> List[Pedido]:
        # databaseAction =
        if pedido.id < 5:
            pedido.id = self.databaseAction.get_next_id()
        return self.databaseAction.post_pedido(pedido)
