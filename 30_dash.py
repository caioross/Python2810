import dash
from dash import dcc, html
import plotly.graph_objs as go

# Inicializando o aplicativo dash
app = dash.Dash()

# Definindo o layout do dashboard (grafico)
app.layout = html.Div([
    html.H1("Grafico interativo com Dash e Plotly"),
    dcc.Graph(
        id = 'grafico-1',
        figure = {
            'data': [
                go.Scatter(
                    x = [1, 2, 3, 4, 5],
                    y = [11, 12, 13, 14, 15],
                    mode = 'lines+markers',
                    name = 'Linha 1'
                )
            ],
            'layout':  
                go.Layout(
                    title = 'Grafico de Linha Interativo',
                    xaxis = {'title':'Eixo X'},
                    yaxis = {'title':'Eixo Y'}    
                )  
        }
    )
])

# Rodando o servidor
if __name__ == '__main__' :
    app.run(debug=True) 