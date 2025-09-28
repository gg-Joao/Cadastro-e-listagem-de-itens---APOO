from DAO.item_dao import ItemDAO
from Model.item import Item

class ItemController:
    def __init__(self):
        self.dao = ItemDAO()

    def criarItem(self, descricao: str, quantidade: int):
        item = Item(id=None, descricao=descricao, quantidade=quantidade)
        self.dao.adicionar(item)

    def obterTodosOsItens(self) -> list[Item]:
        return self.dao.listarTodos()