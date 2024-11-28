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
        self.cursor.execute("SELECT idAparelho FROM PeTag")
        return self.cursor.fetchall()

    def getCoords(self, idDispositivo):
        self.cursor.execute(f"SELECT latitude, longitude, nomePet FROM pet WHERE idDispositivo = {idDispositivo}")
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

db = BancoDeDados(
    host="localhost",
    user="root",
    password="Janeiro.01",
    database="PeTAG"
)

dispositivo1 = Dispositivo(nomeDispositivo='Rex', idDispositivo=1)

coords = db.getCoords(dispositivo1.idDispositivo)
if coords:
    latitude, longitude, nome_pet = coords
    dispositivo1.setCoords((latitude, longitude))
    dispositivo1.setNome(nome_pet)
    print(f"Coordenadas atualizadas: Latitude {latitude}, Longitude {longitude}")
else:
    print("Dispositivo não encontrado no banco de dados.")

if __name__ == "__main__":
    print("BEM-VINDO!!!")
    print("Os dispositivos conectados à base de dados são:")
    aparelhos = db.aparelhosConectados()
    for aparelho in aparelhos:
        print(aparelho)
