import sqlite3
import tkinter as tk
from tkinter import ttk # widget mais moderno do tkinter
from tkinter import messagebox # Para exibir alertas de erros

# ============= Configuração do banco de dados =======================
def conectar_banco():
    conexao = sqlite3.connect(r"C:\Users\Matrix\Desktop\Python_EAD\lista_mercado.db")
    return conexao

def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS itens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER,
            observacao TEXT
        )
    """)
    conexao.commit()
    conexao.close()
    
# ============= Funções Principais =====================================
def adicionar_item():
    # Capturar o texto digitado nos campos de entrada
    nome = entrada_nome.get().strip()
    quantidade = entrada_quantidade.get().strip()
    observacao = entrada_observacao.get().strip()
    
    # Validação simples: não permite o nome vazio
    if not nome:
        messagebox.showwarning("Atenção", "O campo de nome não pode fizar vazio.")
        return

    # Se a quantidade for vazio, define 1 comop padrao
    if quantidade == "":
        quantidade = 1
    else:
        try:
            quantidade = int(quantidade)
        except ValueError:
            messagebox.showwarning("Atenção","Digite um numero valido na quantidade.")
            return
        
    # Insere os dados no banco de dados
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO itens (nome, quantidade, observacao) VALUES (?, ?, ?)", 
        (nome, quantidade, observacao)
    )
    conexao.commit()
    conexao.close()
    
    # Limpa os campos apos salvar
    entrada_nome.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    entrada_observacao.delete(0, tk.END)
    
    # Atualiza a lista exibida na tela
    carregar_itens()


def carregar_itens():
    # Limpar a tabela (Treeview) antes de recarregar
    for item in tabela_itens.get_children():
        tabela_itens.delete(item)
        
    # Buscar todos os registros do banco
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, quantidade, observacao FROM itens")
    registros = cursor.fetchall()
    conexao.close()
    
    # Insere cada registro na tabela visual
    for linha in registros:
        tabela_itens.insert("", tk.END, values=linha)
        

def excluir_item_selecionado():
    # Pega o item selecionado na tabela
    item_selecionado = tabela_itens.selection()
    if not item_selecionado:
        messagebox.showinfo("Info","Selecione um item para excluir.")
        return    

    # Pega os valores da linha (descobre qual id é o selecionado)
    valores = tabela_itens.item(item_selecionado, "values")
    item_id = valores[0]    

    # Confirmar se vai excluir
    confirmar = messagebox.askyesno("Confirmar","Tem certeza que deseja excluir esse item?")
    if not confirmar:
        return

    # Excluir do banco
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM itens WHERE id = ?",(item_id,))
    conexao.commit()
    conexao.close()
    
    # Atualiza a tabela na tela
    carregar_itens()
    
def limpar_busca():
    entrada_busca.delete(0, tk.END)
    carregar_itens()
    
def buscar_itens():
    termo = entrada_busca.get().strip()
    
    # Limpar a tabela antes de mostrar o resultado
    for item in tabela_itens.get_children():
        tabela_itens.delete(item)
        
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    if termo == "":
        # se nao digitou nada, mostra tudo novamente
        cursor.execute("SELECT id, nome, quantidade, observacao FROM itens")
    else:
        # Buscar item cujo nome contenha o termo digitado
        cursor.execute(
            "SELECT id, nome, quantidade, observacao FROM itens WHERE nome LIKE ?",
            (f"%{termo}%",)
        )
    registros = cursor.fetchall()
    conexao.close()
    
    # Preenche a tabela com resultados da busca
    for linha in registros:
        tabela_itens.insert("", tk.END, values=linha)
    
# ============= Interface Gráfica =====================================

criar_tabela() # Garante que a tabela sempre exista antes de abrir a interface
janela = tk.Tk()
janela.title('Lista de Compras - Hemobras')
janela.geometry('700x400')

# Frame para o formulario de cadastro
frame_formulario = tk.Frame(janela)
frame_formulario.pack(pady=10)

# Rotulos e campos de entrada
tk.Label(frame_formulario, text='Nome do item: ').grid(row=0, column=0, sticky='w')
entrada_nome = tk.Entry(frame_formulario, width=30)
entrada_nome.grid(row=0, column=1, sticky='w', padx=5)

tk.Label(frame_formulario, text='Quantidade: ').grid(row=1, column=0, sticky='w')
entrada_quantidade = tk.Entry(frame_formulario, width=10)
entrada_quantidade.grid(row=1, column=1, sticky='w', padx=5)

tk.Label(frame_formulario, text='Observação: ').grid(row=2, column=0, sticky='w')
entrada_observacao = tk.Entry(frame_formulario, width=40)
entrada_observacao.grid(row=2, column=1, padx=5, pady=5)

# Botão para adicionar item
botao_adicionar = tk.Button(
    frame_formulario,
    text = 'Adicionar Item',
    command = adicionar_item
    )
botao_adicionar.grid(row=3, column=0, columnspan=2, pady=5)

# Area de Busca
frame_busca = tk.Frame(janela)
frame_busca.pack(pady=5)

tk.Label(frame_busca, text='Buscar item: ').grid(row=0, column=0, padx=5)
entrada_busca = tk.Entry(frame_busca, width=30)
entrada_busca.grid(row=0, column=1, padx=5)
botao_buscar = tk.Button(frame_busca, text='Buscar', command=buscar_itens)
botao_buscar.grid(row=0, column=2, padx=5)
botao_limpar = tk.Button(frame_busca, text='Limpar', command=limpar_busca)
botao_limpar.grid(row=0, column=4, padx=5)

# Tabela (Treeview) para exibir os dados
colunas = ("id", "nome", "quantidade", "observacao")

tabela_itens = ttk.Treeview(janela, columns=colunas, show='headings')
tabela_itens.heading('id', text='ID')
tabela_itens.heading('nome', text='Nome')
tabela_itens.heading('quantidade', text='Quantidade')
tabela_itens.heading('observacao', text='Observação')

tabela_itens.column('id', width=40)
tabela_itens.column('nome', width=200)
tabela_itens.column('quantidade', width=90)
tabela_itens.column('observacao', width=250)

tabela_itens.pack(fill="both", expand=True, padx=10, pady=10)


# Botões de ações abaixo da tabela
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady = 5)

botao_recarregar = tk.Button(
    frame_botoes,
    text = 'Recarregar Itens',
    command = carregar_itens
    )
botao_recarregar.grid(row = 0, column = 0, padx = 5)

botao_excluir = tk.Button(
    frame_botoes,
    text = 'Excluir selecionado',
    command = excluir_item_selecionado    
)
botao_excluir.grid(row = 0, column = 1, padx = 5)

carregar_itens()

# Inicia o Loop da interface grafica do tkinter
janela.mainloop()