#Atividade avaliativa de Desenvolvimento WEB III
#Prof° Dra. Mariela Tamada 
#Acadêmico: Thiago Silva Marques 
# 4° Período de TSI 

# Importação da classe Flask da biblioteca flask
from flask import Flask, render_template

# Instancia o aplicativo Flask e o nomeia como 'app_devWebIII'
app_devWebIII = Flask (__name__) 
#Criando uma nova rota raiz como homepage da página, recebendo uma página html estática#
#Substintuindo também a routa de saudação.#
@app_devWebIII.route('/index/<id>')
def pagina_inicial(id):
    return render_template('index.html', nome=id)

#Nesta rota substintuindo a rota2, criou-se uma página html para receber as informações transmitidas pelas rotas#
@app_devWebIII.route('/contato/<id>')
def contato(id):
    # Dicionário contendo as informações de contato
    contato_info = {
        "disciplina": "Desenvolvimento Web III",
        "professor": "Profª. Dra. Mariela Tamada",
        "instituicao": "IFRO - Campus PVZN",
        "email": "0000@gmail.com", 
        "telefone": "(69)99999-9999"
    }
    return render_template('contato.html', nome=id, dados=contato_info)

# Verifica se o arquivo está sendo executado diretamente (não importado por outro módulo)
if __name__ == "__main__" : # 
    # Executa o servidor Flask na porta 8080
    app_devWebIII.run(port = 8080, debug=True)  
    # debug=True ativa o modo de depuração, reiniciando o servidor automaticamente ao salvar mudanças

