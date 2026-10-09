class ProcessadorDeAcoes:

    def validar_dados(self, dados: dict) -> bool:
        return True

    def salvar_dados(self, dados: dict) -> bool:
        return True

    def executar_processo(self, dados: dict) -> str:

        if self.validar_dados(dados):
            if self.salvar_dados(dados):
                return "Processo executado com sucesso."

            return "Falha ao salvar os dados."

        return "Falha na validação dos dados."