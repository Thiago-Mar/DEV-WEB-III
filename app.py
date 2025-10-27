#Atividade avaliativa de Desenvolvimento WEB III
#Prof° Dra. Mariela Tamada 
#Acadêmico: Thiago Silva Marques 
# 4° Período de TSI 

# Importação da classe Flask da biblioteca flask
from flask import Flask 

# Instancia o aplicativo Flask e o nomeia como 'app_devWebIII'
app_devWebIII = Flask (__name__) 
@app_devWebIII.route("/")
@app_devWebIII.route("/rota1")
def raiz():
    return 'Olá, bem vindos(as)!'

#Essa rota tem a implementação de TAG HTML#
@app_devWebIII.route('/rota2')
def rota2():
    resposta = "<H3> Página da rota 2, usando conceitos de html <H3>"
    return resposta

# Criação de uma rota dinâmica de saudação
@app_devWebIII.route('/saudacao/<nome>')
# '<nome>' indica que essa parte da URL será dinâmica e passada como parâmetro para a função
# Função recebe o parâmetro 'nome' da URL e retorna uma saudação personalizada
def saudacoes(nome):
     # Função recebe o parâmetro 'nome' da URL e retorna uma saudação personalizada
    return f'Olá, {nome} como vai? '


# Verifica se o arquivo está sendo executado diretamente (não importado por outro módulo)
if __name__ == "__main__" : # 
    # Executa o servidor Flask na porta 8080
    app_devWebIII.run(port = 8080, debug=True)  
    # debug=True ativa o modo de depuração, reiniciando o servidor automaticamente ao salvar mudanças

