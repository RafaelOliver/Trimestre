from datetime import datetime
from datetime import date

# Retorna sempre o trimestre anterior 
def Retorno_Trimestre():

    # Pega o numero do mes e o ano em que estamos
    Nun_Mes = datetime.strftime(date.today(), "%m")
    Ano = datetime.strftime(date.today(), "%Y")
    Trimeste_Anterior = ""
    Ano_Retorno = ""
    DataFinal = ""

    # Pego a descrição do mes em que estamos
    if Nun_Mes[0:1] == 0:
        Nome_Mes = Pegar_Mes(int(Nun_Mes[1:2]) - 1)
    else:
        Nome_Mes = Pegar_Mes(int(Nun_Mes) - 1)
    
    # Pega o trimestre anterior
    Trimeste_Anterior = Localizar_O_Trimeste(str(Nome_Mes))

    # Se o trimestre for Dezembro
    if Trimeste_Anterior == "Dezembro":

        # Se o trimestre cair em dezembro então precisamos trabalhar
        # com o dezembro do ano anterior ao de hoje
        Ano_Retorno = int(Ano) - 1

    else:

        Ano_Retorno = str(Ano)

    # Aqui pega o numero do mês do trimestre
    Mes_Retorno = Retorno_Num_Mes(Trimeste_Anterior)

    # Monta a data final 
    DataFinal = str(Mes_Retorno) + str(Ano_Retorno)

    # Retorna a Data Final
    return DataFinal

# Retorna o numero do mes do Trimestre
def Retorno_Num_Mes(Trimestre):

    # Compara os trimestre
    if Trimestre == "Março":
        return "03"

    if Trimestre == "Junho":
        return "06"

    if Trimestre == "Setembro":
        return "09"

    if Trimestre == "Dezembro":
        return "12"

# Localiza o trimestre
def Localizar_O_Trimeste(Mes):

    # Variaveis de ambiente
    i = 0
    Mes_Retorno = ""

    # Percorro todos os 12 meses
    while i <= 11:

        # Pego o mês
        Mes_Retorno = Pegar_Mes(i)

        # Compa os meses
        if Mes.upper() == Mes_Retorno.upper():

            # Pega o trimestre
            return Pegar_Trimestre(i)

        i = i  + 1


# Pega o mes com base no numero do mês passado
def Pegar_Mes(id):
    
    # Cria uma lista com todos os meses
    Lista_Mes = []
 
    # Adiciona todos os mesese dentro da lista
    Lista_Mes.append("Janeiro")   # 0
    Lista_Mes.append("Fevereiro") # 1 
    Lista_Mes.append("Março")     # 2  ( - )
    Lista_Mes.append("Abril")     # 3
    Lista_Mes.append("Maio")      # 4
    Lista_Mes.append("Junho")     # 5  ( - )
    Lista_Mes.append("Julho")     # 6
    Lista_Mes.append("Agosto")    # 7
    Lista_Mes.append("Setembro")  # 8  ( - )
    Lista_Mes.append("Outubro")   # 9
    Lista_Mes.append("Novembro")  # 10
    Lista_Mes.append("Dezembro")  # 11 ( - )

    return Lista_Mes[id]

# Retorna o trimestre
def Pegar_Trimestre(id):

    # Lista Trimestre
    Lista_Trimestre = []

    # Adciona os trimestre em Uma lista
    Lista_Trimestre.append("Março")
    Lista_Trimestre.append("Junho")
    Lista_Trimestre.append("Setembro")
    Lista_Trimestre.append("Dezembro")

    # Dezembro
    if id >= 0 and id <= 2:
        return Lista_Trimestre[3]

    # Março
    if id >= 3 and id <= 5:
        return Lista_Trimestre[0]
    
    # Junho
    if id >= 6  and id <= 8:
        return Lista_Trimestre[1]
    
    # Setembro
    if id >= 9  and id <= 11:
        return Lista_Trimestre[2]

