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
        
class EstratégiaTercaFeira(EstratégiaDia):
    prioridade = "ALTA"
    def executar(self, usuario: str, info_adicional: str) -> str:
        return f"avance nas tarefas pendentes. A meta é '{info_adicional}'."

class EstratégiaQuartaFeira(EstratégiaDia):
    prioridade = "MÉDIA"
    def executar(self, usuario: str, info_adicional: str) -> str:
        return f"dia de revisão, verifique o andamento da atividade '{info_adicional}'."

class EstratégiaQuintaFeira(EstratégiaDia):
    prioridade = "BAIXA"
    def executar(self, usuario: str, info_adicional: str) -> str:
        return f"colabore com alguém da equipe. inicie com '{info_adicional}'."

class EstratégiaSextaFeira(EstratégiaDia):
    prioridade = "MÉDIA"
    def executar(self, usuario: str, info_adicional: str) -> str:
        return f"registre o que foi concluído. pendencia: '{info_adicional}'."

class EstratégiaSabado(EstratégiaDia):
    prioridade = "BAIXA"
    def executar(self, usuario: str, info_adicional: str) -> str:
        return f"realize estudo livre ou descanso. o que planejei '{info_adicional}'."

class EstratégiaDomingo(EstratégiaDia):
    prioridade = "MÉDIA"
    def executar(self, usuario: str, info_adicional: str) -> str:
        return f"planeje a próxima semana. foque nessa semana em '{info_adicional}'."

if __name__ == "__main__":
    estrategia_segunda = EstratégiaSegundaFeira()
    resultado = estrategia_segunda.executar(
        usuario="Nick", 
        informacao="definir cronograma do projeto e dividir as funcoes do trabalho", 
        dia_semana="segunda-feira"
    )
    
    print(resultado)