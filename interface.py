from customtkinter import *
from CTkToolTip import *
from assistente import *
import threading
from PIL import Image

class janela_inic(CTk):
    def __init__(self):
        super().__init__()
        banco_user()
        self.title("Sponte Study")
        self.geometry("400x270")
        self.resizable(width=False, height=False)
        #Ícone das janelas
        self.iconbitmap("imagens/logo.ico")
         
        self.fonte_titulo = CTkFont(family="Helvetica", size=35, weight="bold")
        self.fonte_inic = CTkFont(family="Arial", size=20)
        self.label_logus = CTkLabel(self, text="Sponte Study", text_color="#105ba0", font=(self.fonte_titulo))
        self.label_logus.pack(pady=30)
        self.inicializacao = CTkLabel(self, text="Inicializando...", text_color="#105ba0", font=(self.fonte_inic))
        self.inicializacao.pack(pady=40)
        self.bem_vindo = CTkLabel(self, text="Seja Bem Vindo", text_color="#105ba0", font=(self.fonte_inic))

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
        #Ícone para todas as janelas
        self.iconbitmap("imagens/logo.ico")

        self.fonte_conhecer = CTkFont(family="Helvetica", size=30, weight="bold")
        self.fonte_erros = CTkFont(family="Arial", size=20, weight="bold")
                        
        self.titulo = CTkLabel(self, text="Conhecendo-te", font=(self.fonte_conhecer), text_color="#105ba0")

        def inserirbarra(evento):
            data_niver = self.data_nasci.get().strip()
            if len(data_niver) == 0:
                self.data_nasci.insert(0, "dd/mm") 
                        
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
        self.geometry("420x300")
        self.resizable(width=False, height=False)
        self.title("Sponte Study")
        #Ícone para todas as janelas
        self.iconbitmap("imagens/logo.ico")

        pg = pega_cor()
        ct = cor_texto()
        ctb = cor_texto_botao()
        ctt = cor_texto_tooltip()
        cf = cor_fundo()
        cbp = cor_borda_place()
        cls = cor_labels()
        ch = cor_hover()
        cn = cor_notas()
        caminho_alerta = imagem_cor()
        self.configure(fg_color=pg)

        caracteres_invalidos_hexa = ('!', '@', '$', '%', '"', '&', '*', '()', '=', '+', '[]', '{}', ':', ';', ',', '.', '|', '\\', '?', '_')

        alerta = CTkImage(light_image=Image.open(caminho_alerta), dark_image=Image.open(caminho_alerta), size=(17, 17))

        #Definindo a fonte da hora
        fonte_hora = CTkFont(family="Arial", size=40, weight="bold")
        #Fonte da data
        fonte_data = CTkFont(family="Arial", size=18, weight="bold")
        #Fonte de erros internos
        fonte_erros_inter = CTkFont(family="Arial", size=15, weight="bold")
        #Fonte do label ajuda
        fonte_ajuda = CTkFont(family="Arial", size=15, weight="bold")
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
                self.label_dia.place(x=69, y=15)
                faloud = True
                hora_da_fala_dia(faloud)
                self.after(1500, tira_labeld)
            elif vft == False and hora_gui >= 13 and hora_gui < 18:
                def tira_labelt():
                    self.label_tarde.destroy()
                self.label_tarde = CTkLabel(self.frame_central, text=f"Boa tarde {n}!", width=90, height=20, text_color=ct, font=fonte_data)
                self.label_tarde.place(x=69, y=15)
                faloudt = True
                hora_da_fala_tarde(faloudt)
                self.after(1500, tira_labelt)
            elif vfn == False and hora_gui >= 18 and hora_gui < 0:
                def tira_labeln():
                    self.label_noite.destroy()
                self.label_noite = CTkLabel(self.frame_central, text=f"Bom noite {n}!", width=90, height=20, text_color=ct, font=fonte_data)
                self.label_noite.place(x=69, y=15)
                faloun = True
                hora_da_fala_dia(faloun)
                self.after(1500, tira_labeln)
        
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
                        fonte = self.tamanho_fonte.get()
                        data_c = data_atual_nota
                        materia = self.tipo_nota.get()
                        if fonte == "Tamanho Da Fonte...":
                            fonte = 12
                        if materia == "Tipo De Notas...":
                            materia = "Outros Estudos"
                        if len(titulo) > 3 and len(titulo) < 30 and len(anotacao) > 3 and len(anotacao) < 500:
                            guarda_titulo_nota(titulo, anotacao, fonte, data_c, materia)
                            verificacao = verifica_guarda_titulo()
                            if verificacao == False:
                                def tira_salvo():
                                    self.label_salvo.destroy()
                                    self.texto.delete("1.0", "end")
                                    self.titulo.delete(0, "end")
                                    self.tipo_nota.set("Tipo De Notas...")
                                    self.tamanho_fonte.set("Tamanho Da Fonte...")
                                self.label_salvo = CTkLabel(self.frame_anota, text="Salvo com sucesso!!", text_color="#2E6F40", font=fonte_erros_inter, fg_color="#CFFFDC")
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
                            self.tipo_nota.configure(fg_color="#FFD32C", button_color="#FFD32C", button_hover_color="#DEB623")
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

                    self.frame_notas.place_forget()
                    self.frame_anota = CTkFrame(self, width=390, height=260, fg_color=pg)
                    self.frame_anota.pack(pady=20)
                    self.botao_voltar_anotas = CTkButton(self.frame_anota, text="Voltar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=voltar_anota, hover_color=ch)
                    self.botao_voltar_anotas.place(x=330, y=1)
                    self.tipo_nota = CTkOptionMenu(self.frame_anota, width=90, cursor="hand2", values=["Português", "Matemática", "História", "Geografia", "Ciências", "Inglês", "Outros Estudos"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=muda_titulo)
                    self.tipo_nota.place(x=240, y=40)
                    self.tamanho_fonte = CTkOptionMenu(self.frame_anota, width=90, cursor="hand2", values=["8","10", "12", "14", "16", "18", "20", "22"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=fonte_tamanho)
                    self.tamanho_fonte.place(x=225, y=80)
                    self.tamanho_fonte.set("Tamanho Da Fonte...")
                    self.tipo_nota.set("Tipo De Notas...")
                    self.titulo = CTkEntry(self.frame_anota, width=212, placeholder_text="Título...", corner_radius=10, border_color=cbp, placeholder_text_color=cbp, text_color=ctt, fg_color=cf)
                    self.titulo.place(x=10, y=40)
                    self.texto = CTkTextbox(self.frame_anota, width=210, height=170, border_width=2, border_color=cbp, corner_radius=10, text_color=ctt, fg_color=cf)
                    self.texto.place(x=10, y=80)
                    self.texto.insert("0.0", "Hoje aprendi sobre...")
                    CTkToolTip(self.texto, message="Clique o botão direito do mouse", alpha=0.81, text_color=ctt, bg_color=cf)
                    self.texto.bind("<Button-3>", apaga_texto)
                    self.botao_salvar = CTkButton(self.frame_anota, text="Salvar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=salvar_texto, hover_color=ch)
                    self.botao_salvar.place(x=230, y=225)
                    
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
                        self.tipo_nota_e.configure(fg_color="#FFD32C", button_color="#FFD32C", button_hover_color="#DEB623")
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
                    tipo_nota = self.tipo_nota_e.get()
                    fonte_e = self.tamanho_fonte_e.get()
                    salvando = salvar_edicao(data_edicao_nota, id, titulo_e, texto_e, tipo_nota, fonte_e)
                    if salvando == True:
                        self.label_sal = CTkLabel(self.frame_edita, text="Salvo com sucesso!!", text_color="#2E6F40", font=fonte_erros_inter, fg_color="#CFFFDC")
                        self.label_sal.place(x=210, y=5)
                        self.after(1000, tira_sal)
                    
                def voltar_anotacao():
                    self.frame_edita.pack_forget()
                    self.entrada_titulo_e.delete(0, "end")
                    self.texto_e.delete(0.0, "end")
                    self.tamanho_fonte_e.destroy()
                    self.tipo_nota_e.destroy()
                    self.frame_notas.place(x=20, y=0)
                    frame_anotacao.pack(pady=5)

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
                self.frame_edita = CTkFrame(self, width=390, height=310, fg_color=pg)
                self.frame_edita.pack(pady=20)
                self.tamanho_fonte_e = CTkOptionMenu(self.frame_edita, width=90, cursor="hand2", values=["8","10", "12", "14", "16", "18", "20", "22"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=fonte_tamanho_e)
                self.entrada_titulo_e = CTkEntry(self.frame_edita, width=212, corner_radius=10, border_color=cbp, placeholder_text_color=cbp, text_color="black", fg_color=cf, font=fonte_e)
                self.texto_e = CTkTextbox(self.frame_edita, width=210, height=170, border_width=2, border_color=cbp, corner_radius=10, text_color="black", fg_color=cf, font=fonte_e)
                self.tipo_nota_e = CTkOptionMenu(self.frame_edita, width=90, cursor="hand2", values=["Português", "Matemática", "História", "Geografia", "Ciências", "Inglês", "Outros Estudos"], fg_color=cls, height=25, corner_radius=15, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=muda_titulo_e)
                self.botao_deletar_e = CTkButton(self.frame_edita, text="Deletar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=deletar, hover_color=ch)
                self.botao_salvar_e = CTkButton(self.frame_edita, text="Salvar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=salvar_e, hover_color=ch)
                self.botao_voltar_e = CTkButton(self.frame_edita, text="Voltar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=voltar_anotacao, hover_color=ch)
                self.texto_e.insert("0.0", texto_frame)
                self.entrada_titulo_e.insert(0, titulo_frame)
                self.tamanho_fonte_e.set(fonte_frame)
                self.tipo_nota_e.set(materia_frame)
                self.entrada_titulo_e.place(x=10, y=41)
                self.texto_e.place(x=10, y=79)
                if materia_frame == "Tipo De Notas..." or materia_frame == "Outros Estudos":
                    self.tipo_nota_e.place(x=257, y=100)
                else:
                    self.tipo_nota_e.place(x=280, y=100)   
                self.botao_voltar_e.place(x=1, y=1) 
                self.tamanho_fonte_e.place(x=280, y=41)
                self.botao_salvar_e.place(x=304, y=220)
                self.botao_deletar_e.place(x=230, y=220)

            self.frame_notas = CTkScrollableFrame(self, width=370, height=280, fg_color=pg)
            self.frame_notas.place(x=20, y=0)
            self.frame_guarda_notas = CTkFrame(self.frame_notas, width=340, height=50, fg_color=pg)
            self.frame_guarda_notas.pack(pady=10)
            self.botao_voltar_notas = CTkButton(self.frame_guarda_notas, text="Voltar", fg_color=cls, width=4, height=22, border_color="black", border_width=2, corner_radius=23, cursor="hand2", command=voltar_notas, hover_color=ch)
            self.botao_voltar_notas.place(x=282, y=1)
            self.botao_cria_nota = CTkOptionMenu(self.frame_guarda_notas, values=["Nota"], fg_color=cls, height=25, cursor="hand2", corner_radius=19, button_color=cls, text_color=ctb, button_hover_color=ch,dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=escolha_comecar)
            self.botao_cria_nota.set("Começar...")
            self.botao_cria_nota.place(x=2, y=13)

            #Pega as notas
            self.lista_nota = pega_notas()
            #Percorre a lista de notas e posiciona os frames com elas.
            for ln in self.lista_nota:
                titulo = ln[1]
                texto = ln[2]
                mtr = ln[3]
                frame_anotacao = CTkFrame(self.frame_notas, width=170, height=110, corner_radius=15, cursor="hand2", fg_color=cn)
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
                    alerta.configure(light_image=Image.open("imagens/alerta_preto.png"), dark_image=Image.open("imagens/alerta_preto.png"))
                    self.botao_voltar_config.configure(fg_color="#5E127F", hover_color="#541070")
                    self.botao_enviar_hexa.configure(fg_color="#5E127F", hover_color="#541070")
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
                    alerta.configure(light_image=Image.open("imagens/alerta_branco.png"), dark_image=Image.open("imagens/alerta_branco.png"))
                    self.botao_voltar_config.configure(fg_color="#105ba0", hover_color="#oc4478")
                    self.botao_enviar_hexa.configure(fg_color="#105ba0", hover_color="#0c4478")
                    self.label_config.configure(text_color="#105ba0")
                    self.label_voz.configure(text_color="#105ba0")
                    self.voz_ativa.configure(progress_color="#105ba0")
                    self.cores_fundo.configure(fg_color="#105ba0", button_color="#105ba0", button_hover_color="#0c4478")
                    cor_escolhida = "#F7F7F7"
                    atualiza_cor(cor_escolhida)
                elif cor == "Amor":
                    self.entrada_hexa.configure(text_color="Black", placeholder_text="Digite a cor hexa...", placeholder_text_color="#F32A2A", border_color="#F32A2A", fg_color="white")
                    self.label_aviso_reinic.configure(text_color="black")
                    self.frame_config.configure(fg_color="#F32A2A")
                    alerta.configure(light_image=Image.open("imagens/alerta_vermelho.png"), dark_image=Image.open("imagens/alerta_vermelho.png"))
                    self.botao_voltar_config.configure(fg_color="#FFBFBF", hover_color="#F1B7B7")
                    self.botao_enviar_hexa.configure(fg_color="#FFBFBF", hover_color="#F1B7B7")
                    self.label_config.configure(text_color="#FFBFBF")
                    self.label_voz.configure(text_color="#FFBFBF")
                    self.voz_ativa.configure(progress_color="#FFBFBF")
                    self.cores_fundo.configure(fg_color="#FFBFBF", button_color="#FFBFBF", button_hover_color="#F1B7B7")
                    cor_escolhida = "#F32A2A"
                    atualiza_cor(cor_escolhida)
                elif cor == "Azul":   
                    self.entrada_hexa.configure(text_color="Black", placeholder_text="Digite a cor hexa...", placeholder_text_color="#1093D4", border_color="#1093D4", fg_color="white")   
                    self.label_aviso_reinic.configure(text_color="white")
                    self.frame_config.configure(fg_color="#1093D4")
                    alerta.configure(light_image=Image.open("imagens/alerta_azul.png"), dark_image=Image.open("imagens/alerta_azul.png"))
                    self.botao_voltar_config.configure(fg_color="#105ba0", hover_color="#0c4478")
                    self.botao_enviar_hexa.configure(fg_color="#105ba0", hover_color="#0c4478")
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
                    alerta.configure(light_image=Image.open("imagens/alerta_amarelo.png"), dark_image=Image.open("imagens/alerta_amarelo.png"))
                    self.botao_voltar_config.configure(fg_color="#FF5C00", hover_color="#EB5A05")
                    self.botao_enviar_hexa.configure(fg_color="#FF5C00", hover_color="#EB5A05")
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
                    alerta.configure(light_image=Image.open("imagens/alerta_verde.png"), dark_image=Image.open("imagens/alerta_verde.png"), size=(17, 17))
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
                    alerta.configure(light_image=Image.open("imagens/alerta_rosa.png"), dark_image=Image.open("imagens/alerta_rosa.png"))
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
                    alerta.configure(light_image=Image.open("imagens/alerta_marrom.png"), dark_image=Image.open("imagens/alerta_marrom.png"))
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
                    alerta.configure(light_image=Image.open("imagens/alerta_azulmn.png"), dark_image=Image.open("imagens/alerta_azulmn.png"))
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
                    alerta.configure(light_image=Image.open("imagens/alerta_padrao.png"), dark_image=Image.open("imagens/alerta_azullogus.png"))
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
                    self.entrada_hexa.configure(border_color="#105ba0")
                    self.creditos.pack(pady=2)
                def tira_erro_alpha():
                    self.erro_alpha_gradiente.destroy()
                    self.botao_enviar_hexa.configure(state=NORMAL)
                    self.entrada_hexa.configure(border_color="#105ba0")
                    self.creditos.pack(pady=2)
                def tira_erro_caracteres():
                    self.erro_caractere.destroy()
                    self.botao_enviar_hexa.configure(state=NORMAL)
                    self.entrada_hexa.configure(border_color="#105ba0")
                    self.creditos.pack(pady=2)
                def tira_erro_hash():
                    self.erro_hash.destroy()
                    self.botao_enviar_hexa.configure(state=NORMAL)
                    self.entrada_hexa.configure(border_color="#105ba0")
                    self.creditos.pack(pady=2)
                if len(num_hexa) > 7:
                    self.entrada_hexa.configure(border_color="red")
                    self.erro_alpha_gradiente = CTkLabel(self.frame_config, text="Erro: Não suportamos valores Alpha!", font=fonte_erros_inter)
                    self.creditos.pack(pady=30)
                    self.erro_alpha_gradiente.place(x=60, y=225)
                    self.after(2500, tira_erro_alpha)
                elif len(num_hexa) < 7:
                    self.entrada_hexa.configure(border_color="red")
                    self.erro_tamanho = CTkLabel(self.frame_config, text="Erro: Valor pequeno demais!", font=fonte_erros_inter)
                    self.creditos.pack(pady=30)
                    self.erro_tamanho.place(x=90, y=225)
                    self.botao_enviar_hexa.configure(state=DISABLED)
                    self.after(2500, tira_erro_tamanho)
                elif num_hexa[0] != "#":
                    self.entrada_hexa.configure(border_color="red")
                    self.erro_hash = CTkLabel(self.frame_config, text="Erro: Verifique Se Tem Hashtag No Início!", font=fonte_erros_inter)
                    self.creditos.pack(pady=8)
                    self.erro_hash.place(x=50, y=225)
                    self.after(2500, tira_erro_hash)
                elif any(x in caracteres_invalidos_hexa for x in num_hexa):
                    erro_caractere = CTkLabel(self, text="Erro: Caracteres Inválidos!", text_color="#E21010", font=fonte_erros_inter)
                    self.creditos.pack(pady=30)
                    erro_caractere.place(x=150, y=225)
                    self.botao_enviar_hexa.configure(state=DISABLED)
                    self.after(2500, tira_erro_caracteres)
                else:
                    self.configure(fg_color=num_hexa)
                    self.frame_config.configure(fg_color=num_hexa)
                    atualiza_cor(num_hexa)

            self.title("Sponte Study")
            self.frame_config = CTkScrollableFrame(self, width=380, height=260, fg_color=pg)
            self.frame_config.place(x=14, y=8)

            self.label_config = CTkLabel(self.frame_config, text="Configurações", text_color=cls, font=fonte_hora)
            self.label_config.pack(pady=22)
            self.alert = CTkLabel(self.frame_config, image=alerta, text=None)
            self.alert.place(x=43, y=91)
            self.label_aviso_reinic = CTkLabel(self.frame_config, text="As mudanças serão aplicadas após\n você reiniciar o app.", font=fonte_erros_inter, text_color=ct)
            self.label_aviso_reinic.pack(pady=5)
            self.cores_fundo = CTkOptionMenu(self.frame_config, values=["Padrão", "Noite", "Branco", "Amor", "Azul", "Praia", "Melancia", "Algodão-Doce", "Urso De Pelúcia", "Azul Meia-Noite\n Intenso"], corner_radius=15, cursor="hand2", height=25, fg_color=cls, button_color=cls, text_color=ctb, button_hover_color=ch, dropdown_fg_color=cls, dropdown_text_color=ctb, dropdown_hover_color=ch, command=cor_fundo)
            self.cores_fundo.set("Sua Cor De Fundo...")
            self.cores_fundo.pack(pady=8)
            self.entrada_hexa = CTkEntry(self.frame_config, placeholder_text="Digite a cor hexa...", placeholder_text_color=cbp, corner_radius=15, border_color=cbp, width=140, text_color=ct, fg_color=cf)
            self.entrada_hexa.pack(pady=8)
            self.entrada_hexa.bind("<Enter>", hashtag_at)
            self.entrada_hexa._entry.configure(insertbackground=cbp)
            self.botao_enviar_hexa = CTkButton(self.frame_config, text="Validar", text_color=ctb, fg_color=cls, border_color="black", border_width=2, corner_radius=23, width=4, height=19, cursor="hand2", command=valida_hexa, hover_color=ch)
            self.botao_enviar_hexa.place(x=270, y=187)
            self.botao_voltar_config = CTkButton(self.frame_config, text="Voltar", text_color=ctb, fg_color=cls, border_color="black", border_width=2, corner_radius=20, width=4, height=22, cursor="hand2", command=voltar_config, hover_color=ch)
            self.botao_voltar_config.place(x=1, y=0)
            self.creditos = CTkLabel(self.frame_config, text="Imagens de Freepik.", text_color=ct, font=fonte_ajuda)
            self.creditos.pack(pady=2)
            self.link_creditos = CTkLabel(self.frame_config, text="Acesse: https://br.freepik.com/app", text_color=ct, font=fonte_14)
            self.link_creditos.pack(pady=4)

        self.frame_central = CTkFrame(self, width=270, height=260, fg_color=pg)
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

        self.after(200, saudacao_gui)
        self.after(800, atualizar_hora_GUI)
        self.after(800, atualiza_dia_back)
        self.after(1200, atualiza_hora)
        self.after(900, reiniciar_saudacao)

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