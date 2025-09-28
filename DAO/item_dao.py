import sqlite3
from Model.item import Item

class ItemDAO:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self._criar_tabela()

    def _criar_tabela(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS itens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                quantidade INTEGER NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def adicionar(self, item: Item):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO itens (descricao, quantidade) VALUES (?, ?)",
                       (item.descricao, item.quantidade))
        conn.commit()
        conn.close()

    def listarTodos(self) -> list[Item]:
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT id, descricao, quantidade FROM itens")
        rows = cursor.fetchall()
        conn.close()

        itens = [Item(id=row[0], descricao=row[1], quantidade=row[2]) for row in rows]
        return itens
 