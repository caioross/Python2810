import sqlite3

# Conectar ao banco de dados (Ou criar um novo, se não existir)
def conectar_banco() :
    conexao = sqlite3.connect('exemplo.db')
    return conexao

# Criar a tabela
def criar_tabela() :
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER       
        )
    ''')
    conexao.commit()
    conexao.close()

# Inserir dados
def inserir_usuario(nome, idade) :
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
       INSERT INTO usuarios (nome, idade)
       VALUES (?, ?)            
    ''', (nome, idade))
    conexao.commit()
    conexao.close()

# Excluir dados
def excluir_usuario(id) :
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        DELETE FROM usuarios
        WHERE id = ?
    ''', (id,))
    conexao.commit()
    conexao.close()
    
# Atualizar dados
def atualizar_usuario(id, novo_nome, nova_idade) :
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE usuarios
        SET nome = ?, idade = ?
        WHERE id = ?
    ''', (novo_nome, nova_idade, id))
    conexao.commit()
    conexao.close()
    
# Listar Usuarios
def listar_usuarios():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    for usuario in usuarios :
        print(usuario)
    conexao.close()

# Exemplos de uso das Funções

# Criar a tabela
criar_tabela()

#Inserir alguns usuarios
inserir_usuario('Caio',39)
inserir_usuario('Fabiano',40)
inserir_usuario('Tito',60)

# Listar os usuarios
print('Usuarios antes de atualizar:')
listar_usuarios()

# Atualizar a idade do Caio
atualizar_usuario(1, 'Caio', 41)

#Listar usuarios apos a atualização
print('Usuarios após a atualização')
listar_usuarios()

#Excluir o usuario caio de id 1
excluir_usuario(1)

#Listar usuarios após a exclusão
print('Usuarios após a Exclusão')
listar_usuarios()