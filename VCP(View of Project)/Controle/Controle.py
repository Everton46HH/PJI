import mysql.connector
import os
import time


class BancoDeDados:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def conectar(self):
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
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
        db.cursor.execute(f"UPDATE usuario SET nome = '{novoNome}' WHERE id = {self.userId}")
        db.conexao.commit()

    def setSenha(self,novaSenha):
        db.cursor.execute(f"UPDATE usuario SET nome ='{novaSenha}') WHERE id = {self.userId}")


class Dispositivo:

    def __init__(self,idDispositivo, nomeDispositivo, longitude, latitude):
        self.idDispositivo = idDispositivo
        self.nomeDispositivo = nomeDispositivo
        self.longitude = longitude
        self.latitude = latitude

    def setNome(self, novoNome):
        self.nomeDispositivo = novoNome

    def getData(self):
        db.conectar()
        db.cursor.execute(f"SELECT idDispositivo,nomeDispositivo,latitude, longitude  FROM Dispositivo WHERE idDispositivo = {id}")
        dados = db.cursor.fetchone()
        db.cursor.close()
        return dados


def verificacao():
    print("\n====== BEM-VINDO AO PETAG ======")
    print("    ====== FAÇA LOGIN ======")
    userId = input("DIGITE SEU ID DE USUARIO: ")
    userSenha = input("DIGITE SUA SENHA: ")

    #Puxei a senha registrada do Banco de Dados usando o ID.
    db.conectar() #mexi aqui
    db.cursor.execute(f"SELECT senha FROM Usuario WHERE userID = {userId}")
    senha = db.cursor.fetchone()
    db.cursor.close()

    if senha is None:
        os.system('cls')
        print("ID DE USUARIO NÃO ENCONTRADO")
        return False
    
    #Ae como o senha é igual a uma tupla e peguei primeiro index dele 
    senha = senha[0]
    
    if userSenha == senha:
        os.system('cls')
        print("ACESSO PERMTIDO :)")
        return True
    else:
        os.system('cls')
        print("ACESSO NEGADO,TENTE NOVAMENTE")
        return False
            
def menu():
    os.system('cls')
    print("=========   MENU  ==========")
    print("1. CONSULTAR DISPOSITIVOS CONECTADOS")
    print("2. CONSULTAR COORDENADAS EM TEMPO REAL DE UM DISPOSITIVO")
    print("3. CONFIGURAÇÕES DE CONTA")
    print("4. Sair")
    print("=============================")

def accountConfig():
    os.system('cls')
    print("========= CONFIGURAÇÂO DE CONTA ACESSADA ==========")
    print("1. MUDAR SENHA")
    print("2. MUDAR EMAIL")
    

#Classe Do Banco de Dados
db = BancoDeDados(
    host="localhost",
    user="root",
    password="Janeiro.01",
    database="PeTAG"
)

#Instacia do usuario
user1 = Usuario(userId='',nome='',email='',senha='')

escolha = True

while True:

    if verificacao():
        
        db.conectar()
        # db.cursor.execute(f'SELECT * from Usuario where userID = {userID}')
        
        while escolha!=4:
            
            menu()

            escolha = int(input("DIGITE UMA OPÇÃO: "))

            if escolha == 1:

                db.conectar()
                print("OS DISPOSITIVOS CONECTADOS A BASE DE DADOS SÂO: ")
                aparelhos = db.aparelhosConectados()
                db.cursor.close()
                for aparelho in aparelhos:
                    print(aparelho)
                time.sleep(6)

            
            if escolha == 2:

                db.conectar() #mexi
                id = input("DIGITE UM ID: ")                
                db.cursor.execute(f"SELECT idDispositivo, nomeDispositivo, latitude, longitude FROM Dispositivo WHERE idDispositivo = {id}")
                
                resultado = db.cursor.fetchone()
                db.cursor.close()
                
                if resultado:
                        idDispositivo, nomeDispositivo, latitude, longitude = resultado
                        dispositivo1 = Dispositivo(
                        idDispositivo=idDispositivo,
                        nomeDispositivo=nomeDispositivo,
                        latitude=latitude,
                        longitude=longitude 
                    )
                        
                for i in range(0, 100, 1):
                    registro = dispositivo1.getData()

                    #essa linha de código ,pega a loc atual e salva no historico :)
                    #quebrei a cabeça pensando nisso 
                    print(registro)
                    db.conectar()
                    db.cursor.execute(f"insert into HistoricoCoordenadas(idDispositivo,latitude,longitude) values({registro[0]}, {registro[2]}, {registro[3]})")
                    db.cursor.close()

                    time.sleep(0.5)
                    db.conexao.commit()

            if escolha == 3:
                accountConfig()
                senhaAtual = input("Digite sua senha atual: ")

                # if senhaAtual == user.senha