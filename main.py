from abc import ABC, abstractmethod

class EstratégiaDia(ABC):
    
    @property
    @abstractmethod
    def prioridade(self) -> str:
        pass

    @abstractmethod
    def executar(self, usuario: str, informacao: str, dia_semana: str) -> str:
        pass


class EstratégiaSegundaFeira(EstratégiaDia):
    
    @property
    def prioridade(self) -> str:
        return "ALTA"  # Segunda Organiza as prioridades, planejamento é importante para qualquer projeto
        
    def executar(self, usuario: str, informacao: str, dia_semana: str) -> str:
        mensagem = f"organize suas prioridades. A meta é '{informacao}'."
        
        return (f"Usuário: {usuario}\n"
                f"Dia consultado: {dia_semana}\n"
                f"Prioridade: {self.prioridade}\n"
                f"Mensagem: {mensagem}")


if __name__ == "__main__":
    pass