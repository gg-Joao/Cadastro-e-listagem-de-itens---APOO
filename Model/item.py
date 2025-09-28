class Item:
    def __init__(self, id: int, descricao: str, quantidade: int):
        self.id = id
        self.descricao = descricao
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.id} - {self.descricao} ({self.quantidade})"
        