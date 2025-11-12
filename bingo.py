import tkinter as tk
from tkinter import ttk, messagebox
import random

class BingoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Conferência Eletrônica de Bingos")
        self.master.configure(bg="black")

        # Configuração do jogo
        self.total_bolas = 75          # se quiser 90 é só mudar aqui
        self.bolas_chamadas = []
        self.bolas_restantes = list(range(1, self.total_bolas + 1))
        self.num_labels = {}

        self._criar_layout()
        self._atualizar_tudo()

    def _criar_layout(self):
        # Cabeçalho estilo DOS
        header = tk.Label(
            self.master,
            text="SISTEMATICA   * CONFERÊNCIA ELETRÔNICA DE BINGOS *",
            font=("Consolas", 14, "bold"),
            bg="black",
            fg="yellow"
        )
        header.pack(fill="x", pady=(5, 0))

        sub_header = tk.Label(
            self.master,
            text="Versão Python/Tkinter",
            font=("Consolas", 9),
            bg="black",
            fg="#cccccc"
        )
        sub_header.pack(fill="x")

        # Frame principal
        frame_principal = tk.Frame(self.master, bg="black")
        frame_principal.pack(fill="both", expand=True, padx=10, pady=5)

        frame_principal.columnconfigure(0, weight=3)
        frame_principal.columnconfigure(1, weight=1)
        frame_principal.rowconfigure(0, weight=1)

        # === QUADRO DE BOLAS (ESQUERDA) ===
        quadro_frame = tk.LabelFrame(
            frame_principal,
            text="RELAÇÃO DE BOLAS CHAMADAS",
            font=("Consolas", 10, "bold"),
            bg="black",
            fg="red",
            labelanchor="n",
            bd=2
        )
        quadro_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        quadro_frame.configure(highlightbackground="red", highlightcolor="red")

        # Grid 1-75 (5 linhas x 15 colunas)
        for i, n in enumerate(range(1, self.total_bolas + 1)):
            row = i // 15
            col = i % 15
            lbl = tk.Label(
                quadro_frame,
                text=f"{n:02d}",
                font=("Consolas", 12),
                width=2,
                bg="black",
                fg="#444444"
            )
            lbl.grid(row=row, column=col, padx=2, pady=2)
            self.num_labels[n] = lbl

        # === LATERAL DIREITA ===
        side_frame = tk.Frame(frame_principal, bg="black")
        side_frame.grid(row=0, column=1, sticky="ns")

        # Última bola sorteada
        titulo_ultima = tk.Label(
            side_frame,
            text="ÚLTIMA BOLA",
            font=("Consolas", 10, "bold"),
            bg="black",
            fg="cyan"
        )
        titulo_ultima.pack(pady=(0, 5))

        self.lbl_ultima = tk.Label(
            side_frame,
            text="--",
            font=("Consolas", 40, "bold"),
            bg="black",
            fg="cyan",
            width=3
        )
        self.lbl_ultima.pack(pady=(0, 10))

        # Infos numéricas
        self.lbl_total = tk.Label(
            side_frame,
            font=("Consolas", 10),
            bg="black",
            fg="white"
        )
        self.lbl_total.pack(anchor="w")

        self.lbl_qtd_chamadas = tk.Label(
            side_frame,
            font=("Consolas", 10),
            bg="black",
            fg="white"
        )
        self.lbl_qtd_chamadas.pack(anchor="w")

        self.lbl_qtd_restantes = tk.Label(
            side_frame,
            font=("Consolas", 10),
            bg="black",
            fg="white"
        )
        self.lbl_qtd_restantes.pack(anchor="w", pady=(0, 8))

        # Lista de bolas na ordem
        lbl_ordem = tk.Label(
            side_frame,
            text="BOLAS NA ORDEM:",
            font=("Consolas", 10, "bold"),
            bg="black",
            fg="yellow"
        )
        lbl_ordem.pack(anchor="w")

        self.listbox_ordem = tk.Listbox(
            side_frame,
            font=("Consolas", 10),
            width=10,
            height=12,
            bg="black",
            fg="#00ff00",
            selectbackground="#333333",
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="#555555"
        )
        self.listbox_ordem.pack(fill="x", pady=(0, 10))

        # === CONTROLES (RODAPÉ) ===
        controles = tk.Frame(self.master, bg="black")
        controles.pack(fill="x", padx=10, pady=(0, 8))

        btn_sortear = tk.Button(
            controles,
            text="F2 - Sortear Próxima Bola",
            font=("Consolas", 10, "bold"),
            command=self.sortear_bola,
            bg="#004400",
            fg="white",
            activebackground="#007700",
            activeforeground="white",
            relief="raised"
        )
        btn_sortear.pack(side="left", padx=(0, 5))

        tk.Label(
            controles,
            text="Digitar bola:",
            font=("Consolas", 10),
            bg="black",
            fg="white"
        ).pack(side="left")

        self.entry_manual = tk.Entry(
            controles,
            font=("Consolas", 10),
            width=4,
            bg="black",
            fg="cyan",
            insertbackground="cyan"
        )
        self.entry_manual.pack(side="left", padx=(2, 2))

        btn_add_manual = tk.Button(
            controles,
            text="OK",
            font=("Consolas", 9, "bold"),
            command=self.adicionar_manual,
            bg="#333333",
            fg="white",
            activebackground="#555555",
            activeforeground="white"
        )
        btn_add_manual.pack(side="left", padx=(0, 10))

        btn_reset = tk.Button(
            controles,
            text="F10 - Novo Jogo",
            font=("Consolas", 10, "bold"),
            command=self.resetar,
            bg="#660000",
            fg="white",
            activebackground="#990000",
            activeforeground="white",
            relief="raised"
        )
        btn_reset.pack(side="right")

        # Atalhos
        self.master.bind("<F2>", lambda e: self.sortear_bola())
        self.master.bind("<F10>", lambda e: self.resetar())
        self.master.bind("<Return>", lambda e: self.adicionar_manual())

    # ===== LÓGICA =====

    def sortear_bola(self):
        if not self.bolas_restantes:
            messagebox.showinfo("Fim", "Todas as bolas já foram chamadas.")
            return
        bola = random.choice(self.bolas_restantes)
        self._registrar_bola(bola)

    def adicionar_manual(self):
        valor = self.entry_manual.get().strip()
        self.entry_manual.delete(0, tk.END)

        if not valor.isdigit():
            if valor != "":
                messagebox.showwarning("Inválido", "Digite um número entre 1 e 75.")
            return

        bola = int(valor)
        if bola < 1 or bola > self.total_bolas:
            messagebox.showwarning("Inválido", "Número fora do intervalo 1-75.")
            return

        if bola in self.bolas_chamadas:
            messagebox.showinfo("Aviso", f"A bola {bola:02d} já foi chamada.")
            return

        if bola not in self.bolas_restantes:
            messagebox.showwarning("Erro", "Essa bola não está disponível.")
            return

        self._registrar_bola(bola)

    def _registrar_bola(self, bola):
        self.bolas_chamadas.append(bola)
        self.bolas_restantes.remove(bola)
        self.lbl_ultima.config(text=f"{bola:02d}")
        self.listbox_ordem.insert(tk.END, f"{bola:02d}")
        self._atualizar_tudo()

    def resetar(self):
        if messagebox.askyesno("Novo Jogo", "Deseja realmente iniciar um novo jogo?"):
            self.bolas_chamadas.clear()
            self.bolas_restantes = list(range(1, self.total_bolas + 1))
            self.lbl_ultima.config(text="--")
            self.listbox_ordem.delete(0, tk.END)
            self._atualizar_tudo()

    def _atualizar_tudo(self):
        chamadas_set = set(self.bolas_chamadas)

        # Atualiza painel
        for n in range(1, self.total_bolas + 1):
            lbl = self.num_labels[n]
            if n in chamadas_set:
                lbl.config(fg="#00ff00", font=("Consolas", 12, "bold"))
            else:
                lbl.config(fg="#444444", font=("Consolas", 12, "normal"))

        # Infos
        self.lbl_total.config(text=f"TOTAL DE BOLAS: {self.total_bolas}")
        self.lbl_qtd_chamadas.config(text=f"BOLAS CHAMADAS: {len(self.bolas_chamadas)}")
        self.lbl_qtd_restantes.config(text=f"BOLAS A CHAMAR: {len(self.bolas_restantes)}")

def main():
    root = tk.Tk()
    app = BingoApp(root)
    root.geometry("1024x600")  # ajusta conforme sua tela
    root.mainloop()

if __name__ == "__main__":
    main()
