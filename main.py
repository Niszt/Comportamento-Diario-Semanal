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
        
        return (f"usuario: {usuario}\n"
                f"dia consultado: {dia_semana}\n"
                f"prioridade: {self.prioridade}\n"
                f"mensagem: {mensagem}")
        
class EstratégiaTercaFeira(EstratégiaDia):
    prioridade = "ALTA"
    def executar(self, usuario: str, informacao: str, dia_semana: str) -> str:
        mensagem = f"avance nas tarefas pendentes. A meta é '{informacao}'."
        return (f"usuario: {usuario}\n"
                f"dia consultado: {dia_semana}\n"
                f"prioridade: {self.prioridade}\n"
                f"mensagem: {mensagem}")
class EstratégiaQuartaFeira(EstratégiaDia):
    prioridade = "MÉDIA"
    def executar(self, usuario: str, informacao: str, dia_semana: str) -> str:
        mensagem = f"dia de revisão, verifique o andamento da atividade '{informacao}'."
        return (f"usuario: {usuario}\n"
                f"dia consultado: {dia_semana}\n"
                f"prioridade: {self.prioridade}\n"
                f"mensagem: {mensagem}")
class EstratégiaQuintaFeira(EstratégiaDia):
    prioridade = "BAIXA"
    def executar(self, usuario: str, informacao: str, dia_semana: str) -> str:
        mensagem = f"colabore com alguém da equipe. inicie com '{informacao}'."
        return (f"usuario: {usuario}\n"
                f"dia consultado: {dia_semana}\n"
                f"prioridade: {self.prioridade}\n"
                f"mensagem: {mensagem}")


if __name__ == "__main__":
    estrategia_segunda = EstratégiaSegundaFeira()
    resultado = estrategia_segunda.executar(
        usuario="Nick", 
        informacao="definir cronograma do projeto e dividir as funcoes do trabalho", 
        dia_semana="segunda-feira"
    )
    
    print(resultado)