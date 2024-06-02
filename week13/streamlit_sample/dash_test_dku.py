#!/usr/bin/python
# -*- coding: <encoding name> -*-
# code source = http://bigdata.dongguk.ac.kr/lectures/datascience/_book/a4.-dash%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-python-dashboard.html#%EB%8C%80%EC%8B%9Cdash%EB%9E%80
# 가상환경에서 "pip install dash"


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = px.data.iris() # iris data 불러오기
# plotly를 이용한 산점도
fig = px.scatter(df, x="sepal_length", y="sepal_width", 
                  color="species")

app = Dash(__name__)
# app layout: html과 dcc 모듈을 이용
app.layout = html.Div(children=[
    # Dash HTML Components module로 HTML 작성 
    html.H1(children='첫번째 Dash 연습'),
    html.Div(children='''
        대시를 이용하여 웹어플리케이션 작성 연습...
    '''),
    # dash.core.component(dcc)의 그래프컴포넌트로 plotly 그래프 렌더링
    dcc.Graph(
        id='graph1',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
    #app.run_server(debug=False, host='0.0.0.0', port=8888)