#Atividade avaliativa de Desenvolvimento WEB III
#Prof° Dra. Mariela Tamada 
#Acadêmico: Thiago Silva Marques 
# 4° Período de TSI 

# Importação da classe Flask da biblioteca flask
from flask import Flask 

# Instancia o aplicativo Flask e o nomeia como 'app_devWebIII'
app_devWebIII = Flask (__name__) 

# Criação da primeira rota (raiz do site)
@app_devWebIII.route('/')
def raiz():
    return 'Olá, bem vindos(as)!'

# Execução da aplicação Flask
app_devWebIII.run()
#Na aula 01 - aprendemos a criar rotas e fazer sua comunicação com o navegador#

