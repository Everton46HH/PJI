class Usuario:
    def __init__(self,nome,email,senha,aparelhosConectados):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.aparelhosConectados = aparelhosConectados
    def setNome(self,novoNome):
        self.nome = novoNome
    def setSenha(self,novaSenha):
        self.senha = novaSenha
    def trocarSenha(self,novaSenha):
        self.senha = novaSenha
    def showAparelhosConectados(self):
        return self.aparelhosConectados
    def setNovoAparelho(self,novoAparelho):
        if novoAparelho not in self.aparelhosConectados:
            self.aparelhosConectados.append(novoAparelho)
aparelhosDetectados = ['ex1','ex2','ex3']
user2 = Usuario(nome = '',email = '',senha = '',aparelhosConectados = [])
x=-1
y=0
while (y!=1):
    user2.nome = input('digite seu nome')
    user2.email = input('digite seu email como no exemplo: example123@gmail.com')
    novaSenha = input('digite sua senha')
    user2.setSenha(novaSenha)
    if(user2.nome == "" or user2.email == "" or novaSenha == ""):
        print("Erro: Algum dos campos acima possui um valor invalido.")
    else:
        y = 1
    
while (x!=7):
    print('1-deseja trocar sua senha?')
    print('2-ver aparelhos conectados')
    print('3-ver aparelhos disponiveis')
    print('4-selecionar um dos aparelhos disponiveis')
    print('5-esqueceu sua senha?')
    x = int(input('escolha '))
    if (x==1):
        conf = input('digite sua senha atual')
        if (conf == user2.senha):
            novaSenha = input('digite sua nova senha')
            user2.trocarSenha(novaSenha)
            print('senha trocada')
        else:
            print('senha descrepante. Digite a senha correta')
    elif (x==2):
        if (user2.aparelhosConectados == []):
            print('não há aparelhos conectados')
        else:
            print(user2.showAparelhosConectados())
    elif (x==3):
        print(aparelhosDetectados)
    elif (x==4):
        novoAparelho = input('selecione o novo aparelho de acordo com os aparelhos detectados')
        if (novoAparelho not in aparelhosDetectados):
            print('selecione um aparelho dentre a lista')
        else:
            user2.setNovoAparelho(novoAparelho)
            print('o aparelho foi conectado')
    elif (x==5):
        print('infelizmente não temos recursos para ajuda-lo.')

class Dispositivo():
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
    def getNome(self):
        return self.nome
    def setNome(self, nome2):
        self.nome = nome2
    def getTipo(self):
        return self.tipo

class Transmissor(Dispositivo):
    def __init__(self, nome, tipo, alcance, rede):
        Dispositivo.__init__(self, nome, tipo)
        self.alcance = alcance
        self.rede = rede
    def getAlcance(self):
        return self.alcance
    def setAlcance(self, alcance2):
        self.alcance = alcance2
    def getRede(self):
        return self.rede
    def setRede(self, rede2):
        self.rede = rede2

class Receptor(Dispositivo):
    def __init__(self, nome, tipo, fuga, localiz):
        Dispositivo.__init__(self, nome, tipo)
        self.fuga = fuga
        self.localiz = localiz
    def getFuga(self):
        return self.fuga
    def setFuga(self, fuga2):
        self.fuga = fuga2
    def getLocaliz(self):
        return self.localiz
    def setLocaliz(self, localiz2):
        self.localiz = localiz2

d1 = Transmissor("Sala", "Transmissor", "30m", "Wi-fi JoãozinhoDosMontes4G")
d2 = Receptor("Bob", "Receptor", "está dentro do domínio", "Bragança Paulista, São Miguel")

print(" --> O objeto D1 é um:\n ", d1.getTipo())
print("--> O alcance do objeto D1 é:\n", d1.getAlcance())
d1.setAlcance("40m")
print("--> Alterei o alcance do transmissor, então o alcance do D1 agora é:\n", d1.getAlcance())
print("--> A rede do objeto D1 é:\n", d1.getRede())
d1.setRede("Wifi 10 números de Pliô")
print("--> Alterei a rede do transmissor, então a rede do D1 agora é:\n", d1.getRede(), "\n\n")

print(" --> O objeto D2 é um:\n ", d2.getTipo())
print("--> O objeto D2 pertence à:\n", d2.getNome())
d2.setNome("Valentina")
print("--> Alterei o nome do receptor, então o objeto D2 agora pertence à:\n", d2.getNome())
print("--> Valentina está dentro de casa?\n", d2.getNome(), d2.getFuga())
d2.setFuga("fugiu!!")
print("\n", d2.getNome(), d2.getFuga())