import plotly.graph_objects as go

# Dados do grafico
dado_x = [1, 2, 3, 4, 5]
dado_y = [10, 11, 12, 13, 14]

# Criar um  graficod e linha
figura = go.Figure(
    data=go.Scatter(
        x = dado_x,
        y = dado_y,
        mode = 'lines+markers',
        name = 'Linha 01'
    )
)

# Adicionar titulo e rotulo aos eixos
figura.update_layout(
    title = 'Grafico de linha interativo',
    xaxis_title = 'Eixo X',
    yaxis_title = 'Eixo Y'    
)

# Exibindo o grafico
figura.show()