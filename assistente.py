import time
import sqlite3
import queue
import threading

#Definindo o formato que será mostrado na GUI
horario_atual = time.strftime("%H:%M:%S")
#Pegando a data local atual
tempo = time.localtime()
#Pegando o dia, mes e ano
dia_mes = tempo.tm_mday
dia_semana = tempo.tm_wday
mes = tempo.tm_mon
ano = tempo.tm_year
#Pegando a hora
hora = tempo.tm_hour

#Verifica que dia é
if dia_semana == 0:
#Pegando a data atual
    data_atual = time.strftime("Seg %d/%m/%Y")
elif dia_semana == 1:
    data_atual = time.strftime("Ter %d/%m/%Y")
elif dia_semana == 2:
    data_atual = time.strftime("Quar %d/%m/%Y")
elif dia_semana == 3:
    data_atual = time.strftime("Quin %d/%m/%Y")
elif dia_semana == 4:
    data_atual = time.strftime("Sex %d/%m/%Y")
elif dia_semana == 5:
    data_atual = time.strftime("Sáb %d/%m/%Y")
else:
    data_atual = time.strftime("Dom %d/%m/%Y")

def saber_hora():    
    hora_atual = tempo.tm_hour
    time.sleep(1)
    return hora_atual
        
def banco_user():
    banco = sqlite3.connect("banco/banco.db")
    cursor = banco.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS usuario
                   (nome TEXT NOT NULL, idade INTEGER NOT NULL, mnome TEXT NOT NULL, dia_niver INTEGER NOT NULL, mes_niver INTEGER NOT NULL, cores TEXT NULL, estado_da_voz TEXT NULL, hora_atual INTEGER NOT NULL, dia_atual INTEGER NOT NULL, dia_anterior INTEGER NOT NULL, mes_atual INTEGER NOT NULL, ano_atual INTEGER NOT NULL, dia TEXT NULL, tarde TEXT NULL, noite TEXT NULL)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS notas 
                   (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, titulo TEXT NULL, texto TEXT NULL, data_criacao TEXT NULL, data_edita TEXT NULL, fonte INTEGER NOT NULL, materia TEXT NOT NULL)""")
    banco.commit()
    banco.close()
    
def inserir_dados(nome, idade, mnome, dividir):
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    dia_niver = int(dividir[0])
    mes_niver = int(dividir[1])
    cursor.execute("""INSERT INTO usuario (nome, idade, mnome, dia_niver, mes_niver, hora_atual, dia_atual, mes_atual, ano_atual, cores, dia_anterior)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (nome, idade, mnome, dia_niver, mes_niver, hora, dia_mes, mes, ano, "#EEEBEB", dia_mes))
    conexao.commit()
    conexao.close()

def nome():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    pega_nome = cursor.execute("SELECT nome FROM usuario")
    for pn in pega_nome:
        pega_nome = pn
    return pega_nome[0]

def atualiza_hora():
    hora_certa = saber_hora()
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    verificahora = cursor.execute("SELECT hora_atual FROM usuario")
    for vha in verificahora:
        verificahora = vha
    if hora_certa != verificahora[0]:
        cursor.execute("UPDATE usuario SET hora_atual = ?", (hora_certa,))
        conexao.commit()
        conexao.close()

def hora_da_fala_dia(hora_falou):
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    verificadia = cursor.execute("SELECT dia FROM usuario")
    for vfd in verificadia:
        verificadia = vfd
    if verificadia[0] == None:
        cursor.execute("UPDATE usuario SET dia = ?", (hora_falou,))
        conexao.commit()
        conexao.close()

def verifica_fala_dia():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    verificadia = cursor.execute("SELECT dia FROM usuario")
    for vfd in verificadia:
        verificadia = vfd
    if verificadia[0] == None:
        conexao.close()
        return False
    else:
        conexao.close()
        return True

def hora_da_fala_tarde(hora_falou):
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    verificatarde = cursor.execute("SELECT tarde FROM usuario")
    for vft in verificatarde:
        verificatarde = vft
    if verificatarde[0] == None:
        cursor.execute("UPDATE usuario SET tarde = ?", (hora_falou,))
        conexao.commit()
        conexao.close()

def verifica_fala_tarde():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    verificatarde = cursor.execute("SELECT tarde FROM usuario")
    for vtd in verificatarde:
        verificatarde = vtd
    if verificatarde[0] == None:
        conexao.close()
        return False
    else:
        conexao.close()
        return True
    
def hora_da_fala_noite(hora_falou):
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    verificanoite = cursor.execute("SELECT noite FROM usuario")
    for vfn in verificanoite:
        verificanoite = vfn
    if verificanoite[0] == None:
        cursor.execute("UPDATE usuario SET noite = ?", (hora_falou,))
        conexao.commit()
        conexao.close()

def verifica_fala_noite():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    verificanoite = cursor.execute("SELECT noite FROM usuario")
    for vfn in verificanoite:
        verificanoite = vfn
    if verificanoite[0] == None:
        conexao.close()
        return False
    else:
        conexao.close()
        return True

def atualiza_dia():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    verificadia = cursor.execute("SELECT dia_atual FROM usuario")
    for vda in verificadia:
        verificadia = vda
    if dia_mes != verificadia[0]:
        cursor.execute("UPDATE usuario SET dia_atual = ?", (dia_mes,))
        conexao.commit()
        conexao.close()

def verificar_dados():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    verifican = cursor.execute("SELECT nome FROM usuario")
    resuln = verifican.fetchone() is None
    verificai = cursor.execute("SELECT idade FROM usuario")
    resuli = verificai.fetchone() is None
    verificamn = cursor.execute("SELECT mnome FROM usuario")
    resulmn = verificamn.fetchone() is None
    verificad_n = cursor.execute("SELECT dia_niver FROM usuario")
    resuld_n = verificad_n.fetchone() is None
    verificam_n = cursor.execute("SELECT mes_niver FROM usuario")
    resulm_n = verificam_n.fetchone() is None
    if resuln and resuli and resulmn and resuld_n and resulm_n == True:
        conexao.close()
        return True
    else:
        conexao.close()
        return False

def reiniciar_ciclo_saudacao():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    verificadal = cursor.execute("SELECT dia_atual FROM usuario")
    for da in verificadal:
        verificadal = da
    verificadan = cursor.execute("SELECT dia_anterior FROM usuario")
    for dan in verificadan:
        verificadan = dan
    if verificadan[0] != verificadal[0]:
        cursor.execute("UPDATE usuario SET dia = ?", (None,))
        conexao.commit()
        cursor.execute("UPDATE usuario SET tarde = ?", (None,))
        cursor.execute("UPDATE usuario SET noite = ?", (None,))
        cursor.execute("UPDATE usuario SET dia_anterior = ?", (dia_mes,))
        conexao.commit()
        conexao.close()

def guarda_titulo_nota(titulo, nota, fonte, data_c, materia):
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    cursor.execute("""INSERT INTO notas (titulo, texto, fonte, data_criacao, materia) VALUES(?, ?, ?, ?, ?)""", (titulo, nota, fonte, data_c, materia))
    conexao.commit()
    conexao.close()

def deletar_nota(id):
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE from notas WHERE ID = ?", (id,))
    conexao.commit()
    verificadel = cursor.execute("SELECT EXISTS(SELECT 1 FROM notas WHERE ID = ?)", (id,))
    for d in verificadel:
        verificadel = d
    if verificadel[0] == 0:
        conexao.close()
        return True
    else:
        conexao.close()
        return False
    
def salvar_edicao(data_e, id, titulo_e, texto_e, tipo_n, fonte):
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE notas SET titulo = ?, texto = ?, data_edita = ?, fonte = ?, materia = ? WHERE ID = ?", (titulo_e, texto_e, data_e, fonte, tipo_n, id))
    conexao.commit()
    atualizou = cursor.rowcount
    if atualizou > 0:
        conexao.close()
        return True
    else:
        conexao.close()
        return False

def verifica_guarda_titulo():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    verificati = cursor.execute("SELECT titulo FROM notas")
    resulti = verificati.fetchone() is None
    verificatxt = cursor.execute("SELECT texto FROM notas")
    resultxt = verificatxt.fetchone() is None
    verifacadc = cursor.execute("SELECT data_criacao FROM notas")
    resuldc = verifacadc.fetchone() is None
    if resulti and resultxt and resuldc == True:
        conexao.close()
        return True
    else:
        conexao.close()
        return False

def pega_notas():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    todas_notas = cursor.execute("SELECT ID, titulo, texto, materia, fonte FROM notas ORDER BY ID")
    return todas_notas

def pega_cor():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    cores = cursor.execute("SELECT cores FROM usuario") 
    for c in cores:
        cores = c
    if cores[0] == "#EEEBEB":
        conexao.close()
        cor_atual = "#EEEBEB"
        return cor_atual
    else:
        conexao.close()
        return cores[0]

def cor_texto():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    cores = cursor.execute("SELECT cores FROM usuario")
    for c in cores:
        cores = c
        if cores[0] == "#101A12" or cores[0] == "#000127" or cores[0] == "#1093D4" or cores[0] == "#008000":
            conexao.close()
            return "white"
        elif cores[0] == "#FFB0E0":
            conexao.close()
            return "#F4EFEF"
        else:
            conexao.close()
            return "black"

def cor_texto_botao():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    cores = cursor.execute("SELECT cores FROM usuario")
    for c in cores:
        cores = c
    if cores[0] == "#F32A2A":
        conexao.close()
        return "#FAF7F7"
    
def cor_texto_tooltip():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    cores = cursor.execute("SELECT cores FROM usuario")
    for c in cores:
        cores = c
    if cores[0] == "#101A12" or cores[0] == "#000127" or cores[0] == "#1093D4":
        conexao.close()
        return "white"
    else:
        conexao.close()
        return "black"

def cor_labels():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    cores = cursor.execute("SELECT cores FROM usuario")
    for c in cores:
        cores = c
        if cores[0] == "#101A12":
            conexao.close()
            return "#5E127F"
        elif cores[0] == "#FFDE21":
            conexao.close()
            return "#FF5C00"
        elif cores[0] == "#008000":
            conexao.close()
            return "#FC6C85"
        elif cores[0] == "#FFB0E0":
            conexao.close()
            return "#1093D4"
        elif cores[0] == "#895129":
            conexao.close()
            return "#E08543"
        elif cores[0] == "#F32A2A":
            conexao.close()
            return "#FFBFBF"
        else:
            conexao.close()
            return "#105ba0"
        
def cor_hover():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    cores = cursor.execute("SELECT cores FROM usuario")
    for c in cores:
        cores = c
        if cores[0] == "#101A12":
            conexao.close()
            return "#541070"
        elif cores[0] == "#000127":
            conexao.close()
            return "#0c4478"
        elif cores[0] == "#1093D4":
            conexao.close()
            return "#0c4478"
        elif cores[0] == "#FFDE21":
            conexao.close()
            return "#EB5A05"
        elif cores[0] == "#008000":
            conexao.close()
            return "#F26A81"
        elif cores[0] == "#F32A2A":
            conexao.close()
            return "#F1B7B7"
        elif cores[0] == "#895129":
            conexao.close()
            return "#D27D40"
        else:
            conexao.close()
            return "#0c4478"

def cor_fundo():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    cores = cursor.execute("SELECT cores FROM usuario")
    for c in cores:
        cores = c
        if cores[0] == "#101A12":
            conexao.close()
            return "#101A12"
        elif cores[0] == "#000127":
            conexao.close()
            return "#000127"
        else:
            conexao.close()
            return "white"
        
def cor_notas():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    cores = cursor.execute("SELECT cores FROM usuario")
    for c in cores:
        cores = c
    if cores[0] == "#EEEBEB":
        conexao.close()
        return "#E0D8D8"
    elif cores[0] == "#101A12" or cores[0] == "#000127":
        conexao.close()
        return "#504949"
    elif cores[0] == "#F32A2A":
        conexao.close()
        return "#C5BCBC"
    elif cores[0] == "#F7F7F7":
        conexao.close()
        return "#E8DFDF"
    elif cores[0] == "#1093D4":
        conexao.close()
        return "#CFCDCD"
    elif cores[0] == "#FFDE21":
        conexao.close()
        return "#C7C0C0"
    elif cores[0] == "#008000":
        conexao.close()
        return "#A6A3A3"
    elif cores[0] == "#FFB0E0":
        conexao.close()
        return "#877E7E"

def cor_borda_place():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    cores = cursor.execute("SELECT cores FROM usuario")
    for c in cores:
        cores = c
    if cores[0] == "#101A12":
        conexao.close()
        return "#5E127F"
    elif cores[0] == "#F7F7F7" or cores[0] == "#EEEBEB":
        conexao.close()
        return "#105ba0"
    elif cores[0] == "#FFB0E0":
        conexao.close()
        return "#FFB0E0"
    elif cores[0] == "#F32A2A":
        conexao.close()
        return "#F32A2A"
    elif cores[0] == "#FFDE21":
        conexao.close()
        return "#FF5C00"
    elif cores[0] == "#008000":
        conexao.close()
        return "#FC6C85"
    elif cores[0] == "#895129":
        conexao.close()
        return "#895129"
    elif cores[0] == "#1093D4":
        conexao.close()
        return "#1093D4"
    elif cores[0] == "#000127":
        conexao.close()
        return "#105ba0"
    else:
        conexao.close()
        return cores[0]

def imagem_cor():
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    cores = cursor.execute("SELECT cores FROM usuario")
    for c in cores:
        cores = c
        if cores[0] == "#FFB0E0":
            conexao.close()
            return "imagens/alerta_rosa.png"
        elif cores[0] == "#101A12":
            conexao.close()
            return "imagens/alerta_preto.png"
        elif cores[0] == "#F32A2A":
            conexao.close()
            return "imagens/alerta_vermelho.png"
        elif cores[0] == "#FFDE21":
            conexao.close()
            return "imagens/alerta_amarelo.png"
        elif cores[0] == "#008000":
            conexao.close()
            return "imagens/alerta_verde.png"
        elif cores[0] == "#895129":
            conexao.close()
            return "imagens/alerta_marrom.png"
        elif cores[0] == "#1093D4":
            conexao.close()
            return "imagens/alerta_azul.png"
        elif cores[0] == "#EEEBEB":
            conexao.close()
            return "imagens/alerta_azullogus.png"
        elif cores[0] == "#000127":
            conexao.close()
            return "imagens/alerta_azulmn.png"
        elif cores[0] == "#F7F7F7":
            conexao.close()
            return "imagens/alerta_branco.png"
        else:
            conexao.close()
            return "imagens/alerta_padrao.png"

def atualiza_cor(cor):
    conexao = sqlite3.connect("banco/banco.db")
    cursor = conexao.cursor()
    cursor.execute("""UPDATE usuario SET cores = ?""", (cor,))
    conexao.commit()
    conexao.close()