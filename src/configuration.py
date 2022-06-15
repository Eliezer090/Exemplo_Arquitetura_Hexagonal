import inject
from flask import Flask
from src.adapters.database.mongo import MongoAdapter
from src.domain.actions.database.database import DatabaseActions
from src.domain.interfaces.database.database import DatabaseInterface
from src.domain.interfaces.pedido.pedidoInterface import PedidoInterface
from src.domain.usecase.pedido.pedido import PedidoUseCase


def configure_inject(application: Flask) -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(DatabaseInterface, MongoAdapter)
        binder.bind(PedidoInterface, PedidoUseCase(DatabaseActions()))

    inject.configure(config)
