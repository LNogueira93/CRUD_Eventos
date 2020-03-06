class Eventos():

    def __init__(self, id_evento, nome_evento, descricao, data_criacao, data_atualizacao, local_evento, qntd_ingresso, preco_ingresso, ingresso_vendido, idade_minima):
        self.id_evento = id_evento
        self.nome_evento = nome_evento
        self.descricao = descricao
        self.data_criacao = data_criacao
        self.data_atualizacao = data_atualizacao
        self.local_evento = local_evento
        self.qntd_ingresso = qntd_ingresso
        self.preco_ingresso = preco_ingresso
        self.ingresso_vendido = ingresso_vendido
        self.idade_minima = idade_minima

    def atualizar(self, dados):
        try:
            id_evento = dados["id_evento"]
            nome_evento = dados["nome_evento"]
            descricao = dados["descricao"]
            data_criacao = dados["data_criacao"]
            data_atualizacao = dados["data_atualizacao"]
            local_evento = dados["local_evento"]
            qntd_ingresso = dados["qntd_ingresso"]
            preco_ingresso = dados["preco_ingresso"]
            ingresso_vendido = dados["ingresso_vendido"]
            idade_minima = dados["idade_minima"]
            self.id_evento, self.nome_evento, self.descricao, self.data_criacao, self.data_atualizacao, self.local_evento, self.qntd_ingresso, self.preco_ingresso, self.ingresso_vendido, self.idade_minima = id_evento, nome_evento, descricao, data_criacao, data_atualizacao, local_evento, qntd_ingresso, preco_ingresso, ingresso_vendido, idade_minima
            return self
        except Exception as e:
            print("Problema ao atualizar seu evento!")
            print(e)

    def __dict__(self):
        d = dict()
        d["id_evento"] = self.id_evento
        d["nome_evento"] = self.nome_evento
        d["descricao"] = self.descricao
        d["data_criacao"] = self.data_criacao
        d["data_atualizacao"] = self.data_atualizacao
        d["local_evento"] = self.local_evento
        d["qntd_ingresso"] = self.qntd_ingresso
        d["preco_ingresso"] = self.preco_ingresso
        d["ingresso_vendido"] = self.ingresso_vendido
        d["idade_minima"] = self.idade_minima
        return d
        
    @staticmethod
    def criar(self):
        try:
            id_evento = self["id_evento"]
            nome_evento = self["nome_evento"]
            descricao = self["descricao"]
            data_criacao = self["data_criacao"]
            data_atualizacao = self["data_atualizacao"]
            local_evento = self["local_evento"]
            qntd_ingresso = self["qntd_ingresso"]
            preco_ingresso = self["preco_ingresso"]
            ingresso_vendido = self["ingresso_vendido"]
            idade_minima = self["idade_minima"]
            return Eventos(id_evento=id_evento, nome_evento=nome_evento, descricao=descricao, data_criacao=data_criacao, data_atualizacao=data_atualizacao, local_evento=local_evento, qntd_ingresso=qntd_ingresso, preco_ingresso=preco_ingresso, ingresso_vendido=ingresso_vendido, idade_minima=idade_minima)
        except Exception as e:
            print("Problema ao criar seu evento!")
            print(e)