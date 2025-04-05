import mysql.connector

def update_cliente(self, cpf: str, novos_dados: dict):
        """Atualiza os dados de um cliente no banco de dados"""
        cursor = self.connection.cursor()
        set_clause = ", ".join([f"{chave} = %s" for chave in novos_dados.keys()])
        valores = list(novos_dados.values()) + [cpf]
        query = (f"""
            UPDATE cliente
            SET {set_clause}
            WHERE cpf = %s
        """)
        cursor.execute(query, valores)
        self.connection.commit()
        cursor.close()
        print("Cliente atualizado com sucesso!")