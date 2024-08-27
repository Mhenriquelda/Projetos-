from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
d1 = pd.read_excel("Book1.xlsx")
d2 = pd.read_excel("Book1.xlsx")

fig1 = px.bar(d1, x="Mês", y="Total", color="Mês", barmode="group")
fig2 = px.bar(d2, x="Media", y="Atendimentos", color="Media", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Como está a tendência de público atendido ao longo do tempo?'),

    html.Div(children='''
        De janeiro até março, teve uma queda significativa no numero de clientes atendidos no hospital.
    '''),
    html.H1(children='A clínica está gastando mais dinheiro com remuneração do que o padrão previsto?'),

    html.Div(children='''
        Sim. O hospital está tendo um alto custo extra. Podemos observar nos dados, que apesar de estar 
        decaindo o numero de atendimentos, o limite diário está sendo ultrapassado quase todos os dias, causando enorme prejuízo. 
    '''),
    html.H1(children='Recomendação com base no Dashboard'),

    html.Div(children='''
        A clinica teria que rever o contrato dos 3 médicos, aumentar o número de consultas diárias e assim equilibrar o 
        prejuízo com a baixa procura mensal.	
    '''),



    dcc.Graph(
        id='example-graph1',
        figure=fig1
    ),

    dcc.Graph(
        id='example-graph2',
        figure=fig2
    )
])

if __name__ == '__main__':
    app.run(debug=True)