def soma(a,b):
    return a + b


def eh_par(n):
    if n % 2 == 0:
        return True
    else:
        return False


def fatorial(n):
    multiplicador = n - 1
    resposta = n
    
    if n == 0:
        resposta = 1
    
    else:
        while multiplicador >= 1:
            resposta = resposta * multiplicador
            multiplicador -= 1

    return resposta


userData = []
def cadastrar(nome, email):
    for usuario in userData:
        if usuario["email"] == email:
            return "email já cadastrado"


    usuario = {
        "nome":nome,
        "email":email
    }

    userData.append(usuario)
    return "sucesso"



#def cadastrar(nome, email):
#    userData = []
#
#    usuario = {
#        "nome":nome,
#        "email":email
#    }
#
#    if usuario["email"] not in userData:
#
#        userData.append(usuario)
#        return "sucesso"
#
#    else:
#        return "email já cadastrado"



# controller
def cadastro(nome, cpf):
    new_user = {
        "nome": nome,
        "cpf": cpf
    }
    return save(new_user)

# service
def save(new_user):
    if new_user["nome"] and new_user["cpf"]:
        return True #salvo no DB
    return False #erro ao salvar no DB



# controller
def envia_email(remetente, destinatario):
    novo_email = {
        "remetente": remetente,
        "destinatario": destinatario
    }
    return servico_email(novo_email)

# service
def servico_email(novo_email):
    conteudo = 'Olá, este é um email de boas vindas.'
    if novo_email["remetente"] and novo_email["destinatario"]:
        return conteudo



# controller
def welcome(email):
    if email:
        resposta = send_mail(email)
        if resposta:
            return 'email de boas vindas enviado'
        return 'erro de provedor'


def send_mail(email):
    return True



# controller
def envia_sms(telefone):
    novo_sms = {
        "telefone": telefone
    }
    return servico_sms(novo_sms)

# service
def servico_sms(novo_sms):
    conteudo = 'mensagem de boas vindas'
    if novo_sms["telefone"]:
        return conteudo
