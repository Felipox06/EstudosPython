class SistemaAutenticacao:
    def __init__(self):
        self.login = {}

    def registrar(self, usuario, senha):
        if usuario in self.login:
            print("Usuário já existe.")
        else:
            self.login[usuario] = senha
            print("Registrado com sucesso.")

    def cadastro(self, usuario, senha):
        if usuario in self.login and self.login[usuario] == senha:
            print("Login bem-sucedido.")
        else:
            print("Credenciais incorretas.")

# Teste
sistema = SistemaAutenticacao()
sistema.registrar("alice", "1234")
sistema.cadastro("alice", "1234")
sistema.cadastro("bob", "5678")