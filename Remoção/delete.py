import mysql.connector

def delete_cliente(self, cpf: str):
    """Deleta um cliente do banco de dados pelo CPF"""
    cursor = self.connection.cursor()
    query = """
        DELETE FROM cliente
        WHERE cpf = %s
    """
    cursor.execute(query, (cpf,))
    self.connection.commit()
    cursor.close()
    print("Cliente deletado com sucesso!")
