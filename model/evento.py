class Eventos():

    def __init__(self, id, nome, categoria, local, organizador, email):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.local = local
        self.organizador = organizador
        self.email = email

    def atualizar(self, dados):
        try:
            id = dados["id"]
            nome = dados["nome"]
            categoria = dados["categoria"]
            local = dados["local"]
            organizador = dados["organizador"]
            email = dados["email"]
            self.id, self.nome, self.categoria, self.local, self.organizador, self.email = id, nome, categoria, local, organizador, email
            return self
        except Exception as e:
            print("Problema ao atualizar seu evento!")
            print(e)

    def __dict__(self):
        d = dict()
        d["id"] = self.id
        d["nome"] = self.nome
        d["categoria"] = self.categoria
        d["local"] = self.local
        d["organizador"] = self.organizador
        d["email"] = self.email
        return d
        
    @staticmethod
    def criar(self):
        try:
            id = self["id"]
            nome = self["nome"]
            categoria = self["categoria"]
            local = self["local"]
            organizador = self["organizador"]
            email = self["email"]
            return Eventos(id=id, nome=nome, categoria=categoria, local=local, organizador=organizador, email=email)
        except Exception as e:
            print("Problema ao criar seu evento!")
            print(e)