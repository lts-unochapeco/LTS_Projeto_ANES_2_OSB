# Build-in Libraries
from datetime import datetime

# Custom Modules
#from modules.output import Output

# Define uma classe chamada `Time` para agrupar todas as funções relacionadas a tempo.
class Time:
    @staticmethod
    def get_now(): # Retorna a data e hora atuais.
        try:
            atual = datetime.now()
            return atual # Retorna um objeto datetime com a data e hora atuais.

        except Exception as warning:
            return #Output.warning(warning, observation="Getting the current date and time")

    @staticmethod
    def pegando_lista_atual(): # Retorna a data e hora atuais em uma lista de inteiros.
        data_atual = Time.get_now()
        # Retorna a data e hora atuais em uma lista de inteiros(Uma lista contendo [ano, mês, dia, hora, minuto, segundo].).
        return [
            data_atual.year,
            data_atual.month,
            data_atual.day,
            data_atual.hour,
            data_atual.minute,
            data_atual.second
        ]

    @staticmethod
    def mudando_para_datetime(date_string, format="%d/%m/%Y"): # Converte uma string de data para um objeto datetime.
        try:
            data_datetime = datetime.strptime(str(date_string), str(format))
            return data_datetime # O objeto datetime correspondente à data.

        except Exception as warning:
            return #Output.warning(warning, observation="Trying to convert a string to a datetime object")

    @staticmethod
    def mudando_para_string(date, format="%d/%m/%Y"): # Converte um objeto datetime para uma string.
        try:
            data_string = date.strftime(str(format))
            return data_string # A string formatada da data.

        except Exception as warning:
            return #Output.warning(warning, observation="Trying to convert a datetime object to a string")

    @staticmethod
    def __change_to_datatime_with_re(data_informada): #Converte uma string de data com nomes de meses em português para um objeto date.
                                                      #Esta é uma função interna, indicada pelo duplo underscore (__).
        data_informada = data_informada.replace("  ", " ")
        data_informada = data_informada.replace(u' de ', u'/')
        data_informada = data_informada.replace(u'janeiro', u'01')
        data_informada = data_informada.replace(u'Janeiro', u'01')
        data_informada = data_informada.replace(u'fevereiro', u'02')
        data_informada = data_informada.replace(u'Fevereiro', u'02')
        data_informada = data_informada.replace(u'março', u'03')
        data_informada = data_informada.replace(u'Março', u'03')
        data_informada = data_informada.replace(u'abril', u'04')
        data_informada = data_informada.replace(u'Abril', u'04')
        data_informada = data_informada.replace(u'maio', u'05')
        data_informada = data_informada.replace(u'Maio', u'05')
        data_informada = data_informada.replace(u'junho', u'06')
        data_informada = data_informada.replace(u'Junho', u'06')
        data_informada = data_informada.replace(u'julho', u'07')
        data_informada = data_informada.replace(u'Julho', u'07')
        data_informada = data_informada.replace(u'agosto', u'08')
        data_informada = data_informada.replace(u'Agosto', u'08')
        data_informada = data_informada.replace(u'setembro', u'09')
        data_informada = data_informada.replace(u'Setembro', u'09')
        data_informada = data_informada.replace(u'outubro', u'10')
        data_informada = data_informada.replace(u'Outubro', u'10')
        data_informada = data_informada.replace(u'novembro', u'11')
        data_informada = data_informada.replace(u'Novembro', u'11')
        data_informada = data_informada.replace(u'dezembro', u'12')
        data_informada = data_informada.replace(u'Dezembro', u'12')

        data_informada = Time.mudando_para_datetime(str(data_informada)).date()
        return data_informada # Um objeto date com a data convertida.

    @staticmethod                      # Converte strings de data de textos em português para objetos date.
    def pegando_o_texto(data_informada): # Lida tanto com strings únicas quanto com listas de strings.
        if type(data_informada) is str:
            datatime = Time.__change_to_datatime_with_re(data_informada)
            return datatime # Um objeto date

        # Ou

        elif type(data_informada) is list:
            for i in range(len(data_informada)):
                data_informada[i] = Time.__change_to_datatime_with_re(data_informada[i])

            return data_informada # Uma lista de objetos date convertidos.
