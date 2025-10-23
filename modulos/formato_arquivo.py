import csv
import pymongo


def CSV(lista_de_dicionarios):
    if not lista_de_dicionarios:
        print("A lista de dados está vazia. Nenhum arquivo será criado.")
        return

    campos = lista_de_dicionarios[0].keys()
    nome_arquivo = 'relatorio.csv'
    for dicionario_linha in lista_de_dicionarios:
        # Verifica se a modalidade é "Dispensa" ou "Inexigibilidade"
        if dicionario_linha.get('Modalidade') in ["Dispensa", "Inexigibilidade"]:
            nome_arquivo = 'relatorioInexigibilidade.csv'
            # Se encontrar pelo menos um, define o nome do arquivo e sai do loop
            break
            
    
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=campos, delimiter=';')
        writer.writeheader()
        writer.writerows(lista_de_dicionarios)
        
    print(f"O arquivo '{nome_arquivo}' foi salvo com sucesso!")

    return nome_arquivo


def salvando_dados_mongodb(lista_de_dados):
    
    if not lista_de_dados:
        print("A lista de dados está vazia. Nenhum dado será salvo no MongoDB.")
        return

    # A sua string de conexão com o MongoDB.
    # Se for uma instância local, o padrão é:
    uri = "mongodb://localhost:27017/"
    
    # Se for uma instância do MongoDB Atlas, use a sua URL completa.
    # Exemplo: uri = "mongodb+srv://<usuario>:<senha>@<cluster>.mongodb.net/"

    cliente = None # Define a variável fora do try para o finally poder acessá-la
    try:
        # Tenta se conectar ao cliente
        cliente = pymongo.MongoClient(uri)
        
        # Seleciona o banco de dados e a coleção onde os dados serão salvos.
        # Eles serão criados automaticamente se não existirem.
        db = cliente["anes"]
        colecao = db["banco"]
        
        # O método insert_many() é o mais eficiente para listas de dicionários
        colecao.insert_many(lista_de_dados)
        
        print(f"Dados salvos com sucesso na coleção '{colecao.name}'.")
        
    except pymongo.errors.ConnectionFailure as erro:
        print(f"Erro ao conectar ao MongoDB: {erro}")
    
    finally:
        # Garante que a conexão será fechada, mesmo se houver um erro
        if cliente:
            cliente.close()
