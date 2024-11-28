import mysql.connector

class BancoDeDados:
    def __init__(self, host, user, password, database):
        self.conexao = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conexao.cursor()

    def aparelhosConectados(self):
        self.cursor.execute("SELECT idDispositivo,nomeDispositivo FROM Dispositivo")
        return self.cursor.fetchall()

    def getCoords(self, idDispositivo):
        self.cursor.execute(f"SELECT latitude, longitude, nomeDispositivo FROM Dispositivo WHERE idDispositivo = {idDispositivo}")
        return self.cursor.fetchone()

class Usuario:
    def __init__(self, userId, nome, email, senha):
        self.userId = userId
        self.nome = nome
        self.email = email
        self.senha = senha

    def setNome(self, novoNome):
        db.cursor.execute(f"UPDATE usuarios SET nome = '{novoNome}' WHERE id = {self.userId}")
        db.conexao.commit()

    def trocarSenha(self, novaSenha):
        db.cursor.execute(f"UPDATE usuarios SET senha = '{novaSenha}' WHERE id = {self.userId}")
        db.conexao.commit()


class Dispositivo:
    def __init__(self, nomeDispositivo, idDispositivo, longitude=None, latitude=None):
        self.nomeDispositivo = nomeDispositivo
        self.idDispositivo = idDispositivo
        self.coord = (longitude, latitude)

    def setCoords(self, novasCoords):
        self.coord = novasCoords

    def setNome(self, novoNome):
        self.nomeDispositivo = novoNome


def verificacao():
    print("\n====== BEM-VINDO AO PETAG ======")
    print("    ====== FAÇA LOGIN ======")
    userId = input("DIGITE SEU ID DE USUARIO: ")
    userSenha = input("DIGITE SUA SENHA: ")

    #Puxei a senha registrada do Banco de Dados usando o ID.
    db.cursor.execute(f"SELECT senha FROM Usuario WHERE userID = {userId}")
    senha = db.cursor.fetchone()

    #Ae como o senha é igual a uma tupla e peguei primeiro index dele 
    senha = senha[0]

    if userSenha == senha:
        print("ACESSO PERMTIDO :)")
        return True
    else:
        print("ACESSO NEGADO,TENTE NOVAMENTE")
        return False

            
# def menu():
#     print("============MENU=============")
#     print("1. VER DISPOSITIVOS CONECTADOS A BASE DE DADOS")
#     print("2. CONFIGURAÇÃO DE CONTA")
#     print("3. Sair")
#     print("=============================")
#     escolha = input("")
#     return escolha


#Classe Do Banco de Dados
db = BancoDeDados(
    host="localhost",
    user="root",
    password="Janeiro.01",
    database="PeTAG"
)

#Classe do 'dispositivo' do Banco De Dados
dispositivo1 = Dispositivo(nomeDispositivo='', idDispositivo=1)
#Esse dispostivo nao possui conexao com bdd,apenas depois os dados sao inseridos ,puxados do BDD
#Pensei em criar um função que tivesse um FOR que puxasse do BDD os dipositivos conectados ae o programa instancia cada um dos dispositvos disponiveis

#Instacia do usuario

user1 = Usuario(userId='',nome='',email='',senha='')

# coords = db.getCoords(dispositivo1.idDispositivo)

# if coords:
#     latitude, longitude, nome_pet = coords
#     dispositivo1.setCoords((latitude, longitude))
#     dispositivo1.setNome(nome_pet)
# else:
#     print("Dispositivo não encontrado no banco de dados.")

if __name__ == "__main__":

    while not verificacao():
            print("TESTANDO GITHUB sfvbsbb")
        # menu()
        # while escolha != False:
        #     print("OS DISPOSITIVOS CONECTADOS A BASE DE DADOS SÂO: ")
        #     aparelhos = db.aparelhosConectados()
        #     for aparelho in aparelhos:
        #         print(aparelho)

    # ID = input("Digite o ID da coleira")