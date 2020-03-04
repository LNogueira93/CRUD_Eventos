class Eventos():

    def __init__(self, ident, nome, categoria, local, organizador, email):
        self.ident = ident
        self.nome = nome
        self.categoria = categoria
        self.local = local
        self.organizador = organizador
        self.email = email

    def atualizar(self, dados):
        try:
            ident = dados["ident"]
            nome = dados["nome"]
            categoria = dados["categoria"]
            local = dados["local"]
            organizador = dados["organizador"]
            email = dados["email"]
            self.ident, self.nome, self.categoria, self.local, self.organizador, self.email = ident, nome, categoria, local, organizador, email
            return self
        except Exception as e:
            print("Problema ao atualizar seu evento!")
            print(e)

    def __call__(self):
        d = dict()
        d["ident"] = self.ident
        d["nome"] = self.nome
        d["categoria"] = self.categoria
        d["local"] = self.local
        d["organizador"] = self.organizador
        d["email"] = self.email
        return d
        
    @staticmethod
    def criar(self):
        try:
            ident = self["ident"]
            nome = self["nome"]
            categoria = self["categoria"]
            local = self["local"]
            organizador = self["organizador"]
            email = self["email"]
            evento = Eventos(ident=ident, nome=nome, categoria=categoria, local=local, organizador=organizador, email=email)
            return evento
        except Exception as e:
            print("Problema ao criar seu evento!")
            print(e)