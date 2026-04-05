import time
import sqlite3
import os
import sys
import shutil
import pyttsx3

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

def verifica_pasta(caminho):
    if hasattr(sys, "_MEIPASS"):    
        pasta_imagens = sys._MEIPASS
    else:
        pasta_imagens = os.path.dirname(sys.executable)
    return os.path.join(pasta_imagens, caminho)

dados = os.path.join(os.getenv("HOME"), ".local", "share")
pasta = os.path.join(dados, "Sponte Study")
os.makedirs(pasta, exist_ok=True)
pasta_db = os.path.join(pasta, "banco.db")

#Abri pasta de imagem
imagem_pasta = os.path.join(pasta, "imagens")
os.makedirs(imagem_pasta, exist_ok=True)

#Copiar arquivos para a pasta de imagens
if not os.listdir(imagem_pasta):
    shutil.copy(verifica_pasta("imagens_app/alerta_padrao.png"), imagem_pasta)
    shutil.copy(verifica_pasta("imagens_app/alerta_azul.png"), imagem_pasta)
    shutil.copy(verifica_pasta("imagens_app/alerta_vermelho.png"), imagem_pasta)
    shutil.copy(verifica_pasta("imagens_app/alerta_verde.png"), imagem_pasta)
    shutil.copy(verifica_pasta("imagens_app/alerta_amarelo.png"), imagem_pasta)
    shutil.copy(verifica_pasta("imagens_app/alerta_rosa.png"), imagem_pasta)
    shutil.copy(verifica_pasta("imagens_app/alerta_preto.png"), imagem_pasta)
    shutil.copy(verifica_pasta("imagens_app/alerta_branco.png"), imagem_pasta)
    shutil.copy(verifica_pasta("imagens_app/alerta_azulmn.png"), imagem_pasta)
    shutil.copy(verifica_pasta("imagens_app/alerta_marrom.png"), imagem_pasta)
    shutil.copy(verifica_pasta("imagens_app/alerta_azullogus.png"), imagem_pasta)
    shutil.copy(verifica_pasta("imagens_app/leitura_preto.png"), imagem_pasta)
    shutil.copy(verifica_pasta("imagens_app/leitura_branco.png"), imagem_pasta)
    shutil.copy(verifica_pasta("imagens_app/logo.ico"), imagem_pasta)
    shutil.copy(verifica_pasta("imagens_app/Sponte.png"), imagem_pasta)

arquivos_leitura = ["leitura_preto.png", "leitura_branco.png"]

def reinicia_pasta(pasta, arquivos_verifica):
    arquivos = os.listdir(pasta)

    for arq in arquivos_verifica:
        if not arq in arquivos:
            shutil.copy("imagens_app/leitura_preto.png", imagem_pasta)
            shutil.copy("imagens_app/leitura_branco.png", imagem_pasta)

reinicia_pasta(imagem_pasta, arquivos_leitura)

#Caminho de arquivos
alerta_padrao = os.path.join(imagem_pasta, "alerta_padrao.png")
alerta_azul = os.path.join(imagem_pasta, "alerta_azul.png")
alerta_vermelho = os.path.join(imagem_pasta, "alerta_vermelho.png")
alerta_verde = os.path.join(imagem_pasta, "alerta_verde.png")
alerta_amarelo = os.path.join(imagem_pasta, "alerta_amarelo.png")
alerta_rosa = os.path.join(imagem_pasta, "alerta_rosa.png")
alerta_preto = os.path.join(imagem_pasta, "alerta_preto.png")
alerta_branco = os.path.join(imagem_pasta, "alerta_branco.png")
alerta_azulmn = os.path.join(imagem_pasta, "alerta_azulmn.png")
alerta_marrom = os.path.join(imagem_pasta, "alerta_marrom.png")
alerta_azullogus = os.path.join(imagem_pasta, "alerta_azullogus.png")
leitura_preto = os.path.join(imagem_pasta, "leitura_preto.png")
leitura_branco = os.path.join(imagem_pasta, "leitura_branco.png")

def saber_hora():    
    hora_atual = tempo.tm_hour
    time.sleep(1)
    return hora_atual
        
def banco_user():
    banco = sqlite3.connect(pasta_db)
    cursor = banco.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS usuario
                   (nome TEXT NOT NULL, idade INTEGER NOT NULL, mnome TEXT NOT NULL, dia_niver INTEGER NOT NULL, mes_niver INTEGER NOT NULL, cores TEXT NULL, estado_da_voz TEXT NULL, hora_atual INTEGER NOT NULL, dia_atual INTEGER NOT NULL, dia_anterior INTEGER NOT NULL, mes_atual INTEGER NOT NULL, ano_atual INTEGER NOT NULL, dia TEXT NULL, tarde TEXT NULL, noite TEXT NULL)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS notas 
                   (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, titulo TEXT NULL, texto TEXT NULL, data_criacao TEXT NULL, data_edita TEXT NULL, fonte INTEGER NOT NULL, materia TEXT NOT NULL, codigo TEXT, tema TEXT, fonte_codigo INTEGER, linguagem TEXT)""")
    banco.commit()
    banco.close()

def adiciona_colunas_codigo():
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    verifica_existencia_coluna = cursor.execute("PRAGMA table_info(notas)")
    colunas = []
    for vec in verifica_existencia_coluna:
        colunas.append(vec[1])
    if "codigo" not in colunas:
       cursor.execute("ALTER TABLE notas ADD COLUMN codigo TEXT")
    if "tema" not in colunas:
        cursor.execute("ALTER TABLE notas ADD COLUMN tema TEXT")
    if "fonte_codigo" not in colunas:
        cursor.execute("ALTER TABLE notas ADD COLUMN fonte_codigo INTEGER")
    if "linguagem" not in colunas:
        cursor.execute("ALTER TABLE notas ADD COLUMN linguagem TEXT")
    conexao.commit()
    conexao.close()
    
def inserir_dados(nome, idade, mnome, dividir):
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    dia_niver = int(dividir[0])
    mes_niver = int(dividir[1])
    cursor.execute("""INSERT INTO usuario (nome, idade, mnome, dia_niver, mes_niver, hora_atual, dia_atual, mes_atual, ano_atual, cores, dia_anterior, estado_da_voz)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (nome, idade, mnome, dia_niver, mes_niver, hora, dia_mes, mes, ano, "#EEEBEB", dia_mes, "Ativa"))
    conexao.commit()
    conexao.close()

def nome():
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    pega_nome = cursor.execute("SELECT nome FROM usuario")
    for pn in pega_nome:
        pega_nome = pn
    return pega_nome[0]

def atualiza_hora():
    hora_certa = saber_hora()
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    verificahora = cursor.execute("SELECT hora_atual FROM usuario")
    for vha in verificahora:
        verificahora = vha
    if hora_certa != verificahora[0]:
        cursor.execute("UPDATE usuario SET hora_atual = ?", (hora_certa,))
        conexao.commit()
        conexao.close()

def hora_da_fala_dia(hora_falou):
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    verificadia = cursor.execute("SELECT dia FROM usuario")
    for vfd in verificadia:
        verificadia = vfd
    if verificadia[0] == None:
        cursor.execute("UPDATE usuario SET dia = ?", (hora_falou,))
        conexao.commit()
        conexao.close()

def verifica_fala_dia():
    conexao = sqlite3.connect(pasta_db)
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
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    verificatarde = cursor.execute("SELECT tarde FROM usuario")
    for vft in verificatarde:
        verificatarde = vft
    if verificatarde[0] == None:
        cursor.execute("UPDATE usuario SET tarde = ?", (hora_falou,))
        conexao.commit()
        conexao.close()

def verifica_fala_tarde():
    conexao = sqlite3.connect(pasta_db)
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
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    verificanoite = cursor.execute("SELECT noite FROM usuario")
    for vfn in verificanoite:
        verificanoite = vfn
    if verificanoite[0] == None:
        cursor.execute("UPDATE usuario SET noite = ?", (hora_falou,))
        conexao.commit()
        conexao.close()

def verifica_fala_noite():
    conexao = sqlite3.connect(pasta_db)
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
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    verificadia = cursor.execute("SELECT dia_atual FROM usuario")
    for vda in verificadia:
        verificadia = vda
    if dia_mes != verificadia[0]:
        cursor.execute("UPDATE usuario SET dia_atual = ?", (dia_mes,))
        conexao.commit()
        conexao.close()

def verifica_fala_config():
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    voz = cursor.execute("SELECT voz_falou_config FROM usuario")
    for v in voz:
        voz = v
    if voz[0] == None:
        conexao.close()
        return True
    else:
        conexao.close()
        return False
    
def ja_falou_config(res):
    if res == True:
        conexao = sqlite3.connect(pasta_db)
        cursor = conexao.cursor()
        cursor.execute("UPDATE usuario SET voz_falou_config = ?", (res,))
        conexao.commit()
        conexao.close()

def atualiza_estado_voz(voz):
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    estado_atual = cursor.execute("SELECT estado_da_voz FROM usuario")
    for ea in estado_atual:
        estado_atual = ea
    if voz != estado_atual[0]:
        cursor.execute("UPDATE usuario SET estado_da_voz = ?", (voz,))
        conexao.commit()
        conexao.close()

def verificar_dados():
    conexao = sqlite3.connect(pasta_db)
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
    conexao = sqlite3.connect(pasta_db)
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
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    cursor.execute("""INSERT INTO notas (titulo, texto, fonte, data_criacao, materia) VALUES(?, ?, ?, ?, ?)""", (titulo, nota, fonte, data_c, materia))
    conexao.commit()
    conexao.close()

def guarda_codigos(titulo, descricao, fonte_descricao, data_criacao, codigo, fonte_codigo, tema, lang):
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    cursor.execute("""INSERT INTO notas (titulo, texto, fonte, data_criacao, codigo, fonte_codigo, tema, linguagem, materia) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""", (titulo, descricao, fonte_descricao, data_criacao, codigo, fonte_codigo, tema, lang, "codigo"))
    conexao.commit()
    conexao.close()

def deletar_nota(id):
    conexao = sqlite3.connect(pasta_db)
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
    conexao = sqlite3.connect(pasta_db)
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
    
def salvar_edicao_codigo(titulo_e, id, descricao_e, fonte_descricao_e, data_edita_codigo, codigo_e, fonte_codigo_e, tema_e, linguagem_e):
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    cursor.execute("UPDATE notas SET titulo = ?, texto = ?, data_edita = ?, fonte = ?, codigo = ?, fonte_codigo = ?, tema = ?, linguagem = ? WHERE ID = ?", (titulo_e, descricao_e, data_edita_codigo, fonte_descricao_e, codigo_e, fonte_codigo_e, tema_e, linguagem_e, id))
    conexao.commit()
    atualizou_codigo = cursor.rowcount
    if atualizou_codigo > 0:
        conexao.close()
        return True
    else:
        conexao.close()
        return False

def verifica_guarda_titulo():
    conexao = sqlite3.connect(pasta_db)
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
    
def verifica_guarda_codigo():
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    verificati = cursor.execute("SELECT titulo FROM notas")
    resulti = verificati.fetchone() is None
    verificatxt = cursor.execute("SELECT texto FROM notas")
    resultxt = verificatxt.fetchone() is None
    verifacadc = cursor.execute("SELECT data_criacao FROM notas")
    resuldc = verifacadc.fetchone() is None
    verificacodi = cursor.execute("SELECT codigo FROM notas")
    resulcodi = verificacodi.fetchone() is None
    verificatem = cursor.execute("SELECT tema FROM notas")
    resultem = verificatem.fetchone() is None
    verificafonte_c = cursor.execute("SELECT fonte_codigo FROM notas")
    resulfonte_c = verificafonte_c.fetchone() is None
    verificalang = cursor.execute("SELECT linguagem FROM notas")
    resullang = verificalang.fetchone() is None
    if resulti and resultxt and resuldc and resulcodi and resultem and resulfonte_c and resullang == True:
        conexao.close()
        return True
    else:
        conexao.close()
        return False

def pegar_estado_voz():
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    estado_atual = cursor.execute("SELECT estado_da_voz FROM usuario")
    for ea in estado_atual:
        estado_atual = ea
    if estado_atual[0] == "Ativa":
        conexao.close()
        return "Ativa"
    else:
        conexao.close()
        return "Desativada"

def pega_notas():
    try:
        conexao = sqlite3.connect(pasta_db)
        cursor = conexao.cursor()
        cursor.execute("SELECT ID, titulo, texto, materia, fonte FROM notas WHERE materia != ? ORDER BY ID", ("codigo",))
        return cursor.fetchall()    
    finally:
        conexao.close()

def pega_codigos():
    try:
        conexao = sqlite3.connect(pasta_db)
        cursor = conexao.cursor()
        cursor.execute("SELECT ID, titulo, texto, fonte, codigo, tema, linguagem, fonte_codigo FROM notas WHERE materia == ? ORDER BY ID", ("codigo",))
        return cursor.fetchall()
    finally:
        conexao.close()

def busca_titulo(titulo, aba):
    try:
        conexao = sqlite3.connect(pasta_db)
        cursor = conexao.cursor()
        texto_existe = cursor.execute("SELECT titulo FROM notas WHERE titulo = ?", (titulo,))
        result = texto_existe.fetchone() is None
        if result == True:
            texto_existe = list(texto_existe)
            texto_existe.clear()
            return True
        else:
            texto_existe = list(texto_existe)
            texto_existe.clear()
            notas_certas = cursor.execute("SELECT ID, titulo, texto, materia, fonte FROM notas WHERE titulo = ?", (titulo,))
            for nc in notas_certas:
                notas_certas = nc
            if notas_certas[3] == "codigo" and aba == "notas":
                notas_certas = list(notas_certas)
                notas_certas.clear()
                return True
            elif notas_certas[3] and aba != "codigo":
                notas_certas = list(notas_certas)
                notas_certas.clear()
                cursor.execute("SELECT ID, titulo, texto, materia, fonte FROM notas WHERE titulo = ?", (titulo,))
                return cursor.fetchall()
            elif notas_certas[3] == "codigo" and aba == "codigo":
                notas_certas = list(notas_certas)
                notas_certas.clear()
                cursor.execute("SELECT ID, titulo, texto, fonte, codigo, tema, linguagem, fonte_codigo FROM notas WHERE titulo = ?", (titulo,))
                return cursor.fetchall()
    finally:
        conexao.close()

def busca_materia(materia):
    try:
        conexao = sqlite3.connect(pasta_db)
        cursor = conexao.cursor()
        texto_existe = cursor.execute("SELECT materia FROM notas WHERE materia = ?", (materia,))
        resulmtr = texto_existe.fetchone() is None
        if resulmtr == True:
            texto_existe = list(texto_existe)
            texto_existe.clear()
            return True
        else:
            cursor.execute("SELECT ID, titulo, texto, materia, fonte FROM notas WHERE materia = ?", (materia,))
            return cursor.fetchall()
    finally:
        conexao.close()

def busca_lang(lang):
    try:
        conexao = sqlite3.connect(pasta_db)
        cursor = conexao.cursor()
        texto_existe = cursor.execute("SELECT linguagem FROM notas WHERE linguagem = ?", (lang,))
        resull = texto_existe.fetchone() is None
        if resull == True:
            texto_existe = list(texto_existe)
            texto_existe.clear()
            return True
        else:
            cursor.execute("SELECT ID, titulo, texto, fonte, codigo, tema, linguagem, fonte_codigo FROM notas WHERE linguagem = ?", (lang,))
            return cursor.fetchall()
    finally:
        conexao.close()

def pega_cor():
    conexao = sqlite3.connect(pasta_db)
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
    conexao = sqlite3.connect(pasta_db)
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
        
def cor_texto_hexa():
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    cores = cursor.execute("SELECT cores FROM usuario")
    for c in cores:
        cores = c
        if cores[0] == "#101A12" or cores[0] == "#000127":
            conexao.close()
            return "white"
        else:
            conexao.close()
            return "black"

def cor_texto_botao():
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    cores = cursor.execute("SELECT cores FROM usuario")
    for c in cores:
        cores = c
    if cores[0] == "#F32A2A":
        conexao.close()
        return "#FAF7F7"
    
def cor_texto_tooltip():
    conexao = sqlite3.connect(pasta_db)
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
    conexao = sqlite3.connect(pasta_db)
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
    conexao = sqlite3.connect(pasta_db)
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
    conexao = sqlite3.connect(pasta_db)
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
    conexao = sqlite3.connect(pasta_db)
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
    conexao = sqlite3.connect(pasta_db)
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
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    cores = cursor.execute("SELECT cores FROM usuario")
    for c in cores:
        cores = c
        if cores[0] == "#FFB0E0":
            conexao.close()
            return alerta_rosa
        elif cores[0] == "#101A12":
            conexao.close()
            return alerta_preto
        elif cores[0] == "#F32A2A":
            conexao.close()
            return alerta_vermelho
        elif cores[0] == "#FFDE21":
            conexao.close()
            return alerta_amarelo
        elif cores[0] == "#008000":
            conexao.close()
            return alerta_verde
        elif cores[0] == "#895129":
            conexao.close()
            return alerta_marrom
        elif cores[0] == "#1093D4":
            conexao.close()
            return alerta_azul
        elif cores[0] == "#EEEBEB":
            conexao.close()
            return alerta_azullogus
        elif cores[0] == "#000127":
            conexao.close()
            return alerta_azulmn
        elif cores[0] == "#F7F7F7":
            conexao.close()
            return alerta_branco
        else:
            conexao.close()
            return alerta_padrao
        
def imagem_ler():
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    cores = cursor.execute("SELECT cores FROM usuario")
    for c in cores:
        cores = c
    if cores[0] == "#101A12" or cores[0] == "#000127":
        conexao.close()
        return leitura_branco
    else:
        conexao.close()
        return leitura_preto

def atualiza_cor(cor):
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    cursor.execute("""UPDATE usuario SET cores = ?""", (cor,))
    conexao.commit()
    conexao.close()

voz = pyttsx3.init()

#Características da voz
voz.setProperty('rate', 130)
voz.setProperty('volume', 1.0)
voz.setProperty('voice', 'pt-br')
vozes = voz.getProperty('voices')      

def inicio():
    voz.say("Olá, seja bem vindo ao isponte, istâri!")
    voz.runAndWait()
    voz.say("Para começarmos essa aventura")
    voz.runAndWait()
    voz.say("Preciso te conhecer")
    voz.runAndWait()
    voz.say("Pôr favor")
    voz.runAndWait()
    voz.say("Preêncha os campos a seguir")
    voz.runAndWait()

def aviso_config():
    voz.say("Aviso: As mudanças, serão aplicadas")
    voz.runAndWait()
    voz.say("após você reiniciar o épi")
    voz.runAndWait()

def bom_dia():
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    nome_usuario = cursor.execute("SELECT nome FROM usuario")
    for nu in nome_usuario:
        nome_usuario = nu
    estado_voz = cursor.execute("SELECT estado_da_voz FROM usuario")
    for ev in estado_voz:
        estado_voz = ev
    if hora >= 0 and hora < 13 and estado_voz[0] == "Ativa" or estado_voz[0] == None:
        voz.say(f"Bom dia {nome_usuario[0]}")
        voz.runAndWait()
    conexao.close()

def boa_tarde():
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    nome_usuario = cursor.execute("SELECT nome FROM usuario")
    for nu in nome_usuario:
        nome_usuario = nu
    estado_voz = cursor.execute("SELECT estado_da_voz FROM usuario")
    for ev in estado_voz:
        estado_voz = ev
    if hora >= 13 and hora < 18 and estado_voz[0] == "Ativa" or estado_voz[0] == None:
        voz.say(f"Boa tarde {nome_usuario[0]}")
        voz.runAndWait() 
    conexao.close()

def boa_noite():
    conexao = sqlite3.connect(pasta_db)
    cursor = conexao.cursor()
    nome_usuario = cursor.execute("SELECT nome FROM usuario")
    for nu in nome_usuario:
        nome_usuario = nu
    estado_voz = cursor.execute("SELECT estado_da_voz FROM usuario")
    for ev in estado_voz:
        estado_voz = ev
    if hora >= 18 and hora < 0 and estado_voz[0] == "Ativa" or estado_voz[0] == None:
        voz.say(f"Boa noite {nome_usuario[0]}")
        voz.runAndWait()
    conexao.close()