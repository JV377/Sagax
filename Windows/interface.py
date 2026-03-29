from customtkinter import *
from tkinter import *
from CTkToolTip import *
from CustomtkinterCodeViewer import CTkCodeViewer as ccv
from CTkCodeBox import CTkCodeBox as ccb
from assistente import *
import os
import threading
from PIL import Image

class janela_inic(CTk):
    def __init__(self):
        super().__init__()
        banco_user()
        adiciona_colunas_codigo()
        self.title("Sponte Study")
        self.geometry("400x270")
        self.resizable(width=False, height=False)
        icone = os.path.join(imagem_pasta, "logo.ico")
        self.iconbitmap(icone)
        #imagens_pasta("imagens/logo.ico")

        self.fonte_titulo = CTkFont(family="Helvetica", size=35, weight="bold")
        self.fonte_inic = CTkFont(family="Arial", size=20)
        self.label_logus = CTkLabel(self, text="Sponte Study", text_color="#105ba0", font=(self.fonte_titulo))
        self.label_logus.pack(pady=30)
        self.inicializacao = CTkLabel(self, text="Inicializando...", text_color="#105ba0", font=(self.fonte_inic))
        self.inicializacao.pack(pady=40)
        self.bem_vindo = CTkLabel(self, text="Boas Vindas", text_color="#105ba0", font=(self.fonte_inic))

        def muda_texto():
            self.inicializacao.destroy()
        def boas_vindas():
            self.bem_vindo.pack(pady=40)
        def fechar():
            self.destroy()
        
        self.after(1900, muda_texto)
        self.after(1900, boas_vindas)
        self.after(2500, fechar)

class janela_preench(CTk):
    def __init__(self):
        super().__init__()
        global feito
        feito = False
        caracteres_invalidos = ('!', '@', '#', '$', '%', '"', '&', '*', '()', '=', '+', '[]', '{}', ':', ';', ',', '.', '/', '|', '\\', '?', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        caracteres_invalidos_niver = ('!', '@', '#', '$', '%', '"', '&', '*', '()', '=', '+', '[]', '{}', ':', ';', ',', '.', '|', '\\', '?', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ,'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
        self.geometry("600x450")
        self.resizable(width=False, height=False)
        self.title("Sponte Study")
        icone = os.path.join(imagem_pasta, "logo.ico")
        self.iconbitmap(icone)

        self.fonte_conhecer = CTkFont(family="Helvetica", size=30, weight="bold")
        self.fonte_erros = CTkFont(family="Arial", size=20, weight="bold")
                        
        self.titulo = CTkLabel(self, text="Conhecendo-te", font=(self.fonte_conhecer), text_color="#105ba0")

        def inserirbarra(evento):
            data_niver = self.data_nasci.get().strip()
            if len(data_niver) == 0:
                self.data_nasci.insert(0, "Exemplo: 25/8") 
                        
        def enviando():
            nome = self.nome_caixa.get().strip()
            idade = self.idade_caixa.get().strip()
            niver = self.data_nasci.get().strip()
            dividir = niver.split("/")
            mnome = self.meunome_caixa.get().strip()

            if len(nome) > 2 and len(idade) > 0 and len(mnome) > 1 and len(niver) >= 3:
                if any(x in caracteres_invalidos for x in nome) or not idade.isdigit() or any(y in caracteres_invalidos for y in mnome) or any(z in caracteres_invalidos_niver for z in niver):
                    self.botao_enviar.configure(state=DISABLED)
                    def habilitar_caractere():
                        self.botao_enviar.configure(state=NORMAL)
                    erro_caractere = CTkLabel(self, text="Erro: Caracteres Inválidos!", text_color="#E21010", font=self.fonte_erros)
                    erro_caractere.place(x=190, y=390)
                    self.after(1200, erro_caractere.destroy)
                    self.after(1200, habilitar_caractere)
                elif all(not x in caracteres_invalidos for x in nome) and idade.isdigit() and all(not y in caracteres_invalidos for y in mnome) and all(not z in caracteres_invalidos_niver for z in niver):
                    idade = int(idade)
                    dividir[0] = int(dividir[0])
                    dividir[1] = int(dividir[1])
                    if idade <= 5:
                        self.botao_enviar.configure(state=DISABLED)
                        def habilitar_idade5():
                            self.botao_enviar.configure(state=NORMAL)
                        erro_idade5 = CTkLabel(self, text="Erro: Menor De Idade!", text_color="#E21010",font=self.fonte_erros)
                        erro_idade5.place(x=200, y=390)
                        self.after(1200, erro_idade5.destroy)
                        self.after(1200, habilitar_idade5)
                    elif idade > 100:
                        self.botao_enviar.configure(state=DISABLED)
                        def habilitar_100():
                            self.botao_enviar.configure(state=NORMAL)
                        erro_idade100 = CTkLabel(self, text="Erro: Idade Inválida!", text_color="#E21010", font=self.fonte_erros)
                        erro_idade100.place(x=210, y=390)
                        self.after(1200, erro_idade100.destroy)
                        self.after(1200, habilitar_100)
                    elif dividir[0] > 31 or dividir[0] < 1 or dividir[1] > 12 or dividir[1] < 1:
                        self.botao_enviar.configure(state=DISABLED)
                        def habilitar_data():
                            self.botao_enviar.configure(state=NORMAL)
                        erro_dia = CTkLabel(self, text="Erro: Data De Aniversário Inválida!", text_color="#E21010", font=self.fonte_erros)
                        erro_dia.place(x=150, y=390)  
                        self.after(1200, erro_dia.destroy)
                        self.after(1200, habilitar_data)
                    elif len(nome) > 25 or len(mnome) > 25 or len(niver) > 5:
                        self.botao_enviar.configure(state=DISABLED)
                        def habilitar_tamanho():
                            self.botao_enviar.configure(state=NORMAL)
                        erro_tamanho = CTkLabel(self, text=f"Erro: Tamanho De Caracteres No Primeiro, \nSegundo ou Terceiro Campos Muito Grandes!", text_color="#E21010", font=self.fonte_erros)
                        erro_tamanho.place(x=100, y=390)
                        self.after(1200, erro_tamanho.destroy)
                        self.after(1200, habilitar_tamanho)
                    elif idade > 5 and idade <= 100 and len(nome) > 2 and len(nome) <= 25 and len(mnome) > 2 and len(mnome) <= 25 and len(niver) >= 3 and len(niver) <= 5:
                        self.botao_enviar.configure(state=DISABLED)
                        inserir_dados(nome, idade, mnome, dividir)
                        dados_salvos = verificar_dados()
                        if dados_salvos == False:
                            self.botao_enviar.configure(text="Enviando...")
                            def destruir_janela():
                                self.destroy()
                            self.after(1500, destruir_janela)
                            global feito
                            feito = True
                        else:
                            self.botao_enviar.configure(state=DISABLED)
                            def habilitar_dados():
                                self.botao_enviar.configure(state=NORMAL)
                            erro_dados = CTkLabel(self, text="Erro: Dados inválidos!", text_color="#E21010", font=self.fonte_erros)
                            erro_dados.place(x=220, y=390)
                            self.after(1200, erro_dados.destroy)
                            self.after(1200, habilitar_dados)
                                
            else:
                self.botao_enviar.configure(state=DISABLED)
                def habilitar_campos():
                    self.botao_enviar.configure(state=NORMAL)
                erro_vazio = CTkLabel(self, text="Erro: Preêncha os campos corretamente!", fg_color="#EEEBEB",text_color="#E21010", font=self.fonte_erros)
                erro_vazio.place(x=120, y=380)
                self.after(1200, erro_vazio.destroy)
                self.after(1200, habilitar_campos)

        self.nome_caixa = CTkEntry(self, width=170, placeholder_text="Digite seu nome...", placeholder_text_color="#105ba0", corner_radius=15, border_color="#105ba0")
        self.idade_caixa = CTkEntry(self, width=170, placeholder_text="Digite sua idade...", placeholder_text_color="#105ba0", corner_radius=15, border_color="#105ba0")
        self.data_nasci = CTkEntry(self, width=180, placeholder_text="Digite sua data de niver...", placeholder_text_color="#105ba0", corner_radius=15, border_color="#105ba0")
        self.data_nasci.bind("<Enter>", inserirbarra)
        self.meunome_caixa = CTkEntry(self, width=178, placeholder_text="Como deseja me chamar?", placeholder_text_color="#105ba0", corner_radius=15, border_color="#105ba0")
        self.botao_enviar = CTkButton(self, text="Começar", width=100, cursor="hand2", corner_radius=10, border_width=2, border_color="black", fg_color="#105ba0", text_color="white", command=enviando)

        def conhecer():
            self.titulo.pack(pady=30)
            self.nome_caixa.pack(pady=15)
            self.idade_caixa.pack(pady=15)
            self.data_nasci.pack(pady=15)
            self.meunome_caixa.pack(pady=15)
            self.botao_enviar.pack(pady=20)

        self.after(10, conhecer)

class janela_principal(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("490x370")
        self.resizable(width=False, height=False)
        self.title("Sponte Study")
        icone = os.path.join(imagem_pasta, "logo.ico")
        self.iconbitmap(icone)
        
        pg = pega_cor()
        ct = cor_texto()
        ctb = cor_texto_botao()
        ctt = cor_texto_tooltip()
        cth = cor_texto_hexa()
        cf = cor_fundo()
        cbp = cor_borda_place()
        cls = cor_labels()
        ch = cor_hover()
        cn = cor_notas()
        pev = pegar_estado_voz()
        caminho_alerta = imagem_cor()
        caminho_leitura = imagem_ler()
        self.configure(fg_color=pg)

        caracteres_invalidos_hexa = ('!', '@', '$', '%', '"', '&', '*', '()', '=', '+', '[]', '{}', ':', ';', ',', '.', '|', '\\', '?', '_')

        alerta = CTkImage(Image.open(os.path.join(imagem_pasta, caminho_alerta)), size=(17, 17))
        leitura = CTkImage(Image.open(os.path.join(imagem_pasta, caminho_leitura)), size=(13, 13))

        #Definindo a fonte da hora
        fonte_hora = CTkFont(family="Arial", size=40, weight="bold")
        #Fonte da data
        fonte_data = CTkFont(family="Arial", size=18, weight="bold")
        #Fonte de erros internos
        fonte_erros_inter = CTkFont(family="Arial", size=15, weight="bold")
        #Fonte do label ajuda
        fonte_ajuda = CTkFont(family="Arial", size=15, weight="bold")
        #Fonte para negritos
        fonte_negrito = CTkFont(family="Arial", size=15, weight="bold")
        #Fontes das anotações
        fonte_8 = CTkFont(family="Arial", size=8)
        fonte_10 = CTkFont(family="Arial", size=10)
        fonte_12 = CTkFont(family="Arial", size=12)
        fonte_14 = CTkFont(family="Arial", size=14)
        fonte_16 = CTkFont(family="Arial", size=16)
        fonte_18 = CTkFont(family="Arial", size=18)
        fonte_20 = CTkFont(family="Arial", size=20)
        fonte_22 = CTkFont(family="Arial", size=22)
        
        #Pegando hora para GUI
        hora_gui = tempo.tm_hour

        def atualizar_hora_GUI():
        #Pega a hora atual e coloca no label
            self.label_hora.configure(text=time.strftime("%H:%M:%S"))
        #Agenda essa atualização
            self.after(1000, atualizar_hora_GUI)
            self.after(900000, atualiza_hora)
            
        def atualiza_dia_back():
            self.thread_atualizadia = threading.Thread(target=atualiza_dia, daemon=True)
            self.thread_atualizadia.start()

        def reiniciar_saudacao():
            self.thread_reinicia_saudacao = threading.Thread(target=reiniciar_ciclo_saudacao, daemon=True)
            self.thread_reinicia_saudacao.start()
        
        def explica_config_entra(evento):
            self.label_ajuda.configure(text="Um mundo de customização")
            self.label_ajuda.place(x=45, y=210)

        def explica_notas_entra(evento):
            self.label_ajuda.configure(text="Anote tudo o que quiser")
            self.label_ajuda.place(x=57, y=210)

        def explica_config_fora(evento):
            self.label_ajuda.configure(text="Seu app de organização \ncom voz 100% offline")
            self.label_ajuda.place(x=55, y=210)

        def explica_notas_fora(evento):
            self.label_ajuda.configure(text="Seu app de organização \ncom voz 100% offline")
            self.label_ajuda.place(x=55, y=210)

        #Função bom dia/boa (tarde/noite)
        def saudacao_gui():
            vfd  = verifica_fala_dia()
            vft = verifica_fala_tarde()
            vfn = verifica_fala_noite()
            n = nome()
            if vfd == False and hora_gui >= 0 and hora_gui < 13:
                def tira_labeld():
                    self.label_dia.destroy()
                self.label_dia = CTkLabel(self.frame_central, text=f"Bom dia {n}!", text_color=ct, font=fonte_data, width=90, height=20)
                self.label_dia.place(x=73, y=15)
                faloud = True
                hora_da_fala_dia(faloud)
                self.after(1500, tira_labeld)
            elif vft == False and hora_gui >= 13 and hora_gui < 18:
                def tira_labelt():
                    self.label_tarde.destroy()
                self.label_tarde = CTkLabel(self.frame_central, text=f"Boa tarde {n}!", width=90, height=20, text_color=ct, font=fonte_data)
                self.label_tarde.place(x=73, y=15)
                faloudt = True
                hora_da_fala_tarde(faloudt)
                self.after(1500, tira_labelt)
            elif vfn == False and hora_gui >= 18 and hora_gui <= 23:
                    def tira_labeln():
                        self.label_noite.destroy()
                    self.label_noite = CTkLabel(self.frame_central, text=f"Boa noite {n}!", width=90, height=20, text_color=ct, font=fonte_data)
                    self.label_noite.place(x=73, y=15)
                    faloun = True
                    hora_da_fala_noite(faloun)
                    self.after(1500, tira_labeln)

        def voltar_notas_b():
                self.frame_notas.place_forget()
                self.frame_central.pack(pady=20)

        def escolha_comecar_b(escolha):
                    if escolha == "Nota":
                        def voltar_anota_b():
                            self.frame_notas.place(x=20, y=0)
                            self.frame_anota.pack_forget()

                        def salvar_texto_b():
                            data_atual_nota = time.strftime("%d/%m/%Y")
                            titulo = self.titulo.get()
                            titulo = titulo.strip().capitalize()
                            anotacao = self.texto.get("1.0", "end")
                            anotacao = anotacao.strip().capitalize()
                            negrito = self.texto._textbox.tag_ranges("negrito")
                            fonte = self.tamanho_fonte.get()
                            data_c = data_atual_nota
                            materia = self.tipo_nota.get()
                            if fonte == "Tamanho Da Fonte...":
                                fonte = 12
                            if materia == "Tipo De Notas...":
                                materia = "Outros Estudos"
                                if len(titulo) >= 3 and len(titulo) < 30 and len(anotacao) >= 3 and len(anotacao) < 500:
                                    guarda_titulo_nota(titulo, anotacao, fonte, data_c, materia)
                                    verificacao = verifica_guarda_titulo()
                                if verificacao == False:
                                    def tira_salvo():
                                        self.label_salvo.destroy()
                                    self.texto.delete("1.0", "end")
                                    self.titulo.delete(0, "end")
                                    self.tipo_nota.set("Tipo De Notas...")
                                    self.tamanho_fonte.set("Tamanho Da Fonte...")
                                    self.label_salvo = CTkLabel(self.frame_anota, text="Salvo com sucesso!!", text_color="#2E6F40",
                                    font=fonte_erros_inter, fg_color=pg)
                                    self.label_salvo.place(x=15, y=4)
                                    self.after(1400, tira_salvo)
                                else:
                                    def tira_erro_salvo():
                                        self.label_erro_salvo.destroy()
                                    self.label_erro_salvo = CTkLabel(self.frame_anota, text="Não Salvou!!!", text_color="#E21010",font=fonte_erros_inter)
                                    self.label_salvo.place(x=15, y=4)
                                    self.after(1400, tira_erro_salvo)
                            elif len(titulo) < 3 or len(titulo) > 30:
                                def tira_erro():
                                    self.erro_titulo.destroy()
                                self.erro_titulo = CTkLabel(self.frame_anota, text="Tamanho de título inválido (Min:3, Max:30)!!", text_color="#E21010", font=fonte_erros_inter)
                                self.erro_titulo.place(x=15, y=4)
                                self.after(1400, tira_erro)
                            elif len(anotacao) < 3 or len(anotacao) > 500:
                                def tira_erro():
                                    self.erro_nota.destroy()
                                self.erro_nota = CTkLabel(self.frame_anota, text="Tamanho de nota inválido (Min:3, Max:500)!!", text_color="#E21010", font=fonte_erros_inter)
                                self.erro_nota.place(x=15, y=4)
                                self.after(1400, tira_erro)
                    
                        def muda_titulo_b(nota_escolha):
                            if nota_escolha == "Português":
                                self.titulo.configure(placeholder_text="Gramática, literatura, redação...")
                                self.tipo_nota.configure(fg_color="#FF8DA1", button_color="#FF8DA1", button_hover_color="#E67E91")
                            elif nota_escolha == "Matemática":
                                self.titulo.configure(placeholder_text="Frações, funções, regra de três...")
                                self.tipo_nota.configure(fg_color="#1591EA", button_color="#1591EA", button_hover_color="#127BC6")
                            elif nota_escolha == "História":
                                self.titulo.configure(placeholder_text="Brasil, revoluções, guerras...")
                                self.tipo_nota.configure(fg_color="#FFA500", button_color="#FFA500", button_hover_color="#E39400")
                            elif nota_escolha == "Geografia":
                                self.titulo.configure(placeholder_text="Clima, relevo, globalização...")
                                self.tipo_nota.configure(fg_color="#50C878", button_color="#50C878", button_hover_color="#46AC68")
                            elif nota_escolha == "Ciências":
                                self.titulo.configure(placeholder_text="Física, química, biologia...")
                                self.tipo_nota.configure(fg_color="#2E6F40", button_color="#2E6F40", button_hover_color="#328A51")
                            elif nota_escolha == "Inglês":
                                self.titulo.configure(placeholder_text="Conectivos, dia a dia, pronouns...")
                                self.tipo_nota.configure(fg_color="#C9A41D", button_color="#C9A41D", button_hover_color="#B6941B")
                            else:
                                self.titulo.configure(placeholder_text="Título...")
                                self.tipo_nota.configure(fg_color=cls, button_color=cls, button_hover_color=ch)

                        def fonte_tamanho_b(tamanho):
                            if tamanho == "8":
                                self.texto.configure(font=fonte_8)
                            elif tamanho == "10":
                                self.texto.configure(font=fonte_10)
                            elif tamanho == "12":
                                self.texto.configure(font=fonte_12)
                            elif tamanho == "14":
                                self.texto.configure(font=fonte_14)
                            elif tamanho == "16":
                                self.texto.configure(font=fonte_16)
                            elif tamanho == "18":
                                self.texto.configure(font=fonte_18)
                            elif tamanho == "20":
                                self.texto.configure(font=fonte_20)
                            elif tamanho == "22":
                                self.texto.configure(font=fonte_22)

                        def apaga_texto_b(evento):
                            self.texto.delete("0.0", END)

                        def ler_b():
                            self.botao_leitura_b.configure(state=DISABLED)
                            def ler_titulo_b():
                                titulo_b = self.titulo.get()
                                texto_b = self.texto.get("1.0", "end")
                                if len(titulo_b) >= 3 and len(texto_b) >= 3 and pev == "Ativa":
                                    voz.say(titulo_b)
                                    voz.runAndWait()
                                    voz.setProperty('rate', 127)
                                    voz.say(texto_b)
                                    voz.runAndWait()
                                elif len(titulo_b) < 3 or len(titulo_b) > 30:
                                        def tira_erro_b():
                                            self.erro_titulo_b.destroy()
                                        self.erro_titulo_b = CTkLabel(self.frame_anota, text="Tamanho de título inválido (Min:3, Max:30)!!", text_color="#981212", font=fonte_erros_inter)
                                        self.erro_titulo_b.place(x=15, y=4)
                                        self.after(1400, tira_erro_b)
                                elif len(texto_b) < 3 or len(texto_b) > 500:
                                        def tira_erro_b():
                                            self.erro_nota_b.destroy()
                                        self.erro_nota_b = CTkLabel(self.frame_anota, text="Tamanho de nota inválida (Min:3, Max:500)!!", text_color="#981212", font=fonte_erros_inter)
                                        self.erro_nota_b.place(x=15, y=4)
                                        self.after(1400, tira_erro_b)
                                else:
                                    def tira_ativa_voz_b():
                                        self.label_ative_voz_b.destroy()
                                        self.botao_leitura_b.configure(state=NORMAL)
                                    self.label_ative_voz_b = CTkLabel(self.frame_anota, text="Ative a Voz!", text_color="#E21010", font=fonte_erros_inter)
                                    self.label_ative_voz_b.place(x=170, y=5)
                                    self.after(1100, tira_ativa_voz_b)
                                self.botao_leitura_b.configure(state=NORMAL)
                            self.thread_ler_titulo_b = threading.Thread(target=ler_titulo_b, daemon=True)
                            self.thread_ler_titulo_b.start()

                        def negrito(evento):
                            self.texto._textbox.tag_add("negrito", "sel.first", "sel.last")
                            self.texto._textbox.tag_configure("negrito", font=fonte_negrito)

                        self.frame_notas.place_forget() 
                        self.frame_anota = CTkFrame(self, width=450, height=340, fg_color=pg)
                        self.frame_anota.pack(pady=20)
                        self.botao_voltar_anotas = CTkButton(self.frame_anota, text="Voltar", fg_color=cls, width=4, height=22,border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=voltar_anota_b, hover_color=ch)
                        self.botao_voltar_anotas.place(x=394, y=1)
                        self.tipo_nota = CTkOptionMenu(self.frame_anota, width=90, cursor="hand2", values=["Português", "Matemática", "História", "Geografia", "Ciências", "Inglês", "Outros Estudos"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=muda_titulo_b)
                        self.tipo_nota.place(x=290, y=110)
                        self.tamanho_fonte = CTkOptionMenu(self.frame_anota, width=90, cursor="hand2", values=["8","10", "12", "14", "16", "18", "20", "22"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=fonte_tamanho_b)
                        self.tamanho_fonte.place(x=275, y=150)
                        self.tamanho_fonte.set("Tamanho Da Fonte...")
                        self.tipo_nota.set("Tipo De Notas...")
                        self.titulo = CTkEntry(self.frame_anota, width=222, placeholder_text="Título...", corner_radius=10, border_color=cbp, placeholder_text_color=cbp, text_color=ctt, fg_color=cf)
                        self.titulo.place(x=10, y=80)
                        self.texto = CTkTextbox(self.frame_anota, width=222, height=200, border_width=2, border_color=cbp, corner_radius=10, text_color=ctt, fg_color=cf)
                        self.texto.place(x=10, y=120)
                        self.texto.insert("0.0", "Hoje aprendi sobre...")
                        self.texto.bind("<Control-n>", negrito)
                        CTkToolTip(self.texto, message="Clique o botão direito do mouse", alpha=0.81, text_color=ctt, bg_color=cf)
                        self.texto.bind("<Button-3>", apaga_texto_b)
                        self.botao_salvar = CTkButton(self.frame_anota, text="Salvar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=salvar_texto_b, hover_color=ch)
                        self.botao_salvar.place(x=238, y=295)
                        self.botao_leitura_b = CTkButton(self.frame_anota, text="Ler", image=leitura, fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=ler_b, hover_color=ch)
                        self.botao_leitura_b.place(x=308, y=295)
                    
                    elif escolha == "Código":
                        def voltar_code():
                            self.frame_codigo.pack_forget()
                            self.frame_notas.place(x=20, y=0)
                        
                        def apaga_descricao(evento):
                            self.descricao.delete("0.0", END)
                        
                        def apaga_texto_codigo(evento):
                            self.texto_codigo.delete("0.0", END)

                        def fonte_tamanho_codigo(tamanho):
                            if tamanho == "8":
                                self.texto_codigo.configure(font=fonte_8)
                            elif tamanho == "10":
                                self.texto_codigo.configure(font=fonte_10)
                            elif tamanho == "12":
                                self.texto_codigo.configure(font=fonte_12)
                            elif tamanho == "14":
                                self.texto_codigo.configure(font=fonte_14)
                            elif tamanho == "16":
                                self.texto_codigo.configure(font=fonte_16)
                            elif tamanho == "18":
                                self.texto_codigo.configure(font=fonte_18)
                            elif tamanho == "20":
                                self.texto_codigo.configure(font=fonte_20)
                            elif tamanho == "22":
                                self.texto_codigo.configure(font=fonte_22)

                        def fonte_tamanho_descricao(tamanho):
                            if tamanho == "8":
                                self.descricao.configure(font=fonte_8)
                            elif tamanho == "10":
                                self.descricao.configure(font=fonte_10)
                            elif tamanho == "12":
                                self.descricao.configure(font=fonte_12)
                            elif tamanho == "14":
                                self.descricao.configure(font=fonte_14)
                            elif tamanho == "16":
                                self.descricao.configure(font=fonte_16)
                            elif tamanho == "18":
                                self.descricao.configure(font=fonte_18)
                            elif tamanho == "20":
                                self.descricao.configure(font=fonte_20)
                            elif tamanho == "22":
                                self.descricao.configure(font=fonte_22)
                            
                        def lang(lang_escolhida):
                            if lang_escolhida == "Python":
                                self.texto_codigo.configure(language="python")
                            elif lang_escolhida == "Zig":
                                self.texto_codigo.configure(language="zig")
                            elif lang_escolhida == "Javascript":
                                self.texto_codigo.configure(language="Javascript")
                            elif lang_escolhida == "C++":
                                self.texto_codigo.configure(language="c++")
                            elif lang_escolhida == "Lua":
                                self.texto_codigo.configure(language="lua")
                            elif lang_escolhida == "Rust":
                                self.texto_codigo.configure(language="rust")
                            elif lang_escolhida == "Java":
                                self.texto_codigo.configure(language="java")
                            elif lang_escolhida == "CSS":
                                self.texto_codigo.configure(language="css")
                            elif lang_escolhida == "HTML":
                                self.texto_codigo.configure(language="html")
                            elif lang_escolhida == "C#":
                                self.texto_codigo.configure(language="c#")
                            elif lang_escolhida == "PHP":
                                self.texto_codigo.configure(language="php")
                        
                        def tema(tema_escolhido):
                            if tema_escolhido == "Arduino":
                                self.texto_codigo.configure(theme="arduino")
                            elif tema_escolhido == "Abap":
                                self.texto_codigo.configure(theme="abap")
                            elif tema_escolhido == "Autumn":
                                self.texto_codigo.configure(theme="autumn")
                            elif tema_escolhido == "Borland":
                                self.texto_codigo.configure(theme="borland")
                            elif tema_escolhido == "Colorful":
                                self.texto_codigo.configure(theme="colorful")
                            elif tema_escolhido == "Default":
                                self.texto_codigo.configure(theme="default")
                            elif tema_escolhido == "Dracula":
                                self.texto_codigo.configure(theme="dracula")
                            elif tema_escolhido == "Emacs":
                                self.texto_codigo.configure(theme="emacs")
                            elif tema_escolhido == "Friendly":
                                self.texto_codigo.configure(theme="friendly")
                            elif tema_escolhido == "Fruit":
                                self.texto_codigo.configure(theme="fruit")
                            elif tema_escolhido == "Igor":
                                self.texto_codigo.configure(theme="igor")
                            elif tema_escolhido == "Inkpot":
                                self.texto_codigo.configure(theme="inkpot")

                        def salvar_texto_codigo():
                            data_atual_codigo = time.strftime("%d/%m/%Y")
                            titulo_codigo = self.titulo_codigo.get().strip().capitalize()
                            descricao = self.descricao.get("1.0", "end").strip().capitalize()
                            codigo = self.texto_codigo.get("1.0", "end").strip()
                            fonte_codigo = self.fonte_tamanho_codigo.get()
                            fonte_descricao = self.fonte_tamanho_descricao.get()
                            tema = self.tema.get().lower()
                            linguagem = self.linguagem.get().lower()
                            data_c = data_atual_codigo
                            if fonte_codigo == "Tamanho Da Fonte...":
                                fonte_codigo = 12
                            if fonte_descricao == "Tamanho Da Fonte...":
                                fonte_descricao = 12
                            if tema == "seu tema favorito...":
                                tema = "arduino"
                            if linguagem == "sua linguagem favorita...":
                                linguagem = "python"
                            if len(titulo_codigo) >= 3 and len(titulo_codigo) < 30 and len(descricao) >= 3 and len(descricao) < 500 and len(codigo) >= 3:
                                guarda_codigos(titulo_codigo, descricao, fonte_descricao, data_c, codigo, fonte_codigo, tema, linguagem)
                                verificacao = verifica_guarda_codigo()
                                if verificacao == False:
                                    def tira_salvo():
                                        self.label_salvo.destroy()
                                        self.texto_codigo.delete("1.0", "end")
                                        self.titulo_codigo.delete(0, "end")
                                        self.descricao.delete("1.0", "end")
                                        self.fonte_tamanho_descricao.set("Tamanho Da Fonte...")
                                        self.fonte_tamanho_codigo.set("Tamanho Da Fonte...")
                                        self.tema.set("Seu Tema Favorito...")
                                        self.linguagem.set("Sua Linguagem Favorita...")
                                    self.label_salvo = CTkLabel(self.frame_codigo, text="Salvo com sucesso!!", text_color="#2E6F40", font=fonte_erros_inter, fg_color=pg)
                                    self.label_salvo.place(x=75, y=2)
                                    self.after(1400, tira_salvo)
                                else:
                                    def tira_erro_salvo():
                                        self.label_erro_salvo.destroy()
                                    self.label_erro_salvo = CTkLabel(self.frame_codigo, text="Não Salvou!!!", text_color="#E21010", font=fonte_erros_inter)
                                    self.label_salvo.place(x=75, y=2)
                                    self.after(1400, tira_erro_salvo)
                            elif len(titulo_codigo) < 3 or len(titulo_codigo) > 30:
                                def tira_erro():
                                    self.erro_titulo.destroy()
                                self.erro_titulo = CTkLabel(self.frame_codigo, text="Tamanho de título inválido (Min:3, Max:30)!!", text_color="#E21010", font=fonte_erros_inter)
                                self.erro_titulo.place(x=167, y=30)
                                self.after(1400, tira_erro)
                            elif len(descricao) < 3 or len(descricao) > 500:
                                def tira_erro():
                                    self.erro_nota.destroy()
                                self.erro_nota = CTkLabel(self.frame_codigo, text="Tamanho de descrição\n inválida (Min:3, Max:500)!!", text_color="#E21010", font=fonte_erros_inter)
                                self.erro_nota.place(x=245, y=30)
                                self.after(1400, tira_erro)
                            elif len(codigo) < 3:
                                def tira_erro():
                                    self.erro_nota.destroy()
                                self.erro_nota = CTkLabel(self.frame_codigo, text="Digite seu código!!", text_color="#E21010", font=fonte_erros_inter)
                                self.erro_nota.place(x=288, y=30)
                                self.after(1400, tira_erro)

                        def ler_descricao():
                            self.botao_leitura_codigos.configure(state=DISABLED)
                            def ler_texto():
                                titulo_codigo = self.titulo_codigo.get()
                                descricao = self.descricao.get("1.0", "end")
                                if len(titulo_codigo) > 3 and len(descricao) > 3 and pev == "Ativa":
                                    voz.say(titulo_codigo)
                                    voz.runAndWait()
                                    voz.setProperty('rate', 127)
                                    voz.say(descricao)
                                    voz.runAndWait()
                                elif len(titulo_codigo) < 3 or len(titulo_codigo) > 30:
                                    def tira_erro():
                                        self.erro_titulo.destroy()
                                    self.erro_titulo = CTkLabel(self.frame_codigo, text="Tamanho de título inválido (Min:3, Max:30)!!", text_color="#981212", font=fonte_erros_inter)
                                    self.erro_titulo.place(x=167, y=30)
                                    self.after(1400, tira_erro)
                                elif len(descricao) < 3 or len(descricao) > 500:
                                        def tira_erro():
                                            self.erro_nota.destroy()
                                        self.erro_nota = CTkLabel(self.frame_codigo, text="Tamanho de descrição inválida (Min:3, Max:500)!!", text_color="#981212", font=fonte_erros_inter)
                                        self.erro_nota.place(x=245, y=30)
                                        self.after(1400, tira_erro)
                                else:
                                    def tira_ativa_voz():
                                        self.label_ative_voz.destroy()
                                        self.botao_leitura_codigos.configure(state=NORMAL)
                                    self.label_ative_voz = CTkLabel(self.frame_codigo, text="Ative a Voz!", text_color="#E21010", font=fonte_erros_inter)
                                    self.label_ative_voz.place(x=170, y=2)
                                    self.botao_leitura_codigos.configure(state=DISABLED)
                                    self.after(1100, tira_ativa_voz)
                                self.botao_leitura_codigos.configure(state=NORMAL)
                            self.thread_ler_descricao = threading.Thread(target=ler_texto, daemon=True)
                            self.thread_ler_descricao.start()

                        def muda_titulo_codigo(evento):
                            self.titulo_codigo.configure(placeholder_text="Projeto, função de, conceito...")

                        self.frame_notas.place_forget()    
                        self.frame_codigo = CTkFrame(self, width=470, height=360, fg_color=pg)
                        self.frame_codigo.pack(pady=20)
                        self.botao_voltar_codigo = CTkButton(self.frame_codigo, text="Voltar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=voltar_code, hover_color=ch)
                        self.botao_voltar_codigo.place(x=404, y=1)
                        self.fonte_tamanho_codigo = CTkOptionMenu(self.frame_codigo, width=90, cursor="hand2", values=["8","10", "12", "14", "16", "18", "20", "22"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=fonte_tamanho_codigo)
                        self.fonte_tamanho_codigo.place(x=4, y=25)
                        self.fonte_tamanho_codigo.set("Tamanho Da Fonte...")
                        self.texto_codigo = ccb.CTkCodeBox(self.frame_codigo, width=227, height=160, theme="arduino", language="python",fg_color=cf, border_width=2, border_color=cbp, corner_radius=10, numbering_color=cbp, menu=False)
                        self.texto_codigo.place(x=4, y=130)
                        self.texto_codigo.insert("0.0", ">Código...")
                        CTkToolTip(self.texto_codigo, message="Clique o botão direito do mouse", alpha=0.81, text_color=ctt, bg_color=cf)
                        self.texto_codigo.bind("<Button-3>", apaga_texto_codigo)
                        self.tema = CTkOptionMenu(self.frame_codigo, width=90, cursor="hand2", values=["Arduino","Abap", "Autumn", "Borland", "Colorful", "Default", "Dracula", "Emacs", "Friendly", "Fruity", "Igor", "Inkpot"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=tema)
                        self.tema.place(x=4, y=60)
                        self.tema.set("Seu Tema Favorito...")
                        self.linguagem = CTkOptionMenu(self.frame_codigo, width=90, cursor="hand2", values=["Python", "JavaScript", "Lua", "Rust", "CSS", "HTML", "Java", "C++", "PHP", "C#", "Zig"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=lang)
                        self.linguagem.place(x=4, y=95)
                        self.linguagem.set("Sua Linguagem Favorita...")
                        self.fonte_tamanho_descricao = CTkOptionMenu(self.frame_codigo, width=90, cursor="hand2", values=["8","10", "12", "14", "16", "18", "20", "22"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=fonte_tamanho_descricao)
                        self.fonte_tamanho_descricao.place(x=282, y=115)
                        self.fonte_tamanho_descricao.set("Tamanho Da Fonte...")
                        self.titulo_codigo = CTkEntry(self.frame_codigo, width=212, border_width=2, border_color=cbp, corner_radius=10, text_color=ctt, fg_color=cf, placeholder_text="Título...", placeholder_text_color=cbp)
                        self.titulo_codigo.place(x=258, y=70)
                        self.titulo_codigo.bind("<Enter>", muda_titulo_codigo)
                        self.descricao = CTkTextbox(self.frame_codigo, width=212, height=90, border_width=2, border_color=cbp, corner_radius=10, text_color=ctt, fg_color=cf)
                        self.descricao.place(x=258, y=150)
                        self.descricao.insert("0.0", "Esse código faz...")
                        CTkToolTip(self.descricao, message="Clique o botão direito do mouse", alpha=0.81, text_color=ctt, bg_color=cf)
                        self.descricao.bind("<Button-3>", apaga_descricao)
                        self.botao_salvar = CTkButton(self.frame_codigo, text="Salvar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=salvar_texto_codigo, hover_color=ch)
                        self.botao_leitura_codigos = CTkButton(self.frame_codigo, text="Ler", image=leitura, fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=ler_descricao, hover_color=ch)
                        self.botao_salvar.place(x=236, y=303)
                        self.botao_leitura_codigos.place(x=398, y=247)

        def muda_aba_codigo():
                def muda_aba_nota_c():
                    self.frame_notas.place(x=20, y=0)
                    self.frame_codigos.place_forget()

                def voltar_codigos():
                    self.frame_central.pack(pady=20)
                    self.frame_codigos.place_forget()

                def escolha_comecar_codigo(escolha):
                    if escolha == "Nota":
                        def voltar_code():
                            self.frame_codigos.place(x=20, y=0)
                            self.frame_anota.pack_forget()

                        def salvar_texto():
                            data_atual_nota = time.strftime("%d/%m/%Y")
                            titulo = self.titulo.get()
                            titulo = titulo.strip().capitalize()
                            anotacao = self.texto.get("1.0", "end")
                            anotacao = anotacao.strip().capitalize()
                            fonte = self.tamanho_fonte.get()
                            data_c = data_atual_nota
                            materia = self.tipo_nota.get()
                            if fonte == "Tamanho Da Fonte...":
                                fonte = 12
                            if materia == "Tipo De Notas...":
                                materia = "Outros Estudos"
                            if len(titulo) >= 3 and len(titulo) < 30 and len(anotacao) >= 3 and len(anotacao) < 500:
                                guarda_titulo_nota(titulo, anotacao, fonte, data_c, materia)
                                verificacao = verifica_guarda_titulo()
                                if verificacao == False:
                                    def tira_salvo():
                                        self.label_salvo.destroy()
                                        self.texto.delete("1.0", "end")
                                        self.titulo.delete(0, "end")
                                        self.tipo_nota.set("Tipo De Notas...")
                                        self.tamanho_fonte.set("Tamanho Da Fonte...")
                                    self.label_salvo = CTkLabel(self.frame_anota, text="Salvo com sucesso!!", text_color="#2E6F40", font=fonte_erros_inter, fg_color=pg)
                                    self.label_salvo.place(x=15, y=4)
                                    self.after(1400, tira_salvo)
                                else:
                                    def tira_erro_salvo():
                                        self.label_erro_salvo.destroy()
                                    self.label_erro_salvo = CTkLabel(self.frame_anota, text="Não Salvou!!!", text_color="#E21010", font=fonte_erros_inter)
                                    self.label_salvo.place(x=15, y=4)
                                    self.after(1400, tira_erro_salvo)
                            elif len(titulo) < 3 or len(titulo) > 30:
                                def tira_erro():
                                    self.erro_titulo.destroy()
                                self.erro_titulo = CTkLabel(self.frame_anota, text="Tamanho de título inválido (Min:3, Max:30)!!", text_color="#E21010", font=fonte_erros_inter)
                                self.erro_titulo.place(x=15, y=4)
                                self.after(1400, tira_erro)
                            elif len(anotacao) < 3 or len(anotacao) > 500:
                                def tira_erro():
                                    self.erro_nota.destroy()
                                self.erro_nota = CTkLabel(self.frame_anota, text="Tamanho de nota inválido (Min:3, Max:500)!!", text_color="#E21010", font=fonte_erros_inter)
                                self.erro_nota.place(x=15, y=4)
                                self.after(1400, tira_erro)
                        
                        def muda_titulo(nota_escolha):
                            if nota_escolha == "Português":
                                self.titulo.configure(placeholder_text="Gramática, literatura, redação...")
                                self.tipo_nota.configure(fg_color="#FF8DA1", button_color="#FF8DA1", button_hover_color="#E67E91")
                                self.texto.delete("0.0", "end")
                                self.texto.insert("0.0", "Hoje aprendi sobre...")
                            elif nota_escolha == "Matemática":
                                self.titulo.configure(placeholder_text="Frações, funções, regra de três...")
                                self.tipo_nota.configure(fg_color="#1591EA", button_color="#1591EA", button_hover_color="#127BC6")
                                self.texto.delete("0.0", "end")
                                self.texto.insert("0.0", "Hoje aprendi sobre...")
                            elif nota_escolha == "História":
                                self.titulo.configure(placeholder_text="Brasil, revoluções, guerras...")
                                self.tipo_nota.configure(fg_color="#FFA500", button_color="#FFA500", button_hover_color="#E39400")
                                self.texto.delete("0.0", "end")
                                self.texto.insert("0.0", "Hoje aprendi sobre...")
                            elif nota_escolha == "Geografia":
                                self.titulo.configure(placeholder_text="Clima, relevo, globalização...")
                                self.tipo_nota.configure(fg_color="#50C878", button_color="#50C878", button_hover_color="#46AC68")
                                self.texto.delete("0.0", "end")
                                self.texto.insert("0.0", "Hoje aprendi sobre...")
                            elif nota_escolha == "Ciências":
                                self.titulo.configure(placeholder_text="Física, química, biologia, energia...")
                                self.tipo_nota.configure(fg_color="#2E6F40", button_color="#2E6F40", button_hover_color="#328A51")
                                self.texto.delete("0.0", "end")
                                self.texto.insert("0.0", "Hoje aprendi sobre...")
                            elif nota_escolha == "Inglês":
                                self.titulo.configure(placeholder_text="Conectivos, dia a dia, pronouns...")
                                self.tipo_nota.configure(fg_color="#C9A41D", button_color="#C9A41D", button_hover_color="#B6941B")
                                self.texto.delete("0.0", "end")
                                self.texto.insert("0.0", "Hoje aprendi sobre...")
                            elif nota_escolha == "Programação":
                                self.titulo.configure(placeholder_text="POO, variáveis, condicionais...")
                                self.tipo_nota.configure(fg_color="#236BAF", button_color="#236BAF", button_hover_color="#1F63A3")
                                self.texto.delete("0.0", "end")
                                self.texto.insert("0.0", "O conceito é...")
                            else:
                                self.titulo.configure(placeholder_text="Título...")
                                self.tipo_nota.configure(fg_color=cls, button_color=cls, button_hover_color=ch)

                        def fonte_tamanho(tamanho):
                            if tamanho == "8":
                                self.texto.configure(font=fonte_8)
                            elif tamanho == "10":
                                self.texto.configure(font=fonte_10)
                            elif tamanho == "12":
                                self.texto.configure(font=fonte_12)
                            elif tamanho == "14":
                                self.texto.configure(font=fonte_14)
                            elif tamanho == "16":
                                self.texto.configure(font=fonte_16)
                            elif tamanho == "18":
                                self.texto.configure(font=fonte_18)
                            elif tamanho == "20":
                                self.texto.configure(font=fonte_20)
                            elif tamanho == "22":
                                self.texto.configure(font=fonte_22)

                        def apaga_texto(evento):
                            self.texto.delete("0.0", END)

                        def ler():
                            self.botao_leitura.configure(state=DISABLED)
                            def ler_titulo():
                                titulo = self.titulo.get()
                                texto = self.texto.get("1.0", "end")
                                if len(titulo) >= 3 and len(texto) >= 3 and pev == "Ativa":
                                    voz.say(titulo)
                                    voz.runAndWait()
                                    voz.setProperty('rate', 127)
                                    voz.say(texto)
                                    voz.runAndWait()
                                elif len(titulo) < 3 or len(titulo) > 30:
                                        def tira_erro():
                                            self.erro_titulo.destroy()
                                        self.erro_titulo = CTkLabel(self.frame_anota, text="Tamanho de título inválido (Min:3, Max:30)!!", text_color="#981212", font=fonte_erros_inter)
                                        self.erro_titulo.place(x=15, y=4)
                                        self.after(1400, tira_erro)
                                elif len(texto) < 3 or len(texto) > 500:
                                        def tira_erro():
                                            self.erro_nota.destroy()
                                        self.erro_nota = CTkLabel(self.frame_anota, text="Tamanho de nota inválido (Min:3, Max:500)!!", text_color="#981212", font=fonte_erros_inter)
                                        self.erro_nota.place(x=15, y=4)
                                        self.after(1400, tira_erro)
                                else:
                                    def tira_ativa_voz():
                                        self.label_ative_voz.destroy()
                                        self.botao_leitura.configure(state=NORMAL)
                                    self.botao_leitura.configure(state=DISABLED)
                                    self.label_ative_voz = CTkLabel(self.frame_anota, text="Ative a Voz!", text_color="#E21010", font=fonte_erros_inter)
                                    self.label_ative_voz.place(x=170, y=5)
                                    self.after(1100, tira_ativa_voz)
                                self.botao_leitura.configure(state=NORMAL)
                            self.thread_ler_titulo = threading.Thread(target=ler_titulo, daemon=True)
                            self.thread_ler_titulo.start()

                        self.frame_codigos.place_forget()
                        self.frame_anota = CTkFrame(self, width=450, height=340, fg_color=pg)
                        self.frame_anota.pack(pady=20)
                        self.botao_voltar_anotas = CTkButton(self.frame_anota, text="Voltar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=voltar_code, hover_color=ch)
                        self.botao_voltar_anotas.place(x=394, y=1)
                        self.tipo_nota = CTkOptionMenu(self.frame_anota, width=90, cursor="hand2", values=["Português", "Matemática", "História", "Geografia", "Ciências", "Inglês", "Programação", "Outros Estudos"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=muda_titulo)
                        self.tipo_nota.place(x=290, y=110)
                        self.tamanho_fonte = CTkOptionMenu(self.frame_anota, width=90, cursor="hand2", values=["8","10", "12", "14", "16", "18", "20", "22"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=fonte_tamanho)
                        self.tamanho_fonte.place(x=275, y=150)
                        self.tamanho_fonte.set("Tamanho Da Fonte...")
                        self.tipo_nota.set("Tipo De Notas...")
                        self.titulo = CTkEntry(self.frame_anota, width=222, placeholder_text="Título...", corner_radius=10, border_color=cbp, placeholder_text_color=cbp, text_color=ctt, fg_color=cf)
                        self.titulo.place(x=10, y=80)
                        self.texto = CTkTextbox(self.frame_anota, width=222, height=200, border_width=2, border_color=cbp, corner_radius=10, text_color=ctt, fg_color=cf)
                        self.texto.place(x=10, y=120)
                        self.texto.insert("0.0", "Hoje aprendi sobre...")
                        CTkToolTip(self.texto, message="Clique o botão direito do mouse", alpha=0.81, text_color=ctt, bg_color=cf)
                        self.texto.bind("<Button-3>", apaga_texto)
                        self.botao_salvar = CTkButton(self.frame_anota, text="Salvar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=salvar_texto, hover_color=ch)
                        self.botao_leitura = CTkButton(self.frame_anota, text="Ler", image=leitura, fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=ler, hover_color=ch)
                        self.botao_salvar.place(x=238, y=295)
                        self.botao_leitura.place(x=308, y=295)

                    elif escolha == "Código":
                        def voltar_code():
                            self.frame_codigo.pack_forget()
                            self.frame_codigos.place(x=20, y=0)
                        
                        def apaga_descricao(evento):
                            self.descricao.delete("0.0", END)
                        
                        def apaga_texto_codigo(evento):
                            self.texto_codigo.delete("0.0", END)

                        def fonte_tamanho_codigo(tamanho):
                            if tamanho == "8":
                                self.texto_codigo.configure(font=fonte_8)
                            elif tamanho == "10":
                                self.texto_codigo.configure(font=fonte_10)
                            elif tamanho == "12":
                                self.texto_codigo.configure(font=fonte_12)
                            elif tamanho == "14":
                                self.texto_codigo.configure(font=fonte_14)
                            elif tamanho == "16":
                                self.texto_codigo.configure(font=fonte_16)
                            elif tamanho == "18":
                                self.texto_codigo.configure(font=fonte_18)
                            elif tamanho == "20":
                                self.texto_codigo.configure(font=fonte_20)
                            elif tamanho == "22":
                                self.texto_codigo.configure(font=fonte_22)

                        def fonte_tamanho_descricao(tamanho):
                            if tamanho == "8":
                                self.descricao.configure(font=fonte_8)
                            elif tamanho == "10":
                                self.descricao.configure(font=fonte_10)
                            elif tamanho == "12":
                                self.descricao.configure(font=fonte_12)
                            elif tamanho == "14":
                                self.descricao.configure(font=fonte_14)
                            elif tamanho == "16":
                                self.descricao.configure(font=fonte_16)
                            elif tamanho == "18":
                                self.descricao.configure(font=fonte_18)
                            elif tamanho == "20":
                                self.descricao.configure(font=fonte_20)
                            elif tamanho == "22":
                                self.descricao.configure(font=fonte_22)
                            
                        def lang(lang_escolhida):
                            if lang_escolhida == "Python":
                                self.texto_codigo.configure(language="python")
                            elif lang_escolhida == "Zig":
                                self.texto_codigo.configure(language="zig")
                            elif lang_escolhida == "Javascript":
                                self.texto_codigo.configure(language="Javascript")
                            elif lang_escolhida == "C++":
                                self.texto_codigo.configure(language="c++")
                            elif lang_escolhida == "Lua":
                                self.texto_codigo.configure(language="lua")
                            elif lang_escolhida == "Rust":
                                self.texto_codigo.configure(language="rust")
                            elif lang_escolhida == "Java":
                                self.texto_codigo.configure(language="java")
                            elif lang_escolhida == "CSS":
                                self.texto_codigo.configure(language="css")
                            elif lang_escolhida == "HTML":
                                self.texto_codigo.configure(language="html")
                            elif lang_escolhida == "C#":
                                self.texto_codigo.configure(language="c#")
                            elif lang_escolhida == "PHP":
                                self.texto_codigo.configure(language="php")
                        
                        def tema(tema_escolhido):
                            if tema_escolhido == "Arduino":
                                self.texto_codigo.configure(theme="arduino")
                            elif tema_escolhido == "Abap":
                                self.texto_codigo.configure(theme="abap")
                            elif tema_escolhido == "Autumn":
                                self.texto_codigo.configure(theme="autumn")
                            elif tema_escolhido == "Borland":
                                self.texto_codigo.configure(theme="borland")
                            elif tema_escolhido == "Colorful":
                                self.texto_codigo.configure(theme="colorful")
                            elif tema_escolhido == "Default":
                                self.texto_codigo.configure(theme="default")
                            elif tema_escolhido == "Dracula":
                                self.texto_codigo.configure(theme="dracula")
                            elif tema_escolhido == "Emacs":
                                self.texto_codigo.configure(theme="emacs")
                            elif tema_escolhido == "Friendly":
                                self.texto_codigo.configure(theme="friendly")
                            elif tema_escolhido == "Fruit":
                                self.texto_codigo.configure(theme="fruit")
                            elif tema_escolhido == "Igor":
                                self.texto_codigo.configure(theme="igor")
                            elif tema_escolhido == "Inkpot":
                                self.texto_codigo.configure(theme="inkpot")
                            
                        def salvar_texto_codigo():
                            data_atual_codigo = time.strftime("%d/%m/%Y")
                            titulo_codigo = self.titulo_codigo.get().strip().capitalize()
                            descricao = self.descricao.get("1.0", "end").strip().capitalize()
                            codigo = self.texto_codigo.get("1.0", "end").strip()
                            fonte_codigo = self.fonte_tamanho_codigo.get()
                            fonte_descricao = self.fonte_tamanho_descricao.get()
                            tema = self.tema.get().lower()
                            linguagem = self.linguagem.get().lower()
                            data_c = data_atual_codigo
                            if fonte_codigo == "Tamanho Da Fonte...":
                                fonte_codigo = 12
                            if fonte_descricao == "Tamanho Da Fonte...":
                                fonte_descricao = 12
                            if tema == "seu tema favorito...":
                                tema = "arduino"
                            if linguagem == "sua linguagem favorita...":
                                linguagem = "python"
                            if len(titulo_codigo) >= 3 and len(titulo_codigo) < 30 and len(descricao) >= 3 and len(descricao) < 500 and len(codigo) >= 3:
                                guarda_codigos(titulo_codigo, descricao, fonte_descricao, data_c, codigo, fonte_codigo, tema, linguagem)
                                verificacao = verifica_guarda_codigo()
                                if verificacao == False:
                                    def tira_salvo():
                                        self.label_salvo.destroy()
                                        self.texto_codigo.delete("1.0", "end")
                                        self.titulo_codigo.delete(0, "end")
                                        self.descricao.delete("1.0", "end")
                                        self.fonte_tamanho_descricao.set("Tamanho Da Fonte...")
                                        self.fonte_tamanho_codigo.set("Tamanho Da Fonte...")
                                        self.tema.set("Seu Tema Favorito...")
                                        self.linguagem.set("Sua Linguagem Favorita...")
                                    self.label_salvo = CTkLabel(self.frame_codigo, text="Salvo com sucesso!!", text_color="#2E6F40", font=fonte_erros_inter, fg_color=pg)
                                    self.label_salvo.place(x=75, y=2)
                                    self.after(1400, tira_salvo)
                                else:
                                    def tira_erro_salvo():
                                        self.label_erro_salvo.destroy()
                                    self.label_erro_salvo = CTkLabel(self.frame_codigo, text="Não Salvou!!!", text_color="#E21010", font=fonte_erros_inter)
                                    self.label_salvo.place(x=75, y=2)
                                    self.after(1400, tira_erro_salvo)
                            elif len(titulo_codigo) < 3 or len(titulo_codigo) > 30:
                                def tira_erro():
                                    self.erro_titulo.destroy()
                                self.erro_titulo = CTkLabel(self.frame_codigo, text="Tamanho de título inválido (Min:3, Max:30)!!", text_color="#E21010", font=fonte_erros_inter)
                                self.erro_titulo.place(x=167, y=30)
                                self.after(1400, tira_erro)
                            elif len(descricao) < 3 or len(descricao) > 500:
                                def tira_erro():
                                    self.erro_nota.destroy()
                                self.erro_nota = CTkLabel(self.frame_codigo, text="Tamanho de descrição\n inválida (Min:3, Max:500)!!", text_color="#E21010", font=fonte_erros_inter)
                                self.erro_nota.place(x=245, y=30)
                                self.after(1400, tira_erro)
                            elif len(codigo) < 3:
                                def tira_erro():
                                    self.erro_nota.destroy()
                                self.erro_nota = CTkLabel(self.frame_codigo, text="Digite seu código!!", text_color="#E21010", font=fonte_erros_inter)
                                self.erro_nota.place(x=288, y=30)
                                self.after(1400, tira_erro)

                        def ler_descricao():
                            self.botao_leitura_codigos.configure(state=DISABLED)
                            def ler_texto():
                                titulo_codigo = self.titulo_codigo.get()
                                descricao = self.descricao.get("1.0", "end")
                                if len(titulo_codigo) > 3 and len(descricao) > 3 and pev == "Ativa":
                                    voz.say(titulo_codigo)
                                    voz.runAndWait()
                                    voz.setProperty('rate', 127)
                                    voz.say(descricao)
                                    voz.runAndWait()
                                elif len(titulo_codigo) < 3 or len(titulo_codigo) > 30:
                                    def tira_erro():
                                        self.erro_titulo.destroy()
                                    self.erro_titulo = CTkLabel(self.frame_codigo, text="Tamanho de título inválido (Min:3, Max:30)!!", text_color="#981212", font=fonte_erros_inter)
                                    self.erro_titulo.place(x=167, y=30)
                                    self.after(1400, tira_erro)
                                elif len(descricao) < 3 or len(descricao) > 500:
                                        def tira_erro():
                                            self.erro_nota.destroy()
                                        self.erro_nota = CTkLabel(self.frame_codigo, text="Tamanho de descrição inválida (Min:3, Max:500)!!", text_color="#981212", font=fonte_erros_inter)
                                        self.erro_nota.place(x=245, y=30)
                                        self.after(1400, tira_erro)
                                else:
                                    def tira_ativa_voz():
                                        self.label_ative_voz.destroy()
                                        self.botao_leitura_codigos.configure(state=NORMAL)
                                    self.label_ative_voz = CTkLabel(self.frame_codigo, text="Ative a Voz!", text_color="#E21010", font=fonte_erros_inter)
                                    self.label_ative_voz.place(x=170, y=2)
                                    self.botao_leitura_codigos.configure(state=DISABLED)
                                    self.after(1100, tira_ativa_voz)
                                self.botao_leitura_codigos.configure(state=NORMAL)
                            self.thread_ler_descricao = threading.Thread(target=ler_texto, daemon=True)
                            self.thread_ler_descricao.start()

                        def muda_titulo_codigo(evento):
                            self.titulo_codigo.configure(placeholder_text="Projeto, função de, conceito...")
        
                        self.frame_codigos.place_forget()    
                        self.frame_codigo = CTkFrame(self, width=470, height=360, fg_color=pg)
                        self.frame_codigo.pack(pady=20)
                        self.botao_voltar_codigo = CTkButton(self.frame_codigo, text="Voltar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=voltar_code, hover_color=ch)
                        self.botao_voltar_codigo.place(x=404, y=1)
                        self.fonte_tamanho_codigo = CTkOptionMenu(self.frame_codigo, width=90, cursor="hand2", values=["8","10", "12", "14", "16", "18", "20", "22"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=fonte_tamanho_codigo)
                        self.fonte_tamanho_codigo.place(x=4, y=25)
                        self.fonte_tamanho_codigo.set("Tamanho Da Fonte...")
                        self.texto_codigo = ccb.CTkCodeBox(self.frame_codigo, width=227, height=160, theme="arduino", language="python",fg_color=cf, border_width=2, border_color=cbp, corner_radius=10, numbering_color=cbp, menu=False)
                        self.texto_codigo.place(x=4, y=130)
                        self.texto_codigo.insert("0.0", ">Código...")
                        CTkToolTip(self.texto_codigo, message="Clique o botão direito do mouse", alpha=0.81, text_color=ctt, bg_color=cf)
                        self.texto_codigo.bind("<Button-3>", apaga_texto_codigo)
                        self.tema = CTkOptionMenu(self.frame_codigo, width=90, cursor="hand2", values=["Arduino","Abap", "Autumn", "Borland", "Colorful", "Default", "Dracula", "Emacs", "Friendly", "Fruity", "Igor", "Inkpot"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=tema)
                        self.tema.place(x=4, y=60)
                        self.tema.set("Seu Tema Favorito...")
                        self.linguagem = CTkOptionMenu(self.frame_codigo, width=90, cursor="hand2", values=["Python", "JavaScript", "Lua", "Rust", "CSS", "HTML", "Java", "C++", "PHP", "C#", "Zig"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=lang)
                        self.linguagem.place(x=4, y=95)
                        self.linguagem.set("Sua Linguagem Favorita...")
                        self.fonte_tamanho_descricao = CTkOptionMenu(self.frame_codigo, width=90, cursor="hand2", values=["8","10", "12", "14", "16", "18", "20", "22"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=fonte_tamanho_descricao)
                        self.fonte_tamanho_descricao.place(x=282, y=115)
                        self.fonte_tamanho_descricao.set("Tamanho Da Fonte...")
                        self.titulo_codigo = CTkEntry(self.frame_codigo, width=212, border_width=2, border_color=cbp, corner_radius=10, text_color=ctt, fg_color=cf, placeholder_text="Título...", placeholder_text_color=cbp)
                        self.titulo_codigo.place(x=258, y=70)
                        self.titulo_codigo.bind("<Enter>", muda_titulo_codigo)
                        self.descricao = CTkTextbox(self.frame_codigo, width=212, height=90, border_width=2, border_color=cbp, corner_radius=10, text_color=ctt, fg_color=cf)
                        self.descricao.place(x=258, y=150)
                        self.descricao.insert("0.0", "Esse código faz...")
                        CTkToolTip(self.descricao, message="Clique o botão direito do mouse", alpha=0.81, text_color=ctt, bg_color=cf)
                        self.descricao.bind("<Button-3>", apaga_descricao)
                        self.botao_salvar = CTkButton(self.frame_codigo, text="Salvar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=salvar_texto_codigo, hover_color=ch)
                        self.botao_leitura_codigos = CTkButton(self.frame_codigo, text="Ler", image=leitura, fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=ler_descricao, hover_color=ch)
                        self.botao_salvar.place(x=236, y=303)
                        self.botao_leitura_codigos.place(x=398, y=247)

                def buscar_codigo(evento):
                    langs = ["Python", "Javascript", "Lua", "Rust", "Css", "Html", "Java", "C++", "Php", "C#", "Zig"]
                    texto_busca = self.campo_busca_codigo.get().strip().capitalize()
                    if texto_busca in langs:
                        texto_busca = texto_busca.lower()
                        lista_codigo_buscar = busca_lang(texto_busca)
                    elif texto_busca not in langs:
                        lista_codigo_buscar = busca_titulo(texto_busca, "codigo")
                    if lista_codigo_buscar == True:
                        def tira_erro_busca():
                            erro_busca.destroy()
                        erro_busca = CTkLabel(self.frame_guarda_codigos, text="Código não encontrado", text_color="#E21010", font=fonte_erros_inter)
                        erro_busca.place(x=148, y=3)
                        self.after(1400, tira_erro_busca)
                    else:
                        def editar_codigo_busca(evento):
                            frame_anotacao_c.pack_forget()
                            self.frame_codigos.place_forget()
                            
                            def fonte_tamanho_codigo_e(tamanho_ec):
                                if tamanho_ec == "8":
                                    self.texto_codigo_ec.configure(font=fonte_8)
                                elif tamanho_ec == "10":
                                    self.texto_codigo_ec.configure(font=fonte_10)
                                elif tamanho_ec == "12":
                                    self.texto_codigo_ec.configure(font=fonte_12)
                                elif tamanho_ec == "14":
                                    self.texto_codigo_ec.configure(font=fonte_14)
                                elif tamanho_ec == "16":
                                    self.texto_codigo_ec.configure(font=fonte_16)
                                elif tamanho_ec == "18":
                                    self.texto_codigo_ec.configure(font=fonte_18)
                                elif tamanho_ec == "20":
                                    self.texto_codigo_ec.configure(font=fonte_20)
                                elif tamanho_ec == "22":
                                    self.texto_codigo_ec.configure(font=fonte_22)

                            def fonte_tamanho_descricao_e(tamanho_ec):
                                if tamanho_ec == "8":
                                    self.descricao_ec.configure(font=fonte_8)
                                elif tamanho_ec == "10":
                                    self.descricao_ec.configure(font=fonte_10)
                                elif tamanho_ec == "12":
                                    self.descricao_ec.configure(font=fonte_12)
                                elif tamanho_ec == "14":
                                    self.descricao_ec.configure(font=fonte_14)
                                elif tamanho_ec == "16":
                                    self.descricao_ec.configure(font=fonte_16)
                                elif tamanho_ec == "18":
                                    self.descricao_ec.configure(font=fonte_18)
                                elif tamanho_ec == "20":
                                    self.descricao.configure(font=fonte_20)
                                elif tamanho_ec == "22":
                                    self.descricao_ec.configure(font=fonte_22)

                            def lang_ec(lang_escolhida_ec):
                                if lang_escolhida_ec == "Python":
                                    self.texto_codigo_ec.configure(language="python")
                                elif lang_escolhida_ec == "Zig":
                                    self.texto_codigo_ec.configure(language="zig")
                                elif lang_escolhida_ec == "Javascript":
                                    self.texto_codigo_ec.configure(language="Javascript")
                                elif lang_escolhida_ec == "C++":
                                    self.texto_codigo_ec.configure(language="c++")
                                elif lang_escolhida_ec == "Lua":
                                    self.texto_codigo_ec.configure(language="lua")
                                elif lang_escolhida_ec == "Rust":
                                    self.texto_codigo_ec.configure(language="rust")
                                elif lang_escolhida_ec == "Java":
                                    self.texto_codigo_ec.configure(language="java")
                                elif lang_escolhida_ec == "CSS":
                                    self.texto_codigo_ec.configure(language="css")
                                elif lang_escolhida_ec == "HTML":
                                    self.texto_codigo_ec.configure(language="html")
                                elif lang_escolhida_ec == "C#":
                                    self.texto_codigo_ec.configure(language="c#")
                                elif lang_escolhida_ec == "PHP":
                                    self.texto_codigo_ec.configure(language="php")
                                
                            def tema_ec(tema_escolhido_ec):
                                if tema_escolhido_ec == "Arduino":
                                    self.texto_codigo_ec.configure(theme="arduino")
                                elif tema_escolhido_ec == "Abap":
                                    self.texto_codigo_ec.configure(theme="abap")
                                elif tema_escolhido_ec == "Autumn":
                                    self.texto_codigo_ec.configure(theme="autumn")
                                elif tema_escolhido_ec == "Borland":
                                    self.texto_codigo_ec.configure(theme="borland")
                                elif tema_escolhido_ec == "Colorful":
                                    self.texto_codigo_ec.configure(theme="colorful")
                                elif tema_escolhido_ec == "Default":
                                    self.texto_codigo_ec.configure(theme="default")
                                elif tema_escolhido_ec == "Dracula":
                                    self.texto_codigo_ec.configure(theme="dracula")
                                elif tema_escolhido_ec == "Emacs":
                                    self.texto_codigo_ec.configure(theme="emacs")
                                elif tema_escolhido_ec == "Friendly":
                                    self.texto_codigo_ec.configure(theme="friendly")
                                elif tema_escolhido_ec == "Fruit":
                                    self.texto_codigo_ec.configure(theme="fruit")
                                elif tema_escolhido_ec == "Igor":
                                    self.texto_codigo_ec.configure(theme="igor")
                                elif tema_escolhido_ec == "Inkpot":
                                    self.texto_codigo_ec.configure(theme="inkpot")

                            def muda_titulo_codigo_e(evento):
                                self.titulo_ec.configure(placeholder_text="Projeto, função de, conceito...")

                            def deletar():
                                deletou = deletar_nota(identidade_frame_c)
                                def tira_del():
                                    self.frame_edita.destroy()
                                    self.frame_codigos.place(x=20, y=0)
                                            
                                if deletou == True:
                                    self.label_del = CTkLabel(self.frame_edita_c, text="Deletado Com Sucesso!!", text_color="#E21010", font=fonte_erros_inter)
                                    self.label_del.place(x=210, y=5)
                                    self.after(1000, tira_del)
                                else:
                                    self.label_del = CTkLabel(self.frame_edita_c, text="Erro ao deletar!!!", text_color="#E21010", font=fonte_erros_inter)
                                    self.label_del.place(x=210, y=5)

                            def salvar_texto_codigo_e():
                                data_atual_codigo_e = time.strftime("%d/%m/%Y")
                                id = identidade_frame_c
                                titulo_codigo_e = self.titulo_ec.get().strip().capitalize()
                                descricao_e = self.descricao_ec.get("1.0", "end").strip().capitalize()
                                codigo_e = self.texto_codigo_ec.get("1.0", "end").strip()
                                fonte_codigo_e = self.fonte_tamanho_codigo_ec.get()
                                fonte_descricao_ec = self.fonte_tamanho_descricao_ec.get()
                                tema_e = self.tema_ec.get().lower()
                                linguagem_e = self.linguagem_ec.get().lower()
                                data_ec = data_atual_codigo_e
                                if fonte_codigo_e == "Tamanho Da Fonte...":
                                    fonte_codigo_e = 12
                                if fonte_descricao_ec == "Tamanho Da Fonte...":
                                    fonte_descricao_ec = 12
                                if tema_e == "seu tema favorito...":
                                    tema_e = "arduino"
                                if linguagem_e == "sua linguagem favorita...":
                                    linguagem_e = "python"
                                if len(titulo_codigo_e) >= 3 and len(titulo_codigo_e) < 30 and len(descricao_e) >= 3 and len(descricao_e) < 500 and len(codigo_e) >= 3:
                                    salvando_codigo = salvar_edicao_codigo(titulo_codigo_e, id, descricao_e, fonte_descricao_ec, data_ec, codigo_e, fonte_codigo_e, tema_e, linguagem_e)
                                    if salvando_codigo == True:
                                        def tira_salvo_ec():
                                            self.label_salvo_ec.destroy()
                                        self.label_salvo_ec = CTkLabel(self.frame_edita_c, text="Salvo com sucesso!!", text_color="#2E6F40",font=fonte_erros_inter, fg_color=pg)
                                        self.label_salvo_ec.place(x=95, y=2)
                                        self.after(1400, tira_salvo_ec)
                                elif len(titulo_codigo_e) < 3 or len(titulo_codigo_e) > 30:
                                    def tira_erro():
                                        self.erro_titulo.destroy()
                                    self.erro_titulo = CTkLabel(self.frame_edita_c, text="Tamanho de título inválido (Min:3, Max:30)!!", text_color="#E21010", font=fonte_erros_inter)
                                    self.erro_titulo.place(x=167, y=30)
                                    self.after(1400, tira_erro)
                                elif len(descricao_e) < 3 or len(descricao_e) > 500:
                                    def tira_erro():
                                        self.erro_nota.destroy()
                                    self.erro_nota = CTkLabel(self.frame_edita_c, text="Tamanho de descrição inválida (Min:3, Max:500)!!", text_color="#E21010", font=fonte_erros_inter)
                                    self.erro_nota.place(x=245, y=30)
                                    self.after(1400, tira_erro)
                                elif len(codigo_e) < 3:
                                    def tira_erro():
                                        self.erro_nota.destroy()
                                    self.erro_nota = CTkLabel(self.frame_edita_c, text="Digite seu código!!", text_color="#E21010",font=fonte_erros_inter)
                                    self.erro_nota.place(x=288, y=30)
                                    self.after(1400, tira_erro)
                            
                            def ler_ec():
                                self.botao_leitura_ec.configure(state=DISABLED)
                                def ler_titulo_ec():
                                    titulo_ec = self.titulo_ec.get()
                                    texto_ec = self.descricao_ec.get("1.0", "end")
                                    if len(titulo_ec) >= 3 and len(texto_ec) >= 3 and pev == "Ativa":
                                        voz.say(titulo_ec)
                                        voz.runAndWait()
                                        voz.setProperty('rate', 127)
                                        voz.say(texto_ec)
                                        voz.runAndWait()
                                    elif len(titulo_ec) < 3 or len(titulo_ec) > 30:
                                        def tira_erro_ec():
                                            self.erro_titulo_ec.destroy()
                                        self.erro_titulo_ec = CTkLabel(self.frame_edita_c, text="Tamanho de título inválido (Min:3, Max:30)!!", text_color="#981212", font=fonte_erros_inter)
                                        self.erro_titulo_ec.place(x=167, y=30)
                                        self.after(1400, tira_erro_ec)
                                    elif len(texto_ec) < 3 or len(texto_ec) > 500:
                                        def tira_erro_ec():
                                            self.erro_nota_ec.destroy()
                                        self.erro_nota_ec = CTkLabel(self.frame_edita_c, text="Tamanho de nota inválido (Min:3, Max:500)!!", text_color="#981212", font=fonte_erros_inter)
                                        self.erro_nota_ec.place(x=245, y=30)
                                        self.after(1400, tira_erro_ec)
                                    else:
                                        def tira_ativa_voz_ec():
                                            self.label_ative_voz_ec.destroy()
                                        self.label_ative_voz_ec = CTkLabel(self.frame_edita_c, text="Ative a Voz!", text_color="#E21010", font=fonte_erros_inter)
                                        self.label_ative_voz_ec.place(x=170, y=5)
                                        self.botao_leitura_ec.configure(state=DISABLED)
                                        self.after(1100, tira_ativa_voz_ec)
                                self.botao_leitura_ec.configure(state=NORMAL)
                                self.thread_ler_titulo_ec = threading.Thread(target=ler_titulo_ec, daemon=True)
                                self.thread_ler_titulo_ec.start()
                                        
                            def voltar_anotacao():
                                self.frame_edita_c.pack_forget()
                                self.titulo_ec.delete(0, "end")
                                self.texto_codigo_ec.delete(0.0, "end")
                                self.fonte_tamanho_descricao_ec.destroy()
                                self.fonte_tamanho_codigo_ec.destroy()
                                self.frame_codigos.place(x=20, y=0)
                                frame_anotacao_c.pack(pady=5, fill="x")

                            id_frame = evento.widget
                            while not hasattr(id_frame, "titulo_c"):
                                id_frame = id_frame.master
                            titulo_c = id_frame
                            titulo_frame_c = titulo_c.titulo_c
                            texto_frame_c = titulo_c.texto_c
                            identidade_frame_c = titulo_c.ID
                            fonte_descricao_frame_c = titulo_c.fonte_descricao
                            fonte_codigo_frame_c = titulo_c.fonte_codigo
                            codigo_frame = titulo_c.codigo
                            tema_frame = titulo_c.tema
                            linguagem_frame = titulo_c.linguagem
                            #Fonte da parte de salvar notas
                            fonte_descricao_ec = CTkFont(family="Arial", size=fonte_descricao_frame_c)
                            fonte_codigo_ec = CTkFont(family="Arial", size=fonte_codigo_frame_c)
                            self.frame_edita_c = CTkFrame(self, width=470, height=350, fg_color=pg)
                            self.frame_edita_c.pack(pady=20)
                            self.fonte_tamanho_descricao_ec = CTkOptionMenu(self.frame_edita_c, width=90, cursor="hand2", values=["8","10", "12", "14", "16", "18", "20", "22"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=fonte_tamanho_descricao_e)
                            self.fonte_tamanho_codigo_ec = CTkOptionMenu(self.frame_edita_c, width=90, cursor="hand2", values=["8","10", "12", "14", "16", "18", "20", "22"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=fonte_tamanho_codigo_e)
                            self.tema_ec = CTkOptionMenu(self.frame_edita_c, width=90, cursor="hand2", values=["Arduino","Abap", "Autumn", "Borland", "Colorful", "Default", "Dracula", "Emacs", "Friendly", "Fruity", "Igor", "Inkpot"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=tema_ec)
                            self.tema_ec.set(tema_frame.capitalize())
                            self.linguagem_ec = CTkOptionMenu(self.frame_edita_c, width=90, cursor="hand2", values=["Python", "JavaScript", "Lua", "Rust", "CSS", "HTML", "Java", "C++", "PHP", "C#", "Zig"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=lang_ec)
                            self.linguagem_ec.set(linguagem_frame.capitalize())
                            self.titulo_ec = CTkEntry(self.frame_edita_c, width=212, corner_radius=10, border_color=cbp, placeholder_text_color=cbp, text_color=ct, fg_color=cf)
                            self.titulo_ec.bind("<Enter>", muda_titulo_codigo_e)
                            self.texto_codigo_ec = ccb.CTkCodeBox(self.frame_edita_c, width=227, height=150, theme=tema_frame, language=linguagem_frame,fg_color=cf, border_width=2, border_color=cbp, corner_radius=10, numbering_color=cbp, menu=False, font=fonte_codigo_ec)
                            self.descricao_ec = CTkTextbox(self.frame_edita_c, width=212, height=90, border_width=2, border_color=cbp, corner_radius=10, text_color=ct, fg_color=cf, font=fonte_descricao_ec)
                            self.botao_deletar_ec = CTkButton(self.frame_edita_c, text="Deletar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=deletar, hover_color=ch)
                            self.botao_salvar_ec = CTkButton(self.frame_edita_c, text="Salvar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=salvar_texto_codigo_e, hover_color=ch)
                            self.botao_leitura_ec = CTkButton(self.frame_edita_c, text="Ler", image=leitura, fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=ler_ec, hover_color=ch)
                            self.botao_voltar_ec = CTkButton(self.frame_edita_c, text="Voltar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=voltar_anotacao, hover_color=ch)
                            self.texto_codigo_ec.insert("0.0", codigo_frame)
                            self.descricao_ec.insert("0.0", texto_frame_c)
                            self.titulo_ec.insert(0, titulo_frame_c)
                            self.fonte_tamanho_descricao_ec.set(fonte_descricao_frame_c)
                            self.fonte_tamanho_codigo_ec.set(fonte_codigo_frame_c)
                            self.titulo_ec.place(x=257, y=90)
                            self.texto_codigo_ec.place(x=4, y=140)
                            self.descricao_ec.place(x=258, y=130)
                            self.botao_voltar_ec.place(x=1, y=1) 
                            self.fonte_tamanho_descricao_ec.place(x=310, y=55)
                            self.fonte_tamanho_codigo_ec.place(x=4, y=30)
                            self.tema_ec.place(x=4, y=65)
                            self.linguagem_ec.place(x=4, y=100)
                            self.botao_salvar_ec.place(x=236, y=303)
                            self.botao_deletar_ec.place(x=298, y=303)
                            self.botao_leitura_ec.place(x=398, y=227)
                        lista_codigos = self.frame_codigos.winfo_children()
                        for lc in lista_codigos:
                            lc.destroy()
                        
                        self.frame_notas.place_forget()
                        self.frame_codigos = CTkScrollableFrame(self, width=440, height=330, fg_color=pg)
                        self.frame_codigos.place(x=20, y=0)
                        self.frame_guarda_codigos = CTkFrame(self.frame_codigos, width=440, height=68, fg_color=pg)
                        self.frame_guarda_codigos.pack(pady=10)
                        self.aba_nota = CTkButton(self.frame_guarda_codigos, text="Notas", fg_color=pg, width=4, height=22, cursor="hand2", corner_radius=23, command=muda_aba_nota_c)
                        self.aba_nota.place(x=4, y=1)
                        self.aba_codigo = CTkButton(self.frame_guarda_codigos, text="Códigos", fg_color=pg, width=4, height=22, cursor="hand2", corner_radius=23, command=muda_aba_codigo)
                        self.aba_codigo.place(x=66, y=1)
                        self.botao_voltar_codigos = CTkButton(self.frame_guarda_codigos, text="Voltar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=voltar_codigos, hover_color=ch)
                        self.botao_voltar_codigos.place(x=365, y=1)
                        self.botao_cria_nota = CTkOptionMenu(self.frame_guarda_codigos, values=["Nota", "Código"], fg_color=cls, height=25, cursor="hand2", corner_radius=19, button_color=cls, text_color=ctb, button_hover_color=ch,dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=escolha_comecar_codigo)
                        self.botao_cria_nota.set("Começar...")
                        self.botao_cria_nota.place(x=2, y=33)
                        self.campo_busca_codigo = CTkEntry(master=self.frame_guarda_codigos, width=162, corner_radius=10, border_color=cbp, placeholder_text_color=cbp, text_color=ct, fg_color=cf, placeholder_text="Busque por...")
                        self.campo_busca_codigo.place(x=260, y=31)
                        CTkToolTip(self.campo_busca_codigo, message="Clique a tecla ENTER", alpha=0.81, text_color=ctt, bg_color=cf)
                        self.campo_busca_codigo.bind("<Return>", buscar_codigo)
                        def entrou_campo_busca_codigo(evento):
                            self.campo_busca_codigo.configure(placeholder_text="Título, lang...")
                        self.campo_busca_codigo.bind("<Enter>", entrou_campo_busca_codigo)
                        def saiu_campo_busca_codigo(evento):
                            self.focus_set()
                            self.campo_busca_codigo.configure(placeholder_text="Buscar por...")
                        self.campo_busca_codigo.bind("<Leave>", saiu_campo_busca_codigo)

                        for lcb in lista_codigo_buscar:
                            id = lcb[0]
                            titulo_bc = lcb[1]
                            texto_bc = lcb[2]
                            linguagem_bc = lcb[6]
                            if len(texto_bc) > 34:
                                if texto_bc[33] == ",":
                                    texto_bc = texto_bc[0:33] + "..."
                                else:
                                    texto_bc = texto_bc[0:34] + "..."
                            else:
                                texto_bc = texto_bc[0:34]
                            frame_anotacao_cb = CTkFrame(self.frame_codigos, width=180, height=110, corner_radius=15, cursor="hand2", fg_color=cn)
                            frame_anotacao_cb.ID = lcb[0] #Atribuindo o atributo ID aos frames, cada qual com seu id
                            frame_anotacao_cb.titulo = lcb[1]
                            frame_anotacao_cb.texto = lcb[2]
                            frame_anotacao_cb.fonte = lcb[4]
                            label_titulo_cb = CTkLabel(frame_anotacao_cb, text=titulo_bc, text_color=ct)
                            label_texto_cb = CTkLabel(frame_anotacao_cb, text=texto_bc, text_color=ct)
                            label_linguagem_cb = CTkLabel(frame_anotacao_cb, text=linguagem_bc, text_color=ct)
                            frame_anotacao_cb.pack(pady=10, fill="x")
                            label_titulo_cb.pack(pady=5)
                            if linguagem != "sua linguagem favorita...":
                                label_linguagem_cb.pack(pady=1)
                            label_texto_cb.pack(pady=1)
                            frame_anotacao_cb.bind("<Button-1>", editar_codigo_busca)


                def editar_codigo(evento):
                    frame_anotacao_c.pack_forget()
                    self.frame_codigos.place_forget()
                    
                    def fonte_tamanho_codigo_e(tamanho_ec):
                        if tamanho_ec == "8":
                            self.texto_codigo_ec.configure(font=fonte_8)
                        elif tamanho_ec == "10":
                            self.texto_codigo_ec.configure(font=fonte_10)
                        elif tamanho_ec == "12":
                            self.texto_codigo_ec.configure(font=fonte_12)
                        elif tamanho_ec == "14":
                            self.texto_codigo_ec.configure(font=fonte_14)
                        elif tamanho_ec == "16":
                            self.texto_codigo_ec.configure(font=fonte_16)
                        elif tamanho_ec == "18":
                            self.texto_codigo_ec.configure(font=fonte_18)
                        elif tamanho_ec == "20":
                            self.texto_codigo_ec.configure(font=fonte_20)
                        elif tamanho_ec == "22":
                            self.texto_codigo_ec.configure(font=fonte_22)

                    def fonte_tamanho_descricao_e(tamanho_ec):
                        if tamanho_ec == "8":
                            self.descricao_ec.configure(font=fonte_8)
                        elif tamanho_ec == "10":
                            self.descricao_ec.configure(font=fonte_10)
                        elif tamanho_ec == "12":
                            self.descricao_ec.configure(font=fonte_12)
                        elif tamanho_ec == "14":
                            self.descricao_ec.configure(font=fonte_14)
                        elif tamanho_ec == "16":
                            self.descricao_ec.configure(font=fonte_16)
                        elif tamanho_ec == "18":
                            self.descricao_ec.configure(font=fonte_18)
                        elif tamanho_ec == "20":
                            self.descricao.configure(font=fonte_20)
                        elif tamanho_ec == "22":
                            self.descricao_ec.configure(font=fonte_22)

                    def lang_ec(lang_escolhida_ec):
                        if lang_escolhida_ec == "Python":
                            self.texto_codigo_ec.configure(language="python")
                        elif lang_escolhida_ec == "Zig":
                            self.texto_codigo_ec.configure(language="zig")
                        elif lang_escolhida_ec == "Javascript":
                            self.texto_codigo_ec.configure(language="Javascript")
                        elif lang_escolhida_ec == "C++":
                            self.texto_codigo_ec.configure(language="c++")
                        elif lang_escolhida_ec == "Lua":
                            self.texto_codigo_ec.configure(language="lua")
                        elif lang_escolhida_ec == "Rust":
                            self.texto_codigo_ec.configure(language="rust")
                        elif lang_escolhida_ec == "Java":
                            self.texto_codigo_ec.configure(language="java")
                        elif lang_escolhida_ec == "CSS":
                            self.texto_codigo_ec.configure(language="css")
                        elif lang_escolhida_ec == "HTML":
                            self.texto_codigo_ec.configure(language="html")
                        elif lang_escolhida_ec == "C#":
                            self.texto_codigo_ec.configure(language="c#")
                        elif lang_escolhida_ec == "PHP":
                            self.texto_codigo_ec.configure(language="php")
                        
                    def tema_ec(tema_escolhido_ec):
                        if tema_escolhido_ec == "Arduino":
                            self.texto_codigo_ec.configure(theme="arduino")
                        elif tema_escolhido_ec == "Abap":
                            self.texto_codigo_ec.configure(theme="abap")
                        elif tema_escolhido_ec == "Autumn":
                            self.texto_codigo_ec.configure(theme="autumn")
                        elif tema_escolhido_ec == "Borland":
                            self.texto_codigo_ec.configure(theme="borland")
                        elif tema_escolhido_ec == "Colorful":
                            self.texto_codigo_ec.configure(theme="colorful")
                        elif tema_escolhido_ec == "Default":
                            self.texto_codigo_ec.configure(theme="default")
                        elif tema_escolhido_ec == "Dracula":
                            self.texto_codigo_ec.configure(theme="dracula")
                        elif tema_escolhido_ec == "Emacs":
                            self.texto_codigo_ec.configure(theme="emacs")
                        elif tema_escolhido_ec == "Friendly":
                            self.texto_codigo_ec.configure(theme="friendly")
                        elif tema_escolhido_ec == "Fruit":
                            self.texto_codigo_ec.configure(theme="fruit")
                        elif tema_escolhido_ec == "Igor":
                            self.texto_codigo_ec.configure(theme="igor")
                        elif tema_escolhido_ec == "Inkpot":
                            self.texto_codigo_ec.configure(theme="inkpot")

                    def muda_titulo_codigo_e(evento):
                        self.titulo_ec.configure(placeholder_text="Projeto, função de, conceito...")

                    def deletar():
                        deletou = deletar_nota(identidade_frame_c)
                        def tira_del():
                            self.frame_edita.destroy()
                            self.frame_codigos.place(x=20, y=0)
                                    
                        if deletou == True:
                            self.label_del = CTkLabel(self.frame_edita_c, text="Deletado Com Sucesso!!", text_color="#E21010", font=fonte_erros_inter)
                            self.label_del.place(x=210, y=5)
                            self.after(1000, tira_del)
                        else:
                            self.label_del = CTkLabel(self.frame_edita_c, text="Erro ao deletar!!!", text_color="#E21010", font=fonte_erros_inter)
                            self.label_del.place(x=210, y=5)

                    def salvar_texto_codigo_e():
                        data_atual_codigo_e = time.strftime("%d/%m/%Y")
                        id = identidade_frame_c
                        titulo_codigo_e = self.titulo_ec.get().strip().capitalize()
                        descricao_e = self.descricao_ec.get("1.0", "end").strip().capitalize()
                        codigo_e = self.texto_codigo_ec.get("1.0", "end").strip()
                        fonte_codigo_e = self.fonte_tamanho_codigo_ec.get()
                        fonte_descricao_ec = self.fonte_tamanho_descricao_ec.get()
                        tema_e = self.tema_ec.get().lower()
                        linguagem_e = self.linguagem_ec.get().lower()
                        data_ec = data_atual_codigo_e
                        if fonte_codigo_e == "Tamanho Da Fonte...":
                            fonte_codigo_e = 12
                        if fonte_descricao_ec == "Tamanho Da Fonte...":
                            fonte_descricao_ec = 12
                        if tema_e == "seu tema favorito...":
                            tema_e = "arduino"
                        if linguagem_e == "sua linguagem favorita...":
                            linguagem_e = "python"
                        if len(titulo_codigo_e) >= 3 and len(titulo_codigo_e) < 30 and len(descricao_e) >= 3 and len(descricao_e) < 500 and len(codigo_e) >= 3:
                            salvando_codigo = salvar_edicao_codigo(titulo_codigo_e, id, descricao_e, fonte_descricao_ec, data_ec, codigo_e, fonte_codigo_e, tema_e, linguagem_e)
                            if salvando_codigo == True:
                                def tira_salvo_ec():
                                    self.label_salvo_ec.destroy()
                                self.label_salvo_ec = CTkLabel(self.frame_edita_c, text="Salvo com sucesso!!", text_color="#2E6F40",font=fonte_erros_inter, fg_color=pg)
                                self.label_salvo_ec.place(x=95, y=2)
                                self.after(1400, tira_salvo_ec)
                        elif len(titulo_codigo_e) < 3 or len(titulo_codigo_e) > 30:
                            def tira_erro():
                                self.erro_titulo.destroy()
                            self.erro_titulo = CTkLabel(self.frame_edita_c, text="Tamanho de título inválido (Min:3, Max:30)!!", text_color="#E21010", font=fonte_erros_inter)
                            self.erro_titulo.place(x=167, y=30)
                            self.after(1400, tira_erro)
                        elif len(descricao_e) < 3 or len(descricao_e) > 500:
                            def tira_erro():
                                self.erro_nota.destroy()
                            self.erro_nota = CTkLabel(self.frame_edita_c, text="Tamanho de descrição inválida (Min:3, Max:500)!!", text_color="#E21010", font=fonte_erros_inter)
                            self.erro_nota.place(x=245, y=30)
                            self.after(1400, tira_erro)
                        elif len(codigo_e) < 3:
                            def tira_erro():
                                self.erro_nota.destroy()
                            self.erro_nota = CTkLabel(self.frame_edita_c, text="Digite seu código!!", text_color="#E21010",font=fonte_erros_inter)
                            self.erro_nota.place(x=288, y=30)
                            self.after(1400, tira_erro)
                    
                    def ler_ec():
                        self.botao_leitura_ec.configure(state=DISABLED)
                        def ler_titulo_ec():
                            titulo_ec = self.titulo_ec.get()
                            texto_ec = self.descricao_ec.get("1.0", "end")
                            if len(titulo_ec) >= 3 and len(texto_ec) >= 3 and pev == "Ativa":
                                voz.say(titulo_ec)
                                voz.runAndWait()
                                voz.setProperty('rate', 127)
                                voz.say(texto_ec)
                                voz.runAndWait()
                            elif len(titulo_ec) < 3 or len(titulo_ec) > 30:
                                def tira_erro_ec():
                                    self.erro_titulo_ec.destroy()
                                self.erro_titulo_ec = CTkLabel(self.frame_edita_c, text="Tamanho de título inválido (Min:3, Max:30)!!", text_color="#981212", font=fonte_erros_inter)
                                self.erro_titulo_ec.place(x=167, y=30)
                                self.after(1400, tira_erro_ec)
                            elif len(texto_ec) < 3 or len(texto_ec) > 500:
                                def tira_erro_ec():
                                    self.erro_nota_ec.destroy()
                                self.erro_nota_ec = CTkLabel(self.frame_edita_c, text="Tamanho de nota inválido (Min:3, Max:500)!!", text_color="#981212", font=fonte_erros_inter)
                                self.erro_nota_ec.place(x=245, y=30)
                                self.after(1400, tira_erro_ec)
                            else:
                                def tira_ativa_voz_ec():
                                    self.label_ative_voz_ec.destroy()
                                self.label_ative_voz_ec = CTkLabel(self.frame_edita_c, text="Ative a Voz!", text_color="#E21010", font=fonte_erros_inter)
                                self.label_ative_voz_ec.place(x=170, y=5)
                                self.botao_leitura_ec.configure(state=DISABLED)
                                self.after(1100, tira_ativa_voz_ec)
                        self.botao_leitura_ec.configure(state=NORMAL)
                        self.thread_ler_titulo_ec = threading.Thread(target=ler_titulo_ec, daemon=True)
                        self.thread_ler_titulo_ec.start()
                                
                    def voltar_anotacao():
                        self.frame_edita_c.pack_forget()
                        self.titulo_ec.delete(0, "end")
                        self.texto_codigo_ec.delete(0.0, "end")
                        self.fonte_tamanho_descricao_ec.destroy()
                        self.fonte_tamanho_codigo_ec.destroy()
                        self.frame_codigos.place(x=20, y=0)
                        frame_anotacao_c.pack(pady=5, fill="x")

                    id_frame = evento.widget
                    while not hasattr(id_frame, "titulo_c"):
                        id_frame = id_frame.master
                    titulo_c = id_frame
                    titulo_frame_c = titulo_c.titulo_c
                    texto_frame_c = titulo_c.texto_c
                    identidade_frame_c = titulo_c.ID
                    fonte_descricao_frame_c = titulo_c.fonte_descricao
                    fonte_codigo_frame_c = titulo_c.fonte_codigo
                    codigo_frame = titulo_c.codigo
                    tema_frame = titulo_c.tema
                    linguagem_frame = titulo_c.linguagem
                    #Fonte da parte de salvar notas
                    fonte_descricao_ec = CTkFont(family="Arial", size=fonte_descricao_frame_c)
                    fonte_codigo_ec = CTkFont(family="Arial", size=fonte_codigo_frame_c)
                    self.frame_edita_c = CTkFrame(self, width=470, height=350, fg_color=pg)
                    self.frame_edita_c.pack(pady=20)
                    self.fonte_tamanho_descricao_ec = CTkOptionMenu(self.frame_edita_c, width=90, cursor="hand2", values=["8","10", "12", "14", "16", "18", "20", "22"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=fonte_tamanho_descricao_e)
                    self.fonte_tamanho_codigo_ec = CTkOptionMenu(self.frame_edita_c, width=90, cursor="hand2", values=["8","10", "12", "14", "16", "18", "20", "22"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=fonte_tamanho_codigo_e)
                    self.tema_ec = CTkOptionMenu(self.frame_edita_c, width=90, cursor="hand2", values=["Arduino","Abap", "Autumn", "Borland", "Colorful", "Default", "Dracula", "Emacs", "Friendly", "Fruity", "Igor", "Inkpot"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=tema_ec)
                    self.tema_ec.set(tema_frame.capitalize())
                    self.linguagem_ec = CTkOptionMenu(self.frame_edita_c, width=90, cursor="hand2", values=["Python", "JavaScript", "Lua", "Rust", "CSS", "HTML", "Java", "C++", "PHP", "C#", "Zig"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=lang_ec)
                    self.linguagem_ec.set(linguagem_frame.capitalize())
                    self.titulo_ec = CTkEntry(self.frame_edita_c, width=212, corner_radius=10, border_color=cbp, placeholder_text_color=cbp, text_color=ct, fg_color=cf)
                    self.titulo_ec.bind("<Enter>", muda_titulo_codigo_e)
                    self.texto_codigo_ec = ccb.CTkCodeBox(self.frame_edita_c, width=227, height=150, theme=tema_frame, language=linguagem_frame,fg_color=cf, border_width=2, border_color=cbp, corner_radius=10, numbering_color=cbp, menu=False, font=fonte_codigo_ec)
                    self.descricao_ec = CTkTextbox(self.frame_edita_c, width=212, height=90, border_width=2, border_color=cbp, corner_radius=10, text_color=ct, fg_color=cf, font=fonte_descricao_ec)
                    self.botao_deletar_ec = CTkButton(self.frame_edita_c, text="Deletar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=deletar, hover_color=ch)
                    self.botao_salvar_ec = CTkButton(self.frame_edita_c, text="Salvar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=salvar_texto_codigo_e, hover_color=ch)
                    self.botao_leitura_ec = CTkButton(self.frame_edita_c, text="Ler", image=leitura, fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=ler_ec, hover_color=ch)
                    self.botao_voltar_ec = CTkButton(self.frame_edita_c, text="Voltar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=voltar_anotacao, hover_color=ch)
                    self.texto_codigo_ec.insert("0.0", codigo_frame)
                    self.descricao_ec.insert("0.0", texto_frame_c)
                    self.titulo_ec.insert(0, titulo_frame_c)
                    self.fonte_tamanho_descricao_ec.set(fonte_descricao_frame_c)
                    self.fonte_tamanho_codigo_ec.set(fonte_codigo_frame_c)
                    self.titulo_ec.place(x=257, y=90)
                    self.texto_codigo_ec.place(x=4, y=140)
                    self.descricao_ec.place(x=258, y=130)
                    self.botao_voltar_ec.place(x=1, y=1) 
                    self.fonte_tamanho_descricao_ec.place(x=310, y=55)
                    self.fonte_tamanho_codigo_ec.place(x=4, y=30)
                    self.tema_ec.place(x=4, y=65)
                    self.linguagem_ec.place(x=4, y=100)
                    self.botao_salvar_ec.place(x=236, y=303)
                    self.botao_deletar_ec.place(x=298, y=303)
                    self.botao_leitura_ec.place(x=398, y=227)

                self.frame_notas.place_forget()
                self.frame_codigos = CTkScrollableFrame(self, width=440, height=330, fg_color=pg)
                self.frame_codigos.place(x=20, y=0)
                self.frame_guarda_codigos = CTkFrame(self.frame_codigos, width=440, height=68, fg_color=pg)
                self.frame_guarda_codigos.pack(pady=10)
                self.aba_nota = CTkButton(self.frame_guarda_codigos, text="Notas", fg_color=pg, width=4, height=22, cursor="hand2", corner_radius=23, command=muda_aba_nota_c, text_color=ct)
                self.aba_nota.place(x=4, y=1)
                self.aba_codigo = CTkButton(self.frame_guarda_codigos, text="Códigos", fg_color=pg, width=4, height=22, cursor="hand2", corner_radius=23, command=muda_aba_codigo, text_color=ct)
                self.aba_codigo.place(x=66, y=1)
                self.aba_codigo.configure(state=DISABLED)
                self.botao_voltar_codigos = CTkButton(self.frame_guarda_codigos, text="Voltar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=voltar_codigos, hover_color=ch)
                self.botao_voltar_codigos.place(x=365, y=1)
                self.botao_cria_nota = CTkOptionMenu(self.frame_guarda_codigos, values=["Nota", "Código"], fg_color=cls, height=25, cursor="hand2", corner_radius=19, button_color=cls, text_color=ctb, button_hover_color=ch,dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=escolha_comecar_codigo)
                self.botao_cria_nota.set("Começar...")
                self.botao_cria_nota.place(x=2, y=33)
                self.campo_busca_codigo = CTkEntry(master=self.frame_guarda_codigos, width=162, corner_radius=10, border_color=cbp, placeholder_text_color=cbp, text_color=ct, fg_color=cf, placeholder_text="Busque por...")
                self.campo_busca_codigo.place(x=260, y=31)
                CTkToolTip(self.campo_busca_codigo, message="Clique a tecla ENTER", alpha=0.81, text_color=ctt, bg_color=cf)
                self.campo_busca_codigo.bind("<Return>", buscar_codigo)
                def entrou_campo_busca_codigo(evento):
                    self.campo_busca_codigo.configure(placeholder_text="Título, lang...")
                self.campo_busca_codigo.bind("<Enter>", entrou_campo_busca_codigo) 
                def saiu_campo_busca_codigo(evento):
                    self.focus_set()
                    self.campo_busca_codigo.configure(placeholder_text="Busque por...")
                self.campo_busca_codigo.bind("<Leave>", saiu_campo_busca_codigo)

                #Pega os codigos
                self.lista_codigo = pega_codigos()
                #Percorre a lista de codigos e posiciona os frames com eles.
                for lc in self.lista_codigo:
                    titulo_c = lc[1]
                    texto_c = lc[2]
                    linguagem = lc[6]
                    if len(texto_c) > 34:
                        if texto_c[33] == ",":
                            texto_c = texto_c[0:33] + "..."
                        else:
                            texto_c = texto_c[0:34] + "..."
                    else:
                        texto_c = texto_c[0:34]
                    frame_anotacao_c = CTkFrame(self.frame_codigos, width=180, height=120, corner_radius=15, cursor="hand2", fg_color=cn)
                    frame_anotacao_c.ID = lc[0] #Atribuindo o atributo ID aos frames, cada qual com seu id
                    frame_anotacao_c.titulo_c = lc[1]
                    frame_anotacao_c.texto_c = lc[2]
                    frame_anotacao_c.fonte_descricao = lc[3]
                    frame_anotacao_c.codigo = lc[4]
                    frame_anotacao_c.tema = lc[5]
                    frame_anotacao_c.linguagem = lc[6]
                    frame_anotacao_c.fonte_codigo = lc[7]
                    label_titulo_c = CTkLabel(frame_anotacao_c, text=titulo_c, text_color=ct)
                    label_texto_c = CTkLabel(frame_anotacao_c, text=texto_c, text_color=ct)
                    label_linguagem = CTkLabel(frame_anotacao_c, text=linguagem.capitalize(), text_color=ct)
                    frame_anotacao_c.pack(pady=10, fill="x")
                    label_titulo_c.pack(pady=5)
                    if linguagem != "sua linguagem favorita...":
                        label_linguagem.pack(pady=1)
                    label_texto_c.pack(pady=1)
                    frame_anotacao_c.bind("<Button-1>", editar_codigo)
        
        def buscar(evento):
            materias = ["Português", "Matemática", "História", "Geografia", "Ciências", "Inglês", "Outros Estudos"]
            texto_busca = self.campo_busca.get().strip().capitalize()
            if texto_busca not in materias:
                lista_nota_buscar = busca_titulo(texto_busca, "notas")
            elif texto_busca in materias:
                lista_nota_buscar = busca_materia(texto_busca)
            if lista_nota_buscar == True:
                def tira_erro_busca():
                    erro_busca.destroy()
                erro_busca = CTkLabel(self.frame_guarda_notas, text="Nota não encontrada", text_color="#E21010", font=fonte_erros_inter)
                erro_busca.place(x=148, y=3)
                self.after(1400, tira_erro_busca)
            else:
                def editar_b(evento):
                        frame_anotacao_b.pack_forget()
                        self.frame_notas.place_forget()
                        def fonte_tamanho_eb(tamanho_eb):
                            if tamanho_eb == "8":
                                self.texto_eb.configure(font=fonte_8)
                            elif tamanho_eb == "10":
                                self.texto_eb.configure(font=fonte_10)
                            elif tamanho_eb == "12":
                                self.texto_eb.configure(font=fonte_12)
                            elif tamanho_eb == "14":
                                self.texto_eb.configure(font=fonte_14)
                            elif tamanho_eb == "16":
                                self.texto_eb.configure(font=fonte_16)
                            elif tamanho_eb == "18":
                                self.texto_eb.configure(font=fonte_18)
                            elif tamanho_eb == "20":
                                self.texto_eb.configure(font=fonte_20)
                            elif tamanho_eb == "22":
                                self.texto_eb.configure(font=fonte_22)

                        def muda_titulo_eb(nota_escolha):
                            if nota_escolha == "Português":
                                self.entrada_titulo_eb.configure(placeholder_text="Gramática, literatura, redação...")
                                self.tipo_nota_eb.configure(fg_color="#FF8DA1", button_color="#FF8DA1", button_hover_color="#E67E91")
                            elif nota_escolha == "Matemática":
                                self.entrada_titulo_eb.configure(placeholder_text="Frações, funções, regra de três...")
                                self.tipo_nota_eb.configure(fg_color="#1591EA", button_color="#1591EA", button_hover_color="#127BC6")
                            elif nota_escolha == "História":
                                self.entrada_titulo_eb.configure(placeholder_text="Brasil, revoluções, guerras...")
                                self.tipo_nota_eb.configure(fg_color="#FFA500", button_color="#FFA500", button_hover_color="#E39400")
                            elif nota_escolha == "Geografia":
                                self.entrada_titulo_eb.configure(placeholder_text="Clima, relevo, globalização...")
                                self.tipo_nota_eb.configure(fg_color="#50C878", button_color="#50C878", button_hover_color="#46AC68")
                            elif nota_escolha == "Ciências":
                                self.entrada_titulo_eb.configure(placeholder_text="Física, química, biologia...")
                                self.tipo_nota_eb.configure(fg_color="#2E6F40", button_color="#2E6F40", button_hover_color="#328A51")
                            elif nota_escolha == "Inglês":
                                self.entrada_titulo_eb.configure(placeholder_text="Conectivos, dia a dia, pronouns...")
                                self.tipo_nota_eb.configure(fg_color="#C9A41D", button_color="#C9A41D", button_hover_color="#B6941B")
                            else:
                                self.entrada_titulo_eb.configure(placeholder_text="Título...")
                                self.tipo_nota_eb.configure(fg_color=cls, button_color=cls, button_hover_color=ch)

                        def deletar_b():
                            deletou = deletar_nota(identidade_b_frame)
                            def tira_del():
                                self.frame_edita.destroy()
                                self.frame_notas.place(x=20, y=0)
                                    
                            if deletou == True:
                                self.label_del = CTkLabel(self.frame_editab, text="Deletado Com Sucesso!!", text_color="#E21010",font=fonte_erros_inter)
                                self.label_del.place(x=210, y=5)
                                self.after(1000, tira_del)
                            else:
                                self.label_del = CTkLabel(self.frame_editab, text="Erro ao deletar!!!", text_color="#E21010", font=fonte_erros_inter)
                                self.label_del.place(x=210, y=5)

                        def salvar_eb():
                            def tira_sal():
                                self.label_sal.destroy()
                            data_edicao_nota = time.strftime("%d/%m/%Y")
                            id = identidade_b_frame
                            titulo_e = self.entrada_titulo_eb.get().strip().capitalize()
                            texto_e = self.texto_eb.get("1.0", "end").strip().capitalize()
                            tipo_nota = self.tipo_nota_eb.get()
                            fonte_e = self.tamanho_fonte_eb.get()
                            negrito = self.texto_e._textbox.tag_ranges("negrito")
                            salvando = salvar_edicao(data_edicao_nota, id, titulo_e, texto_e, tipo_nota, fonte_e)
                            if salvando == True:
                                self.label_sal = CTkLabel(self.frame_editab, text="Salvo com sucesso!!", text_color="#2E6F40", font=fonte_erros_inter, fg_color=pg)
                                self.label_sal.place(x=210, y=5)
                                self.after(1000, tira_sal)

                        def ler_eb():
                            self.botao_leitura_eb.configure(state=DISABLED)
                            def ler_titulo_eb():
                                titulo_eb = self.entrada_titulo_eb.get()
                                texto_eb = self.texto_eb.get("1.0", "end")
                                if len(titulo_eb) >= 3 and len(texto_eb) >= 3 and pev == "Ativa":
                                    voz.say(titulo_eb)
                                    voz.runAndWait()
                                    voz.setProperty('rate', 127)
                                    voz.say(texto_eb)
                                    voz.runAndWait()
                                elif len(titulo_eb) < 3 or len(titulo_eb) > 30:
                                        def tira_erro_eb():
                                            self.erro_titulo_eb.destroy()
                                        self.erro_titulo_eb = CTkLabel(self.frame_editab, text="Tamanho de título inválido (Min:3, Max:30)!!", text_color="#981212", font=fonte_erros_inter)
                                        self.erro_titulo_eb.place(x=15, y=4)
                                        self.after(1400, tira_erro_eb)
                                elif len(texto_eb) < 3 or len(texto_eb) > 500:
                                        def tira_erro_eb():
                                            self.erro_nota_eb.destroy()
                                        self.erro_nota_eb = CTkLabel(self.frame_editab, text="Tamanho de nota inválido (Min:3, Max:500)!!", text_color="#981212", font=fonte_erros_inter)
                                        self.erro_nota_eb.place(x=15, y=4)
                                        self.after(1400, tira_erro_eb)
                                else:
                                    def tira_ativa_voz_eb():
                                        self.label_ative_voz_eb.destroy()
                                        self.botao_leitura_eb.configure(state=NORMAL)
                                    self.label_ative_voz_eb = CTkLabel(self.frame_editab, text="Ative a Voz!", text_color="#E21010", font=fonte_erros_inter)
                                    self.label_ative_voz_eb.place(x=170, y=5)
                                    self.botao_leitura_eb.configure(state=DISABLED)
                                    self.after(1100, tira_ativa_voz_eb)
                                self.botao_leitura_eb.configure(state=NORMAL)
                            self.thread_ler_titulo_eb = threading.Thread(target=ler_titulo_eb, daemon=True)
                            self.thread_ler_titulo_eb.start()

                        def negrito_eb(evento):
                            self.texto_eb._textbox.tag_add("negrito", "sel.first", "sel.last")
                            self.texto_eb._textbox.tag_configure("negrito", font=fonte_negrito)
                        
                        def voltar_anotacao_b():
                            self.frame_editab.pack_forget()
                            self.entrada_titulo_eb.delete(0, "end")
                            self.texto_eb.delete(0.0, "end")
                            self.tamanho_fonte_eb.destroy()
                            self.tipo_nota_eb.destroy()
                            self.frame_notas.place(x=20, y=0)
                            frame_anotacao_b.pack(pady=5, fill="x")

                        id_frame_b = evento.widget
                        while not hasattr(id_frame_b, "titulo"):
                            id_frame_b = id_frame_b.master
                        titulo_b = id_frame_b
                        titulo_b_frame = titulo_b.titulo
                        texto_b_frame = titulo_b.texto
                        identidade_b_frame = titulo_b.ID
                        materia_b_frame = titulo_b.mtr
                        fonte_b_frame = titulo_b.fonte
                        #Fonte da parte de salvar notas
                        fonte_eb = CTkFont(family="Arial", size=fonte_b_frame)
                        self.frame_editab = CTkFrame(self, width=470, height=350, fg_color=pg)
                        self.frame_editab.pack(pady=20)
                        self.tamanho_fonte_eb = CTkOptionMenu(self.frame_editab, width=90, cursor="hand2", values=["8","10", "12", "14", "16", "18", "20", "22"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=fonte_tamanho_eb)
                        self.entrada_titulo_eb = CTkEntry(self.frame_editab, width=212, corner_radius=10, border_color=cbp, placeholder_text_color=cbp, text_color=ct, fg_color=cf, font=fonte_eb)
                        self.texto_eb = CTkTextbox(self.frame_editab, width=210, height=170, border_width=2, border_color=cbp, corner_radius=10, text_color=ct, fg_color=cf, font=fonte_eb)
                        self.tipo_nota_eb = CTkOptionMenu(self.frame_editab, width=90, cursor="hand2", values=["Português", "Matemática", "História", "Geografia", "Ciências", "Inglês", "Outros Estudos"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=muda_titulo_eb)
                        self.botao_deletar_eb = CTkButton(self.frame_editab, text="Deletar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=deletar_b, hover_color=ch)
                        self.botao_salvar_eb = CTkButton(self.frame_editab, text="Salvar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=salvar_eb, hover_color=ch)
                        self.botao_leitura_eb = CTkButton(self.frame_editab, text="Ler", image=leitura, fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=ler_eb, hover_color=ch)
                        self.botao_voltar_eb = CTkButton(self.frame_editab, text="Voltar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=voltar_anotacao_b, hover_color=ch)
                        self.texto_eb.insert("0.0", texto_b_frame)
                        self.texto_eb.bind("<Control-n>", negrito_eb)
                        self.entrada_titulo_eb.insert(0, titulo_b_frame)
                        self.tamanho_fonte_eb.set(fonte_b_frame)
                        self.tipo_nota_eb.set(materia_b_frame)
                        self.entrada_titulo_eb.place(x=10, y=111)
                        self.texto_eb.place(x=10, y=156)
                        if materia_b_frame == "Tipo De Notas..." or materia_b_frame == "Outros Estudos":
                            self.tipo_nota_eb.place(x=360, y=110)
                        else:
                            self.tipo_nota_eb.place(x=370, y=110)   
                        self.botao_voltar_eb.place(x=1, y=1) 
                        self.tamanho_fonte_eb.place(x=370, y=160)
                        self.botao_salvar_eb.place(x=230, y=305)
                        self.botao_deletar_eb.place(x=262, y=272)
                        self.botao_leitura_eb.place(x=300, y=305)

                lista_notas = self.frame_notas.winfo_children()
                for ln in lista_notas:
                    ln.destroy()
                self.frame_guarda_notas = CTkFrame(self.frame_notas, width=440, height=68, fg_color=pg)
                self.frame_guarda_notas.pack(pady=10)
                self.botao_voltar_notas = CTkButton(self.frame_guarda_notas, text="Voltar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=voltar_notas_b, hover_color=ch)
                self.botao_voltar_notas.place(x=365, y=1)
                self.aba_nota = CTkButton(self.frame_guarda_notas, text="Notas", fg_color=pg, width=4, height=22, corner_radius=23, text_color=ct)
                self.aba_nota.place(x=4, y=1)
                self.aba_nota.configure(state=DISABLED)
                self.aba_codigo = CTkButton(self.frame_guarda_notas, text="Códigos", fg_color=pg, width=4, height=22, cursor="hand2", corner_radius=23, command=muda_aba_codigo, text_color=ct)
                self.aba_codigo.place(x=66, y=1)
                self.botao_cria_nota = CTkOptionMenu(self.frame_guarda_notas, values=["Nota", "Código"], fg_color=cls, height=25, cursor="hand2", corner_radius=19, button_color=cls, text_color=ctb, button_hover_color=ch,dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=escolha_comecar_b)
                self.botao_cria_nota.set("Começar...")
                self.botao_cria_nota.place(x=2, y=33)
                self.campo_busca = CTkEntry(self.frame_guarda_notas, width=162, corner_radius=10, border_color=cbp, placeholder_text_color=cbp, text_color=ct, fg_color=cf, placeholder_text="Busque por...")
                self.campo_busca.place(x=260, y=31)
                CTkToolTip(self.campo_busca, message="Clique a tecla ENTER", alpha=0.81, text_color=ctt, bg_color=cf)
                self.campo_busca.bind("<Return>", buscar)
                def entrou_campo_busca(evento):
                    self.campo_busca.configure(placeholder_text="Título, matéria...")
                self.campo_busca.bind("<Enter>", entrou_campo_busca)
                def saiu_campo_busca(evento):
                    self.focus_set()
                    self.campo_busca.configure(placeholder_text="Busque por...")
                self.campo_busca.bind("<Leave>", saiu_campo_busca)

                for lnb in lista_nota_buscar:
                    id = lnb[0]
                    titulo = lnb[1]
                    texto = lnb[2]
                    mtr = lnb[3]
                    fonte = lnb[4]
                    if len(texto) > 34:
                        if texto[33] == ",":
                            texto = texto[0:33] + "..."
                        else:
                            texto = texto[0:34] + "..."
                    else:
                        texto = texto[0:34]
                    frame_anotacao_b = CTkFrame(self.frame_notas, width=180, height=110, corner_radius=15, cursor="hand2", fg_color=cn)
                    frame_anotacao_b.ID = lnb[0] #Atribuindo o atributo ID aos frames, cada qual com seu id
                    frame_anotacao_b.titulo = lnb[1]
                    frame_anotacao_b.texto = lnb[2]
                    frame_anotacao_b.mtr = lnb[3]
                    frame_anotacao_b.fonte = lnb[4]
                    label_titulo = CTkLabel(frame_anotacao_b, text=titulo, text_color=ct)
                    label_texto = CTkLabel(frame_anotacao_b, text=texto, text_color=ct)
                    if mtr != "Tipo De Notas...":#Evita aparecer o nome setado
                        label_materia = CTkLabel(frame_anotacao_b, text=mtr, corner_radius=15, text_color=ct)
                        frame_anotacao_b.pack(pady=10, fill="x")
                        label_titulo.pack(pady=5)
                    if mtr != "Tipo De Notas...":
                        label_materia.pack(pady=0)
                    label_texto.pack(pady=1)
                    frame_anotacao_b.bind("<Button-1>", editar_b)

        def notas():
            self.frame_central.pack_forget()

            def voltar_notas():
                self.frame_notas.place_forget()
                self.frame_central.pack(pady=20) 

            def escolha_comecar(escolha):
                if escolha == "Nota":
                    def voltar_anota():
                        self.frame_notas.place(x=20, y=0)
                        self.frame_anota.pack_forget()

                    def salvar_texto():
                        data_atual_nota = time.strftime("%d/%m/%Y")
                        titulo = self.titulo.get()
                        titulo = titulo.strip().capitalize()
                        anotacao = self.texto.get("1.0", "end")
                        anotacao = anotacao.strip().capitalize()
                        negrito = self.texto._textbox.tag_ranges("negrito")
                        fonte = self.tamanho_fonte.get()
                        data_c = data_atual_nota
                        materia = self.tipo_nota.get()
                        if fonte == "Tamanho Da Fonte...":
                            fonte = 12
                        if materia == "Tipo De Notas...":
                            materia = "Outros Estudos"
                        if len(titulo) >= 3 and len(titulo) < 30 and len(anotacao) >= 3 and len(anotacao) < 500:
                            guarda_titulo_nota(titulo, anotacao, fonte, data_c, materia)
                            verificacao = verifica_guarda_titulo()
                            if verificacao == False:
                                def tira_salvo():
                                    self.label_salvo.destroy()
                                    self.texto.delete("1.0", "end")
                                    self.titulo.delete(0, "end")
                                    self.tipo_nota.set("Tipo De Notas...")
                                    self.tamanho_fonte.set("Tamanho Da Fonte...")
                                self.label_salvo = CTkLabel(self.frame_anota, text="Salvo com sucesso!!", text_color="#2E6F40", font=fonte_erros_inter, fg_color=pg)
                                self.label_salvo.place(x=15, y=4)
                                self.after(1400, tira_salvo)
                            else:
                                def tira_erro_salvo():
                                    self.label_erro_salvo.destroy()
                                self.label_erro_salvo = CTkLabel(self.frame_anota, text="Não Salvou!!!", text_color="#E21010", font=fonte_erros_inter)
                                self.label_salvo.place(x=15, y=4)
                                self.after(1400, tira_erro_salvo)
                        elif len(titulo) < 3 or len(titulo) > 30:
                            def tira_erro():
                                self.erro_titulo.destroy()
                            self.erro_titulo = CTkLabel(self.frame_anota, text="Tamanho de título inválido (Min:3, Max:30)!!", text_color="#E21010", font=fonte_erros_inter)
                            self.erro_titulo.place(x=15, y=4)
                            self.after(1400, tira_erro)
                        elif len(anotacao) < 3 or len(anotacao) > 500:
                            def tira_erro():
                                self.erro_nota.destroy()
                            self.erro_nota = CTkLabel(self.frame_anota, text="Tamanho de nota inválido (Min:3, Max:500)!!", text_color="#E21010", font=fonte_erros_inter)
                            self.erro_nota.place(x=15, y=4)
                            self.after(1400, tira_erro)
                    
                    def muda_titulo(nota_escolha):
                        if nota_escolha == "Português":
                            self.titulo.configure(placeholder_text="Gramática, literatura, redação...")
                            self.tipo_nota.configure(fg_color="#FF8DA1", button_color="#FF8DA1", button_hover_color="#E67E91")
                            self.texto.delete("0.0", "end")
                            self.texto.insert("0.0", "Hoje aprendi sobre...")
                        elif nota_escolha == "Matemática":
                            self.titulo.configure(placeholder_text="Frações, funções, regra de três...")
                            self.tipo_nota.configure(fg_color="#1591EA", button_color="#1591EA", button_hover_color="#127BC6")
                            self.texto.delete("0.0", "end")
                            self.texto.insert("0.0", "Hoje aprendi sobre...")
                        elif nota_escolha == "História":
                            self.titulo.configure(placeholder_text="Brasil, revoluções, guerras...")
                            self.tipo_nota.configure(fg_color="#FFA500", button_color="#FFA500", button_hover_color="#E39400")
                            self.texto.delete("0.0", "end")
                            self.texto.insert("0.0", "Hoje aprendi sobre...")
                        elif nota_escolha == "Geografia":
                            self.titulo.configure(placeholder_text="Clima, relevo, globalização...")
                            self.tipo_nota.configure(fg_color="#50C878", button_color="#50C878", button_hover_color="#46AC68")
                            self.texto.delete("0.0", "end")
                            self.texto.insert("0.0", "Hoje aprendi sobre...")
                        elif nota_escolha == "Ciências":
                            self.titulo.configure(placeholder_text="Física, química, biologia, energia...")
                            self.tipo_nota.configure(fg_color="#2E6F40", button_color="#2E6F40", button_hover_color="#328A51")
                            self.texto.delete("0.0", "end")
                            self.texto.insert("0.0", "Hoje aprendi sobre...")
                        elif nota_escolha == "Inglês":
                            self.titulo.configure(placeholder_text="Conectivos, dia a dia, pronouns...")
                            self.tipo_nota.configure(fg_color="#C9A41D", button_color="#C9A41D", button_hover_color="#B6941B")
                            self.texto.delete("0.0", "end")
                            self.texto.insert("0.0", "Hoje aprendi sobre...")
                        elif nota_escolha == "Programação":
                            self.titulo.configure(placeholder_text="POO, variáveis, condicionais...")
                            self.tipo_nota.configure(fg_color="#236BAF", button_color="#236BAF", button_hover_color="#1F63A3")
                            self.texto.delete("0.0", "end")
                            self.texto.insert("0.0", "O conceito é...")
                        else:
                            self.titulo.configure(placeholder_text="Título...")
                            self.tipo_nota.configure(fg_color=cls, button_color=cls, button_hover_color=ch)

                    def fonte_tamanho(tamanho):
                        if tamanho == "8":
                            self.texto.configure(font=fonte_8)
                        elif tamanho == "10":
                            self.texto.configure(font=fonte_10)
                        elif tamanho == "12":
                            self.texto.configure(font=fonte_12)
                        elif tamanho == "14":
                            self.texto.configure(font=fonte_14)
                        elif tamanho == "16":
                            self.texto.configure(font=fonte_16)
                        elif tamanho == "18":
                            self.texto.configure(font=fonte_18)
                        elif tamanho == "20":
                            self.texto.configure(font=fonte_20)
                        elif tamanho == "22":
                            self.texto.configure(font=fonte_22)

                    def apaga_texto(evento):
                        self.texto.delete("0.0", END)

                    def ler():
                        self.botao_leitura.configure(state=DISABLED)
                        def ler_titulo():
                            titulo = self.titulo.get()
                            texto = self.texto.get("1.0", "end")
                            if len(titulo) >= 3 and len(texto) >= 3 and pev == "Ativa":
                                voz.say(titulo)
                                voz.runAndWait()
                                voz.setProperty('rate', 127)
                                voz.say(texto)
                                voz.runAndWait()
                            elif len(titulo) < 3 or len(titulo) > 30:
                                    def tira_erro():
                                        self.erro_titulo.destroy()
                                    self.erro_titulo = CTkLabel(self.frame_anota, text="Tamanho de título inválido (Min:3, Max:30)!!", text_color="#981212", font=fonte_erros_inter)
                                    self.erro_titulo.place(x=15, y=4)
                                    self.after(1400, tira_erro)
                            elif len(texto) < 3 or len(texto) > 500:
                                    def tira_erro():
                                        self.erro_nota.destroy()
                                    self.erro_nota = CTkLabel(self.frame_anota, text="Tamanho de nota inválido (Min:3, Max:500)!!", text_color="#981212", font=fonte_erros_inter)
                                    self.erro_nota.place(x=15, y=4)
                                    self.after(1400, tira_erro)
                            else:
                                def tira_ativa_voz():
                                    self.label_ative_voz.destroy()
                                    self.botao_leitura.configure(state=NORMAL)
                                self.botao_leitura.configure(state=DISABLED)
                                self.label_ative_voz = CTkLabel(self.frame_anota, text="Ative a Voz!", text_color="#E21010", font=fonte_erros_inter)
                                self.label_ative_voz.place(x=170, y=5)
                                self.after(1100, tira_ativa_voz)
                            self.botao_leitura.configure(state=NORMAL)
                        self.thread_ler_titulo = threading.Thread(target=ler_titulo, daemon=True)
                        self.thread_ler_titulo.start()

                    def negrito(evento):
                        self.texto._textbox.tag_add("negrito", "sel.first", "sel.last")
                        self.texto._textbox.tag_configure("negrito", font=fonte_negrito)
        
                    self.frame_notas.place_forget()
                    self.frame_anota = CTkFrame(self, width=450, height=340, fg_color=pg)
                    self.frame_anota.pack(pady=20)
                    self.botao_voltar_anotas = CTkButton(self.frame_anota, text="Voltar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=voltar_anota, hover_color=ch)
                    self.botao_voltar_anotas.place(x=394, y=1)
                    self.tipo_nota = CTkOptionMenu(self.frame_anota, width=90, cursor="hand2", values=["Português", "Matemática", "História", "Geografia", "Ciências", "Inglês", "Programação", "Outros Estudos"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=muda_titulo)
                    self.tipo_nota.place(x=290, y=110)
                    self.tamanho_fonte = CTkOptionMenu(self.frame_anota, width=90, cursor="hand2", values=["8","10", "12", "14", "16", "18", "20", "22"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=fonte_tamanho)
                    self.tamanho_fonte.place(x=275, y=150)
                    self.tamanho_fonte.set("Tamanho Da Fonte...")
                    self.tipo_nota.set("Tipo De Notas...")
                    self.titulo = CTkEntry(self.frame_anota, width=222, placeholder_text="Título...", corner_radius=10, border_color=cbp, placeholder_text_color=cbp, text_color=ctt, fg_color=cf)
                    self.titulo.place(x=10, y=80)
                    self.texto = CTkTextbox(self.frame_anota, width=222, height=200, border_width=2, border_color=cbp, corner_radius=10, text_color=ctt, fg_color=cf)
                    self.texto.place(x=10, y=120)
                    self.texto.insert("0.0", "Hoje aprendi sobre...")
                    self.texto.bind("<Control-n>", negrito)
                    CTkToolTip(self.texto, message="Clique o botão direito do mouse", alpha=0.81, text_color=ctt, bg_color=cf)
                    self.texto.bind("<Button-3>", apaga_texto)
                    self.botao_salvar = CTkButton(self.frame_anota, text="Salvar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=salvar_texto, hover_color=ch)
                    self.botao_leitura = CTkButton(self.frame_anota, text="Ler", image=leitura, fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=ler, hover_color=ch)
                    self.botao_salvar.place(x=238, y=295)
                    self.botao_leitura.place(x=308, y=295)
                elif escolha == "Código":
                    def voltar_codigo():
                        self.frame_codigo.pack_forget()
                        self.frame_notas.place(x=20, y=0)
                    
                    def apaga_descricao(evento):
                        self.descricao.delete("0.0", END)
                    
                    def apaga_texto_codigo(evento):
                        self.texto_codigo.delete("0.0", END)

                    def fonte_tamanho_codigo(tamanho):
                        if tamanho == "8":
                            self.texto_codigo.configure(font=fonte_8)
                        elif tamanho == "10":
                            self.texto_codigo.configure(font=fonte_10)
                        elif tamanho == "12":
                            self.texto_codigo.configure(font=fonte_12)
                        elif tamanho == "14":
                            self.texto_codigo.configure(font=fonte_14)
                        elif tamanho == "16":
                            self.texto_codigo.configure(font=fonte_16)
                        elif tamanho == "18":
                            self.texto_codigo.configure(font=fonte_18)
                        elif tamanho == "20":
                            self.texto_codigo.configure(font=fonte_20)
                        elif tamanho == "22":
                            self.texto_codigo.configure(font=fonte_22)

                    def fonte_tamanho_descricao(tamanho):
                        if tamanho == "8":
                            self.descricao.configure(font=fonte_8)
                        elif tamanho == "10":
                            self.descricao.configure(font=fonte_10)
                        elif tamanho == "12":
                            self.descricao.configure(font=fonte_12)
                        elif tamanho == "14":
                            self.descricao.configure(font=fonte_14)
                        elif tamanho == "16":
                            self.descricao.configure(font=fonte_16)
                        elif tamanho == "18":
                            self.descricao.configure(font=fonte_18)
                        elif tamanho == "20":
                            self.descricao.configure(font=fonte_20)
                        elif tamanho == "22":
                            self.descricao.configure(font=fonte_22)
                        
                    def lang(lang_escolhida):
                        if lang_escolhida == "Python":
                            self.texto_codigo.configure(language="python")
                        elif lang_escolhida == "Zig":
                            self.texto_codigo.configure(language="zig")
                        elif lang_escolhida == "Javascript":
                            self.texto_codigo.configure(language="Javascript")
                        elif lang_escolhida == "C++":
                            self.texto_codigo.configure(language="c++")
                        elif lang_escolhida == "Lua":
                            self.texto_codigo.configure(language="lua")
                        elif lang_escolhida == "Rust":
                            self.texto_codigo.configure(language="rust")
                        elif lang_escolhida == "Java":
                            self.texto_codigo.configure(language="java")
                        elif lang_escolhida == "CSS":
                            self.texto_codigo.configure(language="css")
                        elif lang_escolhida == "HTML":
                            self.texto_codigo.configure(language="html")
                        elif lang_escolhida == "C#":
                            self.texto_codigo.configure(language="c#")
                        elif lang_escolhida == "PHP":
                            self.texto_codigo.configure(language="php")
                    
                    def tema(tema_escolhido):
                        if tema_escolhido == "Arduino":
                            self.texto_codigo.configure(theme="arduino")
                        elif tema_escolhido == "Abap":
                            self.texto_codigo.configure(theme="abap")
                        elif tema_escolhido == "Autumn":
                            self.texto_codigo.configure(theme="autumn")
                        elif tema_escolhido == "Borland":
                            self.texto_codigo.configure(theme="borland")
                        elif tema_escolhido == "Colorful":
                            self.texto_codigo.configure(theme="colorful")
                        elif tema_escolhido == "Default":
                            self.texto_codigo.configure(theme="default")
                        elif tema_escolhido == "Dracula":
                            self.texto_codigo.configure(theme="dracula")
                        elif tema_escolhido == "Emacs":
                            self.texto_codigo.configure(theme="emacs")
                        elif tema_escolhido == "Friendly":
                            self.texto_codigo.configure(theme="friendly")
                        elif tema_escolhido == "Fruit":
                            self.texto_codigo.configure(theme="fruit")
                        elif tema_escolhido == "Igor":
                            self.texto_codigo.configure(theme="igor")
                        elif tema_escolhido == "Inkpot":
                            self.texto_codigo.configure(theme="inkpot")
                        
                    def salvar_texto_codigo():
                        data_atual_codigo = time.strftime("%d/%m/%Y")
                        titulo_codigo = self.titulo_codigo.get().strip().capitalize()
                        descricao = self.descricao.get("1.0", "end").strip().capitalize()
                        codigo = self.texto_codigo.get("1.0", "end").strip()
                        fonte_codigo = self.fonte_tamanho_codigo.get()
                        fonte_descricao = self.fonte_tamanho_descricao.get()
                        tema = self.tema.get().lower()
                        linguagem = self.linguagem.get().lower()
                        data_c = data_atual_codigo
                        if fonte_codigo == "Tamanho Da Fonte...":
                            fonte_codigo = 12
                        if fonte_descricao == "Tamanho Da Fonte...":
                            fonte_descricao = 12
                        if tema == "seu tema favorito...":
                            tema = "arduino"
                        if linguagem == "sua linguagem favorita...":
                            linguagem = "python"
                        if len(titulo_codigo) >= 3 and len(titulo_codigo) < 30 and len(descricao) >= 3 and len(descricao) < 500:
                            guarda_codigos(titulo_codigo, descricao, fonte_descricao, data_c, codigo, fonte_codigo, tema, linguagem)
                            verificacao = verifica_guarda_codigo()
                            if verificacao == False:
                                def tira_salvo():
                                    self.label_salvo.destroy()
                                    self.texto_codigo.delete("1.0", "end")
                                    self.titulo_codigo.delete(0, "end")
                                    self.descricao.delete("1.0", "end")
                                    self.fonte_tamanho_descricao.set("Tamanho Da Fonte...")
                                    self.fonte_tamanho_codigo.set("Tamanho Da Fonte...")
                                    self.tema.set("Seu Tema Favorito...")
                                    self.linguagem.set("Sua Linguagem Favorita...")
                                self.label_salvo = CTkLabel(self.frame_codigo, text="Salvo com sucesso!!", text_color="#2E6F40", font=fonte_erros_inter, fg_color=pg)
                                self.label_salvo.place(x=75, y=2)
                                self.after(1400, tira_salvo)
                            else:
                                def tira_erro_salvo():
                                    self.label_erro_salvo.destroy()
                                self.label_erro_salvo = CTkLabel(self.frame_codigo, text="Não Salvou!!!", text_color="#E21010", font=fonte_erros_inter)
                                self.label_salvo.place(x=75, y=2)
                                self.after(1400, tira_erro_salvo)
                        elif len(titulo_codigo) < 3 or len(titulo_codigo) > 30:
                            def tira_erro():
                                self.erro_titulo.destroy()
                            self.erro_titulo = CTkLabel(self.frame_codigo, text="Tamanho de título inválido (Min:3, Max:30)!!", text_color="#E21010", font=fonte_erros_inter)
                            self.erro_titulo.place(x=167, y=30)
                            self.after(1400, tira_erro)
                        elif len(descricao) < 3 or len(descricao) > 500:
                            def tira_erro():
                                self.erro_nota.destroy()
                            self.erro_nota = CTkLabel(self.frame_codigo, text="Tamanho de descrição inválido (Min:3, Max:500)!!", text_color="#E21010", font=fonte_erros_inter)
                            self.erro_nota.place(x=245, y=30)
                            self.after(1400, tira_erro)
                        elif len(codigo) < 3:
                            def tira_erro():
                                self.erro_nota.destroy()
                            self.erro_nota = CTkLabel(self.frame_codigo, text="Digite seu código!!", text_color="#E21010", font=fonte_erros_inter)
                            self.erro_nota.place(x=288, y=30)
                            self.after(1400, tira_erro)

                    def ler_descricao():
                        self.botao_leitura_codigos.configure(state=DISABLED)
                        def ler_texto():
                            titulo_codigo = self.titulo_codigo.get()
                            descricao = self.descricao.get("1.0", "end")
                            if len(titulo_codigo) > 3 and len(descricao) > 3 and pev == "Ativa":
                                voz.say(titulo_codigo)
                                voz.runAndWait()
                                voz.setProperty('rate', 127)
                                voz.say(descricao)
                                voz.runAndWait()
                            elif len(titulo_codigo) < 3 or len(titulo_codigo) > 30:
                                def tira_erro():
                                    self.erro_titulo.destroy()
                                self.erro_titulo = CTkLabel(self.frame_codigo, text="Tamanho de título inválido (Min:3, Max:30)!!", text_color="#981212", font=fonte_erros_inter)
                                self.erro_titulo.place(x=167, y=30)
                                self.after(1400, tira_erro)
                            elif len(descricao) < 3 or len(descricao) > 500:
                                    def tira_erro():
                                        self.erro_nota.destroy()
                                    self.erro_nota = CTkLabel(self.frame_codigo, text="Tamanho de descrição inválido (Min:3, Max:500)!!", text_color="#981212", font=fonte_erros_inter)
                                    self.erro_nota.place(x=245, y=30)
                                    self.after(1400, tira_erro)
                            else:
                                def tira_ativa_voz():
                                    self.label_ative_voz.destroy()
                                    self.botao_leitura_codigos.configure(state=NORMAL)
                                self.label_ative_voz = CTkLabel(self.frame_codigo, text="Ative a Voz!", text_color="#E21010", font=fonte_erros_inter)
                                self.label_ative_voz.place(x=170, y=2)
                                self.botao_leitura_codigos.configure(state=DISABLED)
                                self.after(1100, tira_ativa_voz)
                            self.botao_leitura_codigos.configure(state=NORMAL)
                        self.thread_ler_descricao = threading.Thread(target=ler_texto, daemon=True)
                        self.thread_ler_descricao.start()

                    def muda_titulo_codigo(evento):
                        self.titulo_codigo.configure(placeholder_text="Projeto, função de, conceito...")
    
                    self.frame_notas.place_forget()    
                    self.frame_codigo = CTkFrame(self, width=470, height=360, fg_color=pg)
                    self.frame_codigo.pack(pady=20)
                    self.botao_voltar_codigo = CTkButton(self.frame_codigo, text="Voltar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=voltar_codigo, hover_color=ch)
                    self.botao_voltar_codigo.place(x=404, y=1)
                    self.fonte_tamanho_codigo = CTkOptionMenu(self.frame_codigo, width=90, cursor="hand2", values=["8","10", "12", "14", "16", "18", "20", "22"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=fonte_tamanho_codigo)
                    self.fonte_tamanho_codigo.place(x=4, y=25)
                    self.fonte_tamanho_codigo.set("Tamanho Da Fonte...")
                    self.texto_codigo = ccb.CTkCodeBox(self.frame_codigo, width=227, height=160, theme="arduino", language="python",fg_color=cf, border_width=2, border_color=cbp, corner_radius=10, numbering_color=cbp, menu=False)
                    self.texto_codigo.place(x=4, y=130)
                    self.texto_codigo.insert("0.0", ">Código...")
                    CTkToolTip(self.texto_codigo, message="Clique o botão direito do mouse", alpha=0.81, text_color=ctt, bg_color=cf)
                    self.texto_codigo.bind("<Button-3>", apaga_texto_codigo)
                    self.tema = CTkOptionMenu(self.frame_codigo, width=90, cursor="hand2", values=["Arduino","Abap", "Autumn", "Borland", "Colorful", "Default", "Dracula", "Emacs", "Friendly", "Fruity", "Igor", "Inkpot"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=tema)
                    self.tema.place(x=4, y=60)
                    self.tema.set("Seu Tema Favorito...")
                    self.linguagem = CTkOptionMenu(self.frame_codigo, width=90, cursor="hand2", values=["Python", "JavaScript", "Lua", "Rust", "CSS", "HTML", "Java", "C++", "PHP", "C#", "Zig"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=lang)
                    self.linguagem.place(x=4, y=95)
                    self.linguagem.set("Sua Linguagem Favorita...")
                    self.fonte_tamanho_descricao = CTkOptionMenu(self.frame_codigo, width=90, cursor="hand2", values=["8","10", "12", "14", "16", "18", "20", "22"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=fonte_tamanho_descricao)
                    self.fonte_tamanho_descricao.place(x=282, y=115)
                    self.fonte_tamanho_descricao.set("Tamanho Da Fonte...")
                    self.titulo_codigo = CTkEntry(self.frame_codigo, width=212, border_width=2, border_color=cbp, corner_radius=10, text_color=ctt, fg_color=cf, placeholder_text="Título...", placeholder_text_color=cbp)
                    self.titulo_codigo.place(x=258, y=60)
                    self.titulo_codigo.bind("<Enter>", muda_titulo_codigo)
                    self.descricao = CTkTextbox(self.frame_codigo, width=212, height=90, border_width=2, border_color=cbp, corner_radius=10, text_color=ctt, fg_color=cf)
                    self.descricao.place(x=258, y=150)
                    self.descricao.insert("0.0", "Esse código faz...")
                    CTkToolTip(self.descricao, message="Clique o botão direito do mouse", alpha=0.81, text_color=ctt, bg_color=cf)
                    self.descricao.bind("<Button-3>", apaga_descricao)
                    self.botao_salvar = CTkButton(self.frame_codigo, text="Salvar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=salvar_texto_codigo, hover_color=ch)
                    self.botao_leitura_codigos = CTkButton(self.frame_codigo, text="Ler", image=leitura, fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=ler_descricao, hover_color=ch)
                    self.botao_salvar.place(x=236, y=303)
                    self.botao_leitura_codigos.place(x=398, y=247)

            def editar(evento):
                frame_anotacao.pack_forget()
                self.frame_notas.place_forget()
                def fonte_tamanho_e(tamanho_e):
                    if tamanho_e == "8":
                        self.texto_e.configure(font=fonte_8)
                    elif tamanho_e == "10":
                        self.texto_e.configure(font=fonte_10)
                    elif tamanho_e == "12":
                        self.texto_e.configure(font=fonte_12)
                    elif tamanho_e == "14":
                        self.texto_e.configure(font=fonte_14)
                    elif tamanho_e == "16":
                        self.texto_e.configure(font=fonte_16)
                    elif tamanho_e == "18":
                        self.texto_e.configure(font=fonte_18)
                    elif tamanho_e == "20":
                        self.texto_e.configure(font=fonte_20)
                    elif tamanho_e == "22":
                        self.texto_e.configure(font=fonte_22)

                def muda_titulo_e(nota_escolha):
                    if nota_escolha == "Português":
                        self.entrada_titulo_e.configure(placeholder_text="Gramática, literatura, redação...")
                        self.tipo_nota_e.configure(fg_color="#FF8DA1", button_color="#FF8DA1", button_hover_color="#E67E91")
                    elif nota_escolha == "Matemática":
                        self.entrada_titulo_e.configure(placeholder_text="Frações, funções, regra de três...")
                        self.tipo_nota_e.configure(fg_color="#1591EA", button_color="#1591EA", button_hover_color="#127BC6")
                    elif nota_escolha == "História":
                        self.entrada_titulo_e.configure(placeholder_text="Brasil, revoluções, guerras...")
                        self.tipo_nota_e.configure(fg_color="#FFA500", button_color="#FFA500", button_hover_color="#E39400")
                    elif nota_escolha == "Geografia":
                        self.entrada_titulo_e.configure(placeholder_text="Clima, relevo, globalização...")
                        self.tipo_nota_e.configure(fg_color="#50C878", button_color="#50C878", button_hover_color="#46AC68")
                    elif nota_escolha == "Ciências":
                        self.entrada_titulo_e.configure(placeholder_text="Física, química, biologia...")
                        self.tipo_nota_e.configure(fg_color="#2E6F40", button_color="#2E6F40", button_hover_color="#328A51")
                    elif nota_escolha == "Inglês":
                        self.entrada_titulo_e.configure(placeholder_text="Conectivos, dia a dia, pronouns...")
                        self.tipo_nota_e.configure(fg_color="#C9A41D", button_color="#C9A41D", button_hover_color="#B6941B")
                    else:
                        self.entrada_titulo_e.configure(placeholder_text="Título...")
                        self.tipo_nota_e.configure(fg_color=cls, button_color=cls, button_hover_color=ch)

                def deletar():
                    deletou = deletar_nota(identidade_frame)
                    def tira_del():
                        self.frame_edita.destroy()
                        self.frame_notas.place(x=20, y=0)
                        
                    if deletou == True:
                        self.label_del = CTkLabel(self.frame_edita, text="Deletado Com Sucesso!!", text_color="#E21010", font=fonte_erros_inter)
                        self.label_del.place(x=210, y=5)
                        self.after(1000, tira_del)
                    else:
                        self.label_del = CTkLabel(self.frame_edita, text="Erro ao deletar!!!", text_color="#E21010", font=fonte_erros_inter)
                        self.label_del.place(x=210, y=5)

                def salvar_e():
                    def tira_sal():
                        self.label_sal.destroy()
                    data_edicao_nota = time.strftime("%d/%m/%Y")
                    id = identidade_frame
                    titulo_e = self.entrada_titulo_e.get().strip().capitalize()
                    texto_e = self.texto_e.get("1.0", "end").strip().capitalize()
                    negrito = self.texto_e._textbox.tag_ranges("negrito")
                    tipo_nota = self.tipo_nota_e.get()
                    fonte_e = self.tamanho_fonte_e.get()
                    salvando = salvar_edicao(data_edicao_nota, id, titulo_e, texto_e, tipo_nota, fonte_e)
                    if salvando == True:
                        self.label_sal = CTkLabel(self.frame_edita, text="Salvo com sucesso!!", text_color="#2E6F40", font=fonte_erros_inter, fg_color=pg)
                        self.label_sal.place(x=210, y=5)
                        self.after(1000, tira_sal)

                def ler_e():
                    self.botao_leitura_e.configure(state=DISABLED)
                    def ler_titulo_e():
                        titulo_e = self.entrada_titulo_e .get()
                        texto_e = self.texto_e.get("1.0", "end")
                        if len(titulo_e) > 3 and len(texto_e) > 3 and pev == "Ativa":
                            voz.say(titulo_e)
                            voz.runAndWait()
                            voz.setProperty('rate', 127)
                            voz.say(texto_e)
                            voz.runAndWait()
                        elif len(titulo_e) < 3 or len(titulo_e) > 30:
                            def tira_erro_e():
                                    self.erro_titulo_e.destroy()
                            self.erro_titulo_e = CTkLabel(self.frame_anota, text="Tamanho de título inválido (Min:3, Max:30)!!", text_color="#981212", font=fonte_erros_inter)
                            self.erro_titulo_e.place(x=15, y=4)
                            self.after(1400, tira_erro_e)
                        elif len(texto_e) < 3 or len(texto_e) > 500:
                            def tira_erro_e():
                                self.erro_nota_e.destroy()
                            self.erro_nota_e = CTkLabel(self.frame_anota, text="Tamanho de nota inválido (Min:3, Max:500)!!", text_color="#981212", font=fonte_erros_inter)
                            self.erro_nota_e.place(x=15, y=4)
                            self.after(1400, tira_erro_e)
                        else:
                            def tira_ativa_voz_e():
                                self.label_ative_voz_e.destroy()
                            self.label_ative_voz_e = CTkLabel(self.frame_anota, text="Ative a Voz!", text_color="#E21010", font=fonte_erros_inter)
                            self.label_ative_voz_e.place(x=170, y=5)
                            self.botao_leitura_e.configure(state=DISABLED)
                            self.after(1100, tira_ativa_voz_e)
                        self.botao_leitura_e.configure(state=NORMAL)
                    self.thread_ler_titulo_e = threading.Thread(target=ler_titulo_e, daemon=True)
                    self.thread_ler_titulo_e.start()
                    
                def negrito(evento):
                    self.texto_e._textbox.tag_add("negrito", "sel.first", "sel.last")
                    self.texto_e._textbox.tag_configure("negrito", font=fonte_negrito)
                    negrito = self.texto_e._textbox.tag_ranges("negrito")

                def voltar_anotacao():
                    self.frame_edita.pack_forget()
                    self.entrada_titulo_e.delete(0, "end")
                    self.texto_e.delete(0.0, "end")
                    self.tamanho_fonte_e.destroy()
                    self.tipo_nota_e.destroy()
                    self.frame_notas.place(x=20, y=0)
                    frame_anotacao.pack(pady=5, fill="x")

                id_frame = evento.widget
                while not hasattr(id_frame, "titulo"):
                    id_frame = id_frame.master
                titulo = id_frame
                titulo_frame = titulo.titulo
                texto_frame = titulo.texto
                identidade_frame = titulo.ID
                materia_frame = titulo.mtr
                fonte_frame = titulo.fonte
                #Fonte da parte de salvar notas
                fonte_e = CTkFont(family="Arial", size=fonte_frame)
                self.frame_edita = CTkFrame(self, width=470, height=350, fg_color=pg)
                self.frame_edita.pack(pady=20)
                self.tamanho_fonte_e = CTkOptionMenu(self.frame_edita, width=90, cursor="hand2", values=["8","10", "12", "14", "16", "18", "20", "22"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=fonte_tamanho_e)
                self.entrada_titulo_e = CTkEntry(self.frame_edita, width=212, corner_radius=10, border_color=cbp, placeholder_text_color=cbp, text_color=ct, fg_color=cf, font=fonte_e)
                self.texto_e = CTkTextbox(self.frame_edita, width=210, height=170, border_width=2, border_color=cbp, corner_radius=10, text_color=ct, fg_color=cf, font=fonte_e)
                self.tipo_nota_e = CTkOptionMenu(self.frame_edita, width=90, cursor="hand2", values=["Português", "Matemática", "História", "Geografia", "Ciências", "Inglês", "Outros Estudos"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=muda_titulo_e)
                self.botao_deletar_e = CTkButton(self.frame_edita, text="Deletar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=deletar, hover_color=ch)
                self.botao_salvar_e = CTkButton(self.frame_edita, text="Salvar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=salvar_e, hover_color=ch)
                self.botao_leitura_e = CTkButton(self.frame_edita, text="Ler", image=leitura, fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=ler_e, hover_color=ch)
                self.botao_voltar_e = CTkButton(self.frame_edita, text="Voltar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=voltar_anotacao, hover_color=ch)
                self.texto_e.insert("0.0", texto_frame)
                self.texto_e.bind("<Control-n>", negrito)
                self.entrada_titulo_e.insert(0, titulo_frame)
                self.tamanho_fonte_e.set(fonte_frame)
                self.tipo_nota_e.set(materia_frame)
                self.entrada_titulo_e.place(x=10, y=111)
                self.texto_e.place(x=10, y=156)
                if materia_frame == "Tipo De Notas..." or materia_frame == "Outros Estudos":
                    self.tipo_nota_e.place(x=360, y=110)
                else:
                    self.tipo_nota_e.place(x=370, y=110)   
                self.botao_voltar_e.place(x=1, y=1) 
                self.tamanho_fonte_e.place(x=370, y=160)
                self.botao_salvar_e.place(x=230, y=305)
                self.botao_deletar_e.place(x=262, y=272)
                self.botao_leitura_e.place(x=300, y=305)

            self.frame_notas = CTkScrollableFrame(self, width=440, height=330, fg_color=pg)
            self.frame_notas.place(x=20, y=0)
            self.frame_guarda_notas = CTkFrame(self.frame_notas, width=440, height=68, fg_color=pg)
            self.frame_guarda_notas.pack(pady=10)
            self.aba_nota = CTkButton(self.frame_guarda_notas, text="Notas", fg_color=pg, width=4, height=22, corner_radius=23, text_color=ct)
            self.aba_nota.place(x=4, y=1)
            self.aba_nota.configure(state=DISABLED)
            self.aba_codigo = CTkButton(self.frame_guarda_notas, text="Códigos", fg_color=pg, width=4, height=22, cursor="hand2", corner_radius=23, command=muda_aba_codigo, text_color=ct)
            self.aba_codigo.place(x=66, y=1)
            self.botao_voltar_notas = CTkButton(self.frame_guarda_notas, text="Voltar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=voltar_notas, hover_color=ch)
            self.botao_voltar_notas.place(x=365, y=1)
            self.botao_cria_nota = CTkOptionMenu(self.frame_guarda_notas, values=["Nota", "Código"], fg_color=cls, height=25, cursor="hand2", corner_radius=19, button_color=cls, text_color=ctb, button_hover_color=ch,dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=escolha_comecar)
            self.botao_cria_nota.set("Começar...")
            self.botao_cria_nota.place(x=2, y=33)
            self.campo_busca = CTkEntry(master=self.frame_guarda_notas, width=162, corner_radius=10, border_color=cbp, placeholder_text_color=cbp, text_color=ct, fg_color=cf, placeholder_text="Busque por...")
            self.campo_busca.place(x=260, y=31)
            CTkToolTip(self.campo_busca, message="Clique a tecla ENTER", alpha=0.81, text_color=ctt, bg_color=cf)
            self.campo_busca.bind("<Return>", buscar)
            def entrou_campo_busca(evento):
                self.campo_busca.configure(placeholder_text="Título, matéria...")
            self.campo_busca.bind("<Enter>", entrou_campo_busca)
            def saiu_campo_busca(evento):
                self.focus_set()
                self.campo_busca.configure(placeholder_text="Busque por...")
            self.campo_busca.bind("<Leave>", saiu_campo_busca)

            #Pega as notas
            self.lista_notas = pega_notas()
            #Percorre a lista de notas e posiciona os frames com elas.
            for ln in self.lista_notas:
                titulo = ln[1]
                texto = ln[2]
                if len(texto) > 34:
                    if texto[33] == ",":
                        texto = texto[0:33] + "..."
                    else:
                        texto = texto[0:34] + "..."
                else:
                    texto = texto[0:34]
                mtr = ln[3]
                frame_anotacao = CTkFrame(self.frame_notas, width=180, height=120, corner_radius=15, cursor="hand2", fg_color=cn)
                frame_anotacao.ID = ln[0] #Atribuindo o atributo ID aos frames, cada qual com seu id
                frame_anotacao.titulo = ln[1]
                frame_anotacao.texto = ln[2]
                frame_anotacao.mtr = ln[3]
                frame_anotacao.fonte = ln[4]
                label_titulo = CTkLabel(frame_anotacao, text=titulo, text_color=ct)
                label_texto = CTkLabel(frame_anotacao, text=texto, text_color=ct)
                if mtr != "Tipo De Notas...":#Evita aparecer o nome setado
                    label_materia = CTkLabel(frame_anotacao, text=mtr, corner_radius=15, text_color=ct)
                frame_anotacao.pack(pady=10, fill="x")
                label_titulo.pack(pady=5)
                if mtr != "Tipo De Notas...":
                    label_materia.pack(pady=0)
                label_texto.pack(pady=1)
                frame_anotacao.bind("<Button-1>", editar)

        def config():
            self.frame_central.pack_forget()

            def voltar_config():
                self.frame_config.place_forget()

                self.title("Sponte Study")
                self.frame_central.pack(pady=20)

            def cor_fundo(cor):
                if cor == "Noite":
                    self.frame_config.configure(fg_color="#101A12")
                    self.entrada_hexa.configure(text_color="white", placeholder_text="Digite a cor hexa...", placeholder_text_color="#5E127F", border_color="#5E127F", fg_color="#101A12")
                    self.label_aviso_reinic.configure(text_color="white")
                    alerta = CTkImage(Image.open(os.path.join(imagem_pasta, "alerta_preto.png")), size=(17, 17))
                    self.alert.configure(image=alerta)
                    self.botao_voltar_config.configure(fg_color="#5E127F", hover_color="#541070")
                    self.botao_enviar_hexa.configure(fg_color="#5E127F", hover_color="#541070")
                    self.label_config.configure(text_color="#5E127F")
                    self.label_config.configure(text_color="#5E127F")
                    self.label_voz.configure(text_color="#5E127F")
                    self.voz_ativa.configure(progress_color="#5E127F")
                    self.cores_fundo.configure(fg_color="#5E127F", button_color="#5E127F", button_hover_color="#541070")
                    cor_escolhida = "#101A12"
                    atualiza_cor(cor_escolhida)
                elif cor == "Branco":
                    self.entrada_hexa.configure(text_color="black", border_color="#105ba0", placeholder_text="Digite a cor hexa...", placeholder_text_color="#105ba0", fg_color="white")
                    self.label_aviso_reinic.configure(text_color="black")
                    self.frame_config.configure(fg_color="#F7F7F7")
                    self.entrada_hexa._entry.configure(insertbackground="#105ba0")
                    alerta = CTkImage(Image.open(os.path.join(imagem_pasta, "alerta_branco.png")), size=(17, 17))
                    self.alert.configure(image=alerta)
                    self.botao_voltar_config.configure(fg_color="#105ba0", hover_color="#oc4478")
                    self.botao_enviar_hexa.configure(fg_color="#105ba0", hover_color="#0c4478")
                    self.label_config.configure(text_color="#105ba0")
                    self.label_config.configure(text_color="#105ba0")
                    self.label_voz.configure(text_color="#105ba0")
                    self.voz_ativa.configure(progress_color="#105ba0")
                    self.cores_fundo.configure(fg_color="#105ba0", button_color="#105ba0", button_hover_color="#0c4478")
                    cor_escolhida = "#F7F7F7"
                    atualiza_cor(cor_escolhida)
                elif cor == "Amor":
                    self.entrada_hexa.configure(text_color="Black", placeholder_text="Digite a cor hexa...", placeholder_text_color="#F32A2A", border_color="#F32A2A", fg_color="white")
                    self.label_aviso_reinic.configure(text_color="black")
                    self.frame_config.configure(fg_color="#BE2121")
                    alerta = CTkImage(Image.open(os.path.join(imagem_pasta, "alerta_vermelho.png")), size=(17, 17))
                    self.alert.configure(image=alerta)
                    self.botao_voltar_config.configure(fg_color="#FFBFBF", hover_color="#F1B7B7")
                    self.botao_enviar_hexa.configure(fg_color="#FFBFBF", hover_color="#F1B7B7")
                    self.label_config.configure(text_color="#FFBFBF")
                    self.label_config.configure(text_color="#FFBFBF")
                    self.label_voz.configure(text_color="#FFBFBF")
                    self.voz_ativa.configure(progress_color="#FFBFBF")
                    self.cores_fundo.configure(fg_color="#FFBFBF", button_color="#FFBFBF", button_hover_color="#F1B7B7")
                    self.cores_fundo.configure(fg_color="#FFBFBF", button_color="#FFBFBF", button_hover_color="#F1B7B7")
                    cor_escolhida = "#BE2121"
                    atualiza_cor(cor_escolhida)
                elif cor == "Azul":   
                    self.entrada_hexa.configure(text_color="Black", placeholder_text="Digite a cor hexa...", placeholder_text_color="#1093D4", border_color="#1093D4", fg_color="white")   
                    self.label_aviso_reinic.configure(text_color="white")
                    self.frame_config.configure(fg_color="#1093D4")
                    alerta = CTkImage(Image.open(os.path.join(imagem_pasta, "alerta_azullogus.png")), size=(17, 17))
                    self.alert.configure(image=alerta)
                    self.botao_voltar_config.configure(fg_color="#105ba0", hover_color="#0c4478")
                    self.botao_enviar_hexa.configure(fg_color="#105ba0", hover_color="#0c4478")
                    self.label_config.configure(text_color="#105ba0")
                    self.label_config.configure(text_color="#105ba0")
                    self.label_voz.configure(text_color="#105ba0")
                    self.voz_ativa.configure(progress_color="#105ba0")
                    self.cores_fundo.configure(fg_color="#105ba0", button_color="#105ba0", button_hover_color="#105ba0")
                    cor_escolhida = "#1093D4"
                    atualiza_cor(cor_escolhida)
                elif cor == "Praia":
                    self.entrada_hexa.configure(text_color="Black", placeholder_text="Digite a cor hexa...", placeholder_text_color="#FF5C00", border_color="#FF5C00", fg_color="white")
                    self.label_aviso_reinic.configure(text_color="black")
                    self.frame_config.configure(fg_color="#FFDE21")
                    alerta = CTkImage(Image.open(os.path.join(imagem_pasta, "alerta_amarelo.png")), size=(17, 17))
                    self.alert.configure(image=alerta)
                    self.botao_voltar_config.configure(fg_color="#FF5C00", hover_color="#EB5A05")
                    self.botao_enviar_hexa.configure(fg_color="#FF5C00", hover_color="#EB5A05")
                    self.label_config.configure(text_color="#FF5C00")
                    self.label_config.configure(text_color="#FF5C00")
                    self.label_voz.configure(text_color="#FF5C00")
                    self.voz_ativa.configure(progress_color="#FF5C00")
                    self.cores_fundo.configure(fg_color="#FF5C00", button_color="#FF5C00", button_hover_color="#EB5A05")
                    cor_escolhida = "#FFDE21"
                    atualiza_cor(cor_escolhida)
                elif cor == "Melancia":
                    self.entrada_hexa.configure(text_color="Black", placeholder_text="Digite a cor hexa...", placeholder_text_color="#FC6C85", border_color="#FC6C85", fg_color="white")
                    self.label_aviso_reinic.configure(text_color="white")
                    self.frame_config.configure(fg_color="#008000")
                    self.botao_voltar_config.configure(fg_color="#FC6C85", hover_color="#F26A81")
                    self.botao_enviar_hexa.configure(fg_color="#FC6C85", hover_color="#F26A81")
                    alerta = CTkImage(Image.open(os.path.join(imagem_pasta, "alerta_verde.png")), size=(17, 17))
                    self.alert.configure(image=alerta)
                    self.label_config.configure(text_color="#FC6C85")
                    self.label_config.configure(text_color="#FC6C85")
                    self.label_voz.configure(text_color="#FC6C85")
                    self.voz_ativa.configure(progress_color="#FC6C85")
                    self.cores_fundo.configure(fg_color="#FC6C85", button_color="#FC6C85", button_hover_color="#F26A81")
                    cor_escolhida = "#008000"
                    atualiza_cor(cor_escolhida)
                elif cor == "Algodão-Doce":
                    self.entrada_hexa.configure(text_color="Black", placeholder_text="Digite a cor hexa...", placeholder_text_color="#1093D4", border_color="#1093D4", fg_color="white")
                    self.label_aviso_reinic.configure(text_color="#F4EFEF")
                    self.frame_config.configure(fg_color="#FFB0E0")
                    self.botao_voltar_config.configure(fg_color="#1093D4", hover_color="#0c4478")
                    self.botao_enviar_hexa.configure(fg_color="#1093D4", hover_color="#0c4478")
                    alerta = CTkImage(Image.open(os.path.join(imagem_pasta, "alerta_azul.png")), size=(17, 17))
                    self.alert.configure(image=alerta)
                    self.label_config.configure(text_color="#1093D4")
                    self.label_config.configure(text_color="#1093D4")
                    self.label_voz.configure(text_color="#1093D4")
                    self.voz_ativa.configure(progress_color="#1093D4")
                    self.cores_fundo.configure(fg_color="#1093D4", button_color="#1093D4", button_hover_color="#0c4478")
                    cor_escolhida = "#FFB0E0"
                    atualiza_cor(cor_escolhida)
                elif cor == "Urso De Pelúcia":
                    self.entrada_hexa.configure(text_color="Black", placeholder_text="Digite a cor hexa...", placeholder_text_color="#E08543", border_color="#E08543", fg_color="white")
                    self.label_aviso_reinic.configure(text_color="white")
                    self.frame_config.configure(fg_color="#895129")
                    self.botao_voltar_config.configure(fg_color="#1093D4", hover_color="#D27D40")
                    self.botao_enviar_hexa.configure(fg_color="#1093D4", hover_color="#D27D40")
                    alerta = CTkImage(Image.open(os.path.join(imagem_pasta, "alerta_marrom.png")), size=(17, 17))
                    self.alert.configure(image=alerta)
                    self.label_config.configure(text_color="#E08543")
                    self.label_config.configure(text_color="#E08543")
                    self.label_voz.configure(text_color="#E08543")
                    self.voz_ativa.configure(progress_color="#E08543")
                    self.cores_fundo.configure(fg_color="#E08543", button_color="#E08543", button_hover_color="#D27D40")
                    cor_escolhida = "#895129"
                    atualiza_cor(cor_escolhida)
                elif cor == "Azul Meia-Noite\n Intenso":
                    self.entrada_hexa.configure(text_color="Black", placeholder_text="Digite a cor hexa...", placeholder_text_color="#105ba0", border_color="#105ba0", fg_color="#000127")
                    self.label_aviso_reinic.configure(text_color="white")
                    self.entrada_hexa._entry.configure(insertbackground="#105ba0")
                    self.frame_config.configure(fg_color="#000127")
                    self.botao_voltar_config.configure(fg_color="#105ba0", hover_color="#0c4478")
                    self.botao_enviar_hexa.configure(fg_color="#105ba0", hover_color="#0c4478")
                    alerta = CTkImage(Image.open(os.path.join(imagem_pasta, "alerta_azulmn.png")), size=(17, 17))
                    self.alert.configure(image=alerta)
                    self.label_config.configure(text_color="#105ba0")
                    self.label_config.configure(text_color="#105ba0")
                    self.label_voz.configure(text_color="#105ba0")
                    self.voz_ativa.configure(progress_color="#105ba0")
                    self.cores_fundo.configure(fg_color="#105ba0", button_color="#105ba0", button_hover_color="#0c4478")
                    cor_escolhida = "#000127"
                    atualiza_cor(cor_escolhida)
                elif cor == "Padrão":
                    self.entrada_hexa.configure(text_color="Black", border_color="#105ba0", placeholder_text="Digite a cor hexa...", placeholder_text_color="#105ba0", fg_color="white")
                    self.label_aviso_reinic.configure(text_color="black")
                    self.entrada_hexa._entry.configure(insertbackground="#105ba0")
                    self.frame_config.configure(fg_color="#EEEBEB")
                    alerta = CTkImage(Image.open(os.path.join(imagem_pasta, "alerta_padrao.png")), size=(17, 17))
                    self.alert.configure(image=alerta)
                    cor_escolhida = "#EEEBEB"
                    atualiza_cor(cor_escolhida)
        
            def hashtag_at(evento):
                texto = self.entrada_hexa.get()
                if len(texto) == 0:
                    self.entrada_hexa.insert(0, "#")

            def valida_hexa():
                num_hexa = self.entrada_hexa.get()
                def tira_erro_tamanho():
                    self.erro_tamanho.destroy()
                    self.botao_enviar_hexa.configure(state=NORMAL)
                    self.entrada_hexa.configure(border_color=cbp)
                    self.label_voz.pack(pady=7)
                def tira_erro_alpha():
                    self.erro_alpha_gradiente.destroy()
                    self.botao_enviar_hexa.configure(state=NORMAL)
                    self.entrada_hexa.configure(border_color=cbp)
                    self.label_voz.pack(pady=7)
                def tira_erro_caracteres():
                    self.erro_caractere.destroy()
                    self.botao_enviar_hexa.configure(state=NORMAL)
                    self.entrada_hexa.configure(border_color=cbp)
                    self.label_voz.pack(pady=7)
                def tira_erro_hash():
                    self.erro_hash.destroy()
                    self.botao_enviar_hexa.configure(state=NORMAL)
                    self.entrada_hexa.configure(border_color=cbp)
                    self.label_voz.pack(pady=7)
                if len(num_hexa) > 7:
                    self.entrada_hexa.configure(border_color="red")
                    self.erro_alpha_gradiente = CTkLabel(self.frame_config, text="Erro: Não suportamos valores Alpha!", text_color="#E21010", font=fonte_erros_inter)
                    self.label_voz.pack(pady=26)
                    self.erro_alpha_gradiente.place(x=70, y=225)
                    self.after(2500, tira_erro_alpha)
                elif len(num_hexa) < 7:
                    self.entrada_hexa.configure(border_color="red")
                    self.erro_tamanho = CTkLabel(self.frame_config, text="Erro: Valor pequeno demais!", text_color="#E21010", font=fonte_erros_inter)
                    self.label_voz.pack(pady=26)
                    self.erro_tamanho.place(x=100, y=225)
                    self.botao_enviar_hexa.configure(state=DISABLED)
                    self.after(2500, tira_erro_tamanho)
                elif num_hexa[0] != "#":
                    self.entrada_hexa.configure(border_color="red")
                    self.erro_hash = CTkLabel(self.frame_config, text="Erro: Verifique Se Tem Hashtag No Início!", text_color="#E21010",font=fonte_erros_inter)
                    self.label_voz.pack(pady=26)
                    self.erro_hash.place(x=60, y=225)
                    self.after(2500, tira_erro_hash)
                elif any(x in caracteres_invalidos_hexa for x in num_hexa):
                    erro_caractere = CTkLabel(self, text="Erro: Caracteres Inválidos!", text_color="#E21010", font=fonte_erros_inter)
                    self.label_voz.pack(pady=26)
                    erro_caractere.place(x=160, y=225)
                    self.botao_enviar_hexa.configure(state=DISABLED)
                    self.after(2500, tira_erro_caracteres)
                else:
                    self.configure(fg_color=num_hexa)
                    self.frame_config.configure(fg_color=num_hexa)
                    atualiza_cor(num_hexa)

            padrao = StringVar(value=pev)
            def estado_voz():
                estado_atual = self.voz_ativa.get()
                if estado_atual == "Ativa":
                    self.voz_ativa.configure(text="Ativa")
                    atualiza_estado_voz(estado_atual)
                else:
                    self.voz_ativa.configure(text="Desativada")
                    atualiza_estado_voz(estado_atual)

            self.title("Sponte Study")
            self.frame_config = CTkScrollableFrame(self, width=440, height=310, fg_color=pg)
            self.frame_config.place(x=14, y=8)

            self.label_config = CTkLabel(self.frame_config, text="Configurações", text_color=cls, font=fonte_hora)
            self.label_config.pack(pady=22)
            self.alert = CTkLabel(self.frame_config, image=alerta, text=None)
            self.alert.place(x=77, y=91)
            self.label_aviso_reinic = CTkLabel(self.frame_config, text="As mudanças serão aplicadas após\n você reiniciar o app.", font=fonte_erros_inter, text_color=ct)
            self.label_aviso_reinic.pack(pady=5)
            self.cores_fundo = CTkOptionMenu(self.frame_config, values=["Padrão", "Noite", "Branco", "Amor", "Azul", "Praia", "Melancia", "Algodão-Doce", "Urso De Pelúcia", "Azul Meia-Noite\n Intenso"], corner_radius=15, cursor="hand2", height=25, fg_color=cls, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=cor_fundo)
            self.cores_fundo.set("Sua Cor De Fundo...")
            self.cores_fundo.pack(pady=8)
            self.entrada_hexa = CTkEntry(self.frame_config, placeholder_text="Digite a cor hexa...", placeholder_text_color=cbp, corner_radius=15, border_color=cbp, width=140, text_color=cth, fg_color=cf)
            self.entrada_hexa.pack(pady=8)
            self.entrada_hexa.bind("<Enter>", hashtag_at)
            self.entrada_hexa._entry.configure(insertbackground=cbp)
            self.botao_enviar_hexa = CTkButton(self.frame_config, text="Validar", text_color=ctb, fg_color=cls, border_color="black", border_width=2, corner_radius=23, width=4, height=19, cursor="hand2", command=valida_hexa, hover_color=ch)
            self.botao_enviar_hexa.place(x=295, y=189)
            self.botao_voltar_config = CTkButton(self.frame_config, text="Voltar", text_color=ctb, fg_color=cls, border_color="black", border_width=2, corner_radius=20, width=4, height=22, cursor="hand2", command=voltar_config, hover_color=ch)
            self.botao_voltar_config.place(x=1, y=0)
            self.label_voz = CTkLabel(self.frame_config, text="Voz", font=fonte_hora, text_color=cls)
            self.label_voz.pack(pady=7)
            self.voz_ativa = CTkSwitch(self.frame_config, text="Ativa", cursor="hand2", variable=padrao, command=estado_voz, onvalue="Ativa", offvalue="Desativada", text_color=ct, progress_color=cls)
            self.voz_ativa.pack(pady=7)
            if pev == "Ativa":
                self.voz_ativa.configure(text="Ativa")
            else:
                self.voz_ativa.configure(text="Desativada")
            self.creditos = CTkLabel(self.frame_config, text="Imagens de Freepik.", text_color=ct, font=fonte_ajuda)
            self.creditos.pack(pady=2)
            self.link_creditos = CTkLabel(self.frame_config, text="Acesse: https://br.freepik.com/app", text_color=ct, font=fonte_14)
            self.link_creditos.pack(pady=4)

        self.frame_central = CTkFrame(self, width=280, height=260, fg_color=pg)
        self.frame_central.pack(pady=22)
        self.label_hora = CTkLabel(self.frame_central, width=230, height=120, text=horario_atual, text_color=cls, font=fonte_hora, bg_color="transparent", corner_radius=20)
        self.label_hora.place(x=21, y=20)
        self.label_data = CTkLabel(self.frame_central, width=100, height=50, bg_color="transparent", text=data_atual, font=fonte_data, text_color=ct)
        self.label_data.place(x=66, y=110)
        self.botao_notas = CTkButton(self.frame_central, text="Notas", text_color=ctb, width=30, cursor="hand2", fg_color=cls, border_color="black", border_width=2, corner_radius=15, command=notas, hover_color=ch)
        self.botao_notas.place(x=55, y=160)
        self.botao_configuracoes = CTkButton(self.frame_central, text="Config", text_color=ctb, width=30, cursor="hand2",fg_color=cls, border_color="black", border_width=2, corner_radius=15, command=config, hover_color=ch)
        self.botao_configuracoes.place(x=153, y=160)
        self.label_ajuda = CTkLabel(self.frame_central, text="Seu app de organização\ncom voz 100% offline", font=fonte_ajuda, text_color=ct)
        self.label_ajuda.place(x=55, y=210)
        self.botao_configuracoes.bind("<Enter>", explica_config_entra)
        self.botao_configuracoes.bind("<Leave>", explica_config_fora)
        self.botao_notas.bind("<Enter>", explica_notas_entra)
        self.botao_notas.bind("<Leave>", explica_notas_fora)

        self.after(500, saudacao_gui)
        self.after(800, atualizar_hora_GUI)
        self.after(800, atualiza_dia_back)
        self.after(1200, atualiza_hora)
        self.after(200, reiniciar_saudacao)

janela_i = janela_inic()
janela_i.mainloop()
existe_dados = verificar_dados()
if existe_dados == False:
    janela_princi = janela_principal()
    janela_princi.mainloop()
else:
    janela_pr = janela_preench()
    janela_pr.mainloop()
    if feito == True:
        janela_princi = janela_principal()
        janela_princi.mainloop()