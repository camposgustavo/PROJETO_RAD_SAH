from datetime import datetime
from pydantic import BaseModel, field_validator
from typing import Optional


class ClienteInput(BaseModel):
    """Modelo para entrada de dados do cliente"""
    nome: str
    cpf: str
    quarto: int
    check_in: datetime
    check_out: datetime
    cafe_manha: bool = False
    periodo: str

    @field_validator('periodo')
    def validar_periodo(cls, periodo: str) -> str:
        """Garante que o período seja 'diária' ou 'semanal'"""
        if periodo.lower() not in {"diária", "semanal"}:
            raise ValueError('Período inválido: deve ser "diária" ou "semanal"')
        return periodo

    @field_validator('check_in', 'check_out')
    def validar_formato_data(cls, data: str) -> str:
        """Valida o formato DD/MM/AAAA HH:MM"""
        try:
            datetime.strptime(data, "%d/%m/%Y %H:%M")
            return data
        except ValueError:
            raise ValueError("Formato de data inválido. Use: dd/mm/aaaa HH:MM")

class ClienteValidado(ClienteInput):
    """Modelo estendido com datas convertidas para datetime"""
    check_in: datetime
    check_out: datetime

def validar_cadastro(dados: ClienteInput) -> ClienteValidado:
    """Valida e converte os dados do cliente"""
    check_in = datetime.strptime(dados.check_in, "%d/%m/%Y %H:%M")
    check_out = datetime.strptime(dados.check_out, "%d/%m/%Y %H:%M")
    
    if check_out <= check_in:
        raise ValueError("Check-out deve ser posterior ao check-in")
    
    return ClienteValidado(**dados.model_dump(), check_in=check_in, check_out=check_out)




if "__name__"=="__main__":
    main()