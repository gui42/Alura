from datetime import datetime
class Datas:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        messes = [
                'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
                ]
        mes = self.momento_cadastro.month
        return messes[mes-1]

    def dia_semana(self):
        dias_semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado','domingo']
        dia = self.momento_cadastro.weekday()
        return dias_semana[dia]  
       
    def formata_data(self):
        return self.momento_cadastro.strftime("%d/%m/%Y  %H:%M")

    def tempo_cadastro(self):
        return datetime.today() - self.momento_cadastro
