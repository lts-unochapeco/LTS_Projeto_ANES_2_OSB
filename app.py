from time import sleep

# Processos
from processos.preparando_website import pegando_avisos_abertos
from processos.extraindo_informacoes import pegando_informacoes
from processos.extraindo_informacoes_inexequibilidade import pegando_avisos_inexequibilidades
from processos.enviando_email import enviando_relatorio_email
from processos.cod_parada import PegandocodParada

# Modulos
from modulos.formato_arquivo import CSV, salvando_dados_mongodb

condicao2 = None

def main():
    arquivos = []

    links_avisos_abertos = pegando_avisos_abertos()
    dicionario_avisos_abertos = pegando_informacoes(links_avisos_abertos)
    arquivo1 = CSV(dicionario_avisos_abertos)
    salvando_dados_mongodb(dicionario_avisos_abertos)

    links_inexequibilidades = pegando_avisos_inexequibilidades()
    dicionario_inexequibilidade = pegando_informacoes(links_inexequibilidades)
    arquivo2 = CSV(dicionario_inexequibilidade)
    salvando_dados_mongodb(dicionario_inexequibilidade)    
    
    arquivos.append(arquivo1)
    arquivos.append(arquivo2)

    enviando_relatorio_email(arquivos)

# if __name__ == "__main__":
while True:

    condicao1 = PegandocodParada()

    print(condicao1)
    print(condicao2)

    if condicao2 is None:
        condicao2 = condicao1
        print("Monitoramento iniciado. Referência estabelecida.")
        main()
        sleep(3600)
        continue # Vai para a próxima checagem sem rodar o main()

    elif condicao1 != condicao2:

        print(f"   repr(Anterior): {repr(condicao2)}") 
        print(f"   repr(Atual):    {repr(condicao1)}")

        main()  

        condicao2 = condicao1
        print(condicao1)
        print(condicao2)
    else:
        print("Nenhuma alteração no portal de transparência")

    sleep(3600)
