from app import db


class usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(16))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


class entidade(db.Model):
    __tablename__ = "entidade"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cnpj = db.Column(db.Integer)
    estado = db.Column(db.Boolean)
    telefone = db.Column(db.Integer)
    tipo_entidade = db.Column(db.Integer)
    id_endereco = db.Column(db.Integer)
    id_usuario = db.Column(db.Integer)
    razao_social = db.Column(db.String(50))

    def __init__(self, id, cnpj, estado, telefone, tipo_entidade, id_endereco, id_usuario, razao_social):
        self.id = id
        self.cnpj = cnpj
        self.estado = estado
        self.telefone = telefone
        self.tipo_entidade = tipo_entidade
        self.id_endereco = id_endereco
        self.id_usuario = id_usuario
        self.razao_social = razao_social


class endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rua = db.Column(db.String(35))
    bairro = db.Column(db.String(30))
    cidade = db.Column(db.String(30))
    estado = db.Column(db.String(35))
    numero = db.Column(db.Integer)
    cep = db.Column(db.Integer)

    def __init__(self, id, rua, bairro, cidade, estado, numero, cep):
        self.id = id
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.numero = numero
        self.cep = cep


class assinatura(db.Model):
    __tablename__ = "assinatura"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_entidade = db.Column(db.Integer)
    id_pacote_informacao = db.Column(db.Integer)
    data_compra = db.Column(db.String(10))
    validade = db.Column(db.String(10))
    preco_compra = db.Column(db.Float)

    def __init__(self, id_entidade, id, id_pacote_informacao, data_compra, validade, preco_compra):
        self.id = id
        self.id_entidade = id_entidade
        self.id_pacote_informacao = id_pacote_informacao
        self.data_compra = data_compra
        self.validade = validade
        self.preco_compra = preco_compra


class pacote_informacao(db.Model):
    __tablename__ = "pacote_informacao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_pacote = db.Column(db.String(30))
    tipo_entidade = db.Column(db.Integer)
    ano_pacote = db.Column(db.String(10))
    duracao = db.Column(db.String(10))
    descricao = db.Column(db.String(50))
    valor = db.Column(db.Float)

    def __init__(self, id, nome_pacote, tipo_entidade, ano_pacote, duracao, descricao, valor):
        self.id = id
        self.nome_pacote = nome_pacote
        self.tipo_entidade = tipo_entidade
        self.ano_pacote = ano_pacote
        self.duracao = duracao
        self.descricao = descricao
        self.valor = valor


class sugestao(db.Model):
    __tablename__ = "sugestao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_entidade = db.Column(db.Integer)
    mensagem = db.Column(db.String(150))
    data = db.Column(db.String(10))

    def __init__(self, id, id_entidade, mensagem, data):
        self.id = id
        self.id_entidade = id_entidade
        self.mensagem = mensagem
        self.data = data


class acidente(db.Model):
    __tablename__ = "acidente"

    cod = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_endereco = db.Column(db.Integer)
    cod_envolvido = db.Column(db.Integer)
    # talvez precisemos ajustar a classe atual de endereco
    # adicionando os campos latitude e longitude
    tipo = db.Column(db.String(50))
    situacao = db.Column(db.String(50))
    data = db.Column(db.String(10))
    hora = db.Column(db.String(10))
    natureza = db.Column(db.String(50))
    descricao = db.Column(db.String(100))
    qtd_vitmas = db.Column(db.Integer)
    qtd_vitmas_fatais = db.Column(db.Integer)

    def __init__(self, cod, cod_envolvido, id_endereco, tipo, situacao, data, hora, natureza, descricao, qtd_vitmas,
                 qtd_vitmas_fatais):
        self.cod = cod
        self.cod_envolvido = cod_envolvido
        self.id_endereco = id_endereco
        self.tipo = tipo
        self.situacao = situacao
        self.data = data
        self.hora = hora
        self.natureza = natureza
        self.qtd_vitmas = qtd_vitmas
        self.qtd_vitmas_fatais = qtd_vitmas_fatais


class envolvido(db.Model):
    __tablename__ = "envolvido"

    cod = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qtd_auto = db.Column(db.Integer)
    qtd_moto = db.Column(db.Integer)
    qtd_ciclom = db.Column(db.Integer)
    qtd_ciclista = db.Column(db.Integer)
    qtd_pedestre = db.Column(db.Integer)
    qtd_onibus = db.Column(db.Integer)
    qtd_caminhao = db.Column(db.Integer)
    qtd_viatura = db.Column(db.Integer)
    qtd_outros = db.Column(db.Integer)

    def __init__(self, cod, qtd_auto, qtd_moto, qtd_ciclom, qtd_ciclista, qtd_pedestre, qtd_onibus, qtd_caminhao,
                 qtd_viatura, qtd_outros):
        self.cod = cod
        self.qtd_auto = qtd_auto
        self.qtd_moto = qtd_moto
        self.qtd_ciclom = qtd_ciclom
        self.qtd_ciclista = qtd_ciclista
        self.qtd_pedestre = qtd_pedestre
        self.qtd_onibus = qtd_onibus
        self.qtd_caminhao = qtd_caminhao
        self.qtd_viatura = qtd_viatura
        self.qtd_outros = qtd_outros


class camera_transito(db.Model):
    __tablename__ = "camera_transito"

    cod = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_endereco = db.Column(db.Integer)
    nome = db.Column(db.String(10))

    def __init__(self, cod, id_endereco, nome):
        self.cod = cod
        self.id_endereco = id_endereco
        self.nome = nome


class infracao(db.Model):
    __tablename__ = "infracao"

    cod_infracao = db.Column(db.Integer, primary_key=True)
    amaparo_legal = db.Column(db.String(50))
    descricao_infracao = db.Column(db.String(300))

    def __init__(self, cod_infracao, amaparo_legal, descricao_infracao):
        self.cod_infracao = cod_infracao
        self.amaparo_legal = amaparo_legal
        self.descricao_infracao = descricao_infracao


class registro_infracao(db.Model):
    __tablename__ = "registro_infracao"

    cod = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_endereco = db.Column(db.Integer)
    cod_infracao = db.Column(db.Integer)
    agente_equipamento = db.Column(db.String(50))
    hora_infracao = db.Column(db.String(10))
    data_infracao = db.Column(db.String(10))
    data_implantacao = db.Column(db.String(10))

    def __init__(self, cod, id_endereco, cod_infracao, agente_equipamento, hora_infracao, data_infracao,
                 data_implantacao):
        self.cod = cod
        self.id_endereco = id_endereco
        self.cod_infracao = cod_infracao
        self.agente_equipamento = agente_equipamento
        self.hora_infracao = hora_infracao
        self.data_infracao = data_infracao
        self.data_implantacao = data_implantacao


class semaforo(db.Model):
    __tablename__ = "semaforo"

    cod_semaforo = db.Column(db.Integer, primary_key=True)
    id_endereco = db.Column(db.Integer)
    funcionamento = db.Column(db.String(10))
    utilizacao = db.Column(db.String(20))
    sinalsonoro = db.Column(db.String(1))
    sinalizadorciclista = db.Column(db.String(1))

    def __init__(self, cod_semaforo, id_endereco, funcionamento, utilizacao, sinalsonoro, sinalizadorciclista):
        self.cod_semaforo = cod_semaforo
        self.id_endereco = id_endereco
        self.funcionamento = funcionamento
        self.utilizacao = utilizacao
        self.sinalsonoro = sinalsonoro
        self.sinalizadorciclista = sinalizadorciclista


class coordenadas(db.Model):
    __tablename__ = "coordenadas"

    cod = db.Column(db.Integer, primary_key=True, autoincrement=True)
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)

    def __init__(self, cod, latitude, longitude):
        self.cod = cod
        self.latitude = latitude
        self.longitude = longitude


# Obs: nao sei que valores serao setados em: equipamento e fluxo_veiculo
class equipamento_fiscalizacao(db.Model):
    __tablename__ = "equipamento_fiscalizacao"

    cod_equipamento = db.Column(db.Integer, primary_key=True)
    id_endereco = db.Column(db.Integer)
    velociade = db.Column(db.Integer)
    equipamento = ''
    fluxo_veiculo = ''

    def __init__(self, cod_equipamento, id_endereco, velociade, equipamento, fluxo_veiculo):
        self.cod_equipamento = cod_equipamento
        self.id_endereco = id_endereco
        self.velociade = velociade
        self.equipamento = equipamento
        self.fluxo_veiculo = fluxo_veiculo
