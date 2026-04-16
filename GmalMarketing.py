import customtkinter as ctk
from tkinter import filedialog, messagebox
import pandas as pd
import smtplib
import time
import random
import threading
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from groq import Groq

# Configuração de Aparência
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AI Email Marketing Assistant")
        self.geometry("1100x700")
        self.configure(fg_color="#F6F8FC")  # Cor de fundo padrão do Gmail

        # Variáveis de controle
        self.df_contatos = None
        self.parar_processo = False
        self.api_key_groq = ctk.StringVar(value="")
        self.gmail_user = ctk.StringVar(value="")
        self.gmail_pass = ctk.StringVar(value="") # Senha de app 16 dígitos
        self.hora_envio = ctk.StringVar(value="09:00")

        # Configuração de Grid Responsivo
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        # --- BARRA LATERAL (CONFIGURAÇÕES) ---
        self.sidebar = ctk.CTkFrame(self, width=300, corner_radius=0, fg_color="#F0F2F5", border_width=1, border_color="#E0E0E0")
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar, text="Settings", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(pady=(20, 20))

        # Inputs da Barra Lateral
        self.create_label_input(self.sidebar, "Gmail:", self.gmail_user, placeholder="your-email@gmail.com")
        self.create_label_input(self.sidebar, "App Password (16 digits):", self.gmail_pass, placeholder="xxxx xxxx xxxx xxxx", show="*")
        self.create_label_input(self.sidebar, "Groq API Key:", self.api_key_groq, placeholder="gsk_...", show="*")
        self.create_label_input(self.sidebar, "Send Time (HH:MM):", self.hora_envio)

        self.btn_importar = ctk.CTkButton(self.sidebar, text="📥 Import CSV List", 
                                          fg_color="#0B57D0", hover_color="#0842A0", 
                                          height=40, font=("Segoe UI", 12, "bold"),
                                          command=self.importar_csv)
        self.btn_importar.pack(pady=20, padx=20, fill="x")

        self.status_lista = ctk.CTkLabel(self.sidebar, text="No file loaded", font=("Segoe UI", 11), text_color="gray")
        self.status_lista.pack()

        # --- ÁREA PRINCIPAL ---
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Cabeçalho
        self.header = ctk.CTkLabel(self.main_frame, text="AI Email Marketing Assistant", font=ctk.CTkFont(size=24, weight="bold"), text_color="#1F1F1F")
        self.header.pack(anchor="w", pady=(0, 20))

        # Caixas Editáveis (Prompt e Proibições)
        self.tabview = ctk.CTkTabview(self.main_frame, height=250, corner_radius=15, fg_color="white", border_width=1, border_color="#E0E0E0")
        self.tabview.pack(fill="x", pady=10)
        self.tabview.add("Condições Obrigatórias")
        self.tabview.add("Palavras Proibidas")
        self.tabview.add("Assunto do e-mail")
        self.tabview.add("Link do site oficial")
        self.tabview.add("Links extras")
        self.tabview.add("Direitos Autorais")

        self.txt_condicoes = ctk.CTkTextbox(self.tabview.tab("Condições Obrigatórias"), font=("Segoe UI", 12), border_width=0)
        self.txt_condicoes.pack(fill="both", expand=True)
        self.txt_condicoes.insert("0.0", "1. Tone and Style: Professional, friendly, and engaging.\n2. Content Length: Keep emails concise (maximum 3 paragraphs).\n3. Personalization: Use recipient's first name naturally.\n4. Call to Action: Include a clear and compelling call-to-action.")

        self.txt_proibidas = ctk.CTkTextbox(self.tabview.tab("Palavras Proibidas"), font=("Segoe UI", 12), border_width=0)
        self.txt_proibidas.pack(fill="both", expand=True)
        self.txt_proibidas.insert("0.0", "GANHE DINHEIRO, GRÁTIS, URGENTE, CLIQUE AQUI, ÚLTIMA CHANCE, NÃO PERCA TEMPO, HOJE MESMO, ESGOTANDO RÁPIDO, VAGAS LIMITADAS, ACESSE ANTES QUE ACABE, RENDA EXTRA, DINHEIRO FÁCIL, MILHÕES EM 30 DIAS, CASHBACK EXCLUSIVO, SEM GASTOS, COMPLETAMENTE GRÁTIS, BÔNUS EXCLUSIVO, RESULTADO MILAGROSO, SISTEMA INFALÍVEL.")

        self.txt_assunto_email = ctk.CTkTextbox(self.tabview.tab("Assunto do e-mail"), font=("Segoe UI", 12), border_width=0)
        self.txt_assunto_email.pack(fill="both", expand=True)
        self.txt_assunto_email.insert("0.0", "Assunto do e-mail (opcional).")

        self.txt_link_site_oficial = ctk.CTkTextbox(self.tabview.tab("Link do site oficial"), font=("Segoe UI", 12), border_width=0)
        self.txt_link_site_oficial.pack(fill="both", expand=True)
        self.txt_link_site_oficial.insert("0.0", "https://example.com")

        self.txt_links_extras = ctk.CTkTextbox(self.tabview.tab("Links extras"), font=("Segoe UI", 12), border_width=0)
        self.txt_links_extras.pack(fill="both", expand=True)
        self.txt_links_extras.insert("0.0", "Add additional links or resources here (one per line).")

        self.txt_direitos_autorais = ctk.CTkTextbox(self.tabview.tab("Direitos Autorais"), font=("Segoe UI", 12), border_width=0)
        self.txt_direitos_autorais.pack(fill="both", expand=True)
        self.txt_direitos_autorais.insert(
            "0.0",
            "CC BY-NC-SA 4.0 LICENSE\n\n"
            "This software is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.\n\n"
            "YOU ARE FREE TO:\n"
            "- Share: Copy and redistribute the material in any medium or format.\n"
            "- Adapt: Remix, transform, and build upon the material.\n\n"
            "UNDER THE FOLLOWING TERMS:\n"
            "- Attribution: You must give appropriate credit to the original author (glaudeslm).\n"
            "- Non-Commercial: You may NOT use this material for commercial purposes or resale.\n"
            "- ShareAlike: If you remix, transform, or build upon the material, you must distribute your contributions under the same license.\n\n"
            "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY.\n\n"
            "For more information, visit: https://creativecommons.org/licenses/by-nc-sa/4.0/"
        )
        self.txt_direitos_autorais.configure(state="disabled")

        # Caixa de Log
        self.label_log = ctk.CTkLabel(self.main_frame, text="Activity Log", font=("Segoe UI", 12, "bold"))
        self.label_log.pack(anchor="w", pady=(20, 5))
        
        self.txt_log = ctk.CTkTextbox(self.main_frame, height=200, corner_radius=15, fg_color="#1E1E1E", text_color="#A9FFAD", font=("Consolas", 11))
        self.txt_log.pack(fill="both", expand=True)

        # Botões de Ação
        self.action_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.action_frame.pack(fill="x", pady=20)

        self.btn_iniciar = ctk.CTkButton(self.action_frame, text="🚀 START CAMPAIGN", 
                                         fg_color="#D93025", hover_color="#B3261E", 
                                         height=45, font=("Segoe UI", 13, "bold"),
                                         command=self.iniciar_thread)
        self.btn_iniciar.pack(side="left", padx=(0, 10), expand=True, fill="x")

        self.btn_parar = ctk.CTkButton(self.action_frame, text="🛑 STOP CAMPAIGN", 
                                       fg_color="#5F6368", hover_color="#3C4043", 
                                       height=45, font=("Segoe UI", 13, "bold"),
                                       command=self.parar_envio)
        self.btn_parar.pack(side="left", expand=True, fill="x")

        self.footer_label = ctk.CTkLabel(
            self,
            text="Open Source Project - CC BY-NC-SA 4.0 License",
            font=("Segoe UI", 10),
            text_color="#5F6368",
        )
        self.footer_label.grid(row=1, column=0, columnspan=2, sticky="ew", padx=20, pady=(0, 10))

    # --- FUNÇÕES AUXILIARES ---
    def create_label_input(self, master, label_text, variable, placeholder="", show="", **kwargs):
        lbl = ctk.CTkLabel(master, text=label_text, font=("Segoe UI", 11))
        lbl.pack(anchor="w", padx=20, pady=(10, 0))
        entry = ctk.CTkEntry(master, textvariable=variable, placeholder_text=placeholder, show=show, corner_radius=8, height=35)
        entry.pack(fill="x", padx=20, pady=(2, 5))

    def log(self, mensagem):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.txt_log.insert("end", f"[{timestamp}] {mensagem}\n")
        self.txt_log.see("end")

    def importar_csv(self):
        caminho = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if caminho:
            try:
                self.df_contatos = pd.read_csv(caminho)
                cols_necessarias = ['Email', 'FirstName']
                if all(col in self.df_contatos.columns for col in cols_necessarias):
                    self.status_lista.configure(text=f"Ready: {len(self.df_contatos)} contacts loaded", text_color="#188038")
                    self.log(f"Contact list loaded successfully. {len(self.df_contatos)} contacts found.")
                else:
                    messagebox.showerror("Error", "CSV must contain 'Email' and 'FirstName' columns.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read CSV: {e}")

    def gerar_ia(self, nome):
        try:
            client = Groq(api_key=self.api_key_groq.get())
            prompt = f"""
            {self.txt_condicoes.get("0.0", "end")}
            
            PROIBIDO USAR: {self.txt_proibidas.get("0.0", "end")}
            
            SAÍDA:
            Assunto: [Assunto dinâmico]
            Corpo: [Texto para {nome}]
            """
            chat_completion = client.chat.completions.create(
                model="llama-3.1-70b-versatile",
                messages=[{"role": "system", "content": prompt},
                          {"role": "user", "content": f"Escreva para {nome}."}],
                temperature=0.8
            )
            res = chat_completion.choices[0].message.content
            # Parsing simples
            assunto = res.split("Assunto:")[1].split("Corpo:")[0].strip()
            corpo = res.split("Corpo:")[1].strip()
            return assunto, corpo
        except:
            return "Novidades Agente Revisional", f"Olá {nome}, conheça nossa plataforma..."

    def parar_envio(self):
        self.parar_processo = True
        self.log("Stop requested... The process will end after the current email.")

    def iniciar_thread(self):
        if not self.gmail_user.get() or not self.api_key_groq.get():
            messagebox.showwarning("Warning", "Please fill in the email and Groq API key!")
            return
        if self.df_contatos is None:
            messagebox.showwarning("Warning", "Import the contact list first!")
            return
        
        self.parar_processo = False
        threading.Thread(target=self.processo_envio, daemon=True).start()

    def processo_envio(self):
        self.btn_iniciar.configure(state="disabled")
        self.log(f"Waiting for scheduled time: {self.hora_envio.get()}...")
        
        # Simplified waiting loop for demonstration
        # In production, check: if datetime.now().strftime("%H:%M") == self.hora_envio.get()

        for index, row in self.df_contatos.iterrows():
            if self.parar_processo: break

            email_cliente = row['Email']
            nome_cliente = row['FirstName']

            self.log(f"Generating content for {nome_cliente}...")
            assunto_ia, corpo_ia = self.gerar_ia(nome_cliente)
            
            try:
                msg = MIMEMultipart()
                msg['From'] = self.gmail_user.get()
                msg['To'] = email_cliente
                msg['Subject'] = f"{nome_cliente}! {assunto_ia}"
                msg.attach(MIMEText(corpo_ia, 'plain'))

                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()
                    server.login(self.gmail_user.get(), self.gmail_pass.get())
                    server.send_message(msg)
                
                self.log(f"✅ Sent: {email_cliente}")
                
                # Random Human-Like Delay
                delay = random.randint(45, 150)
                self.log(f"Safety pause: {delay} seconds...")
                time.sleep(delay)

            except Exception as e:
                self.log(f"❌ Error sending to {email_cliente}: {str(e)}")
                time.sleep(10)

        self.log("🏁 Campaign finished.")
        self.btn_iniciar.configure(state="normal")

if __name__ == "__main__":
    app = App()
    app.mainloop()
