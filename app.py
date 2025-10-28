# Atividade avaliativa de Desenvolvimento WEB III
# Prof° Dra. Mariela Tamada 
# Acadêmico: Thiago Silva Marques 
# 4° Período de TSI 

# Importação da classe Flask da biblioteca flask
from flask import Flask, render_template

# Instancia o aplicativo Flask e o nomeia como 'app_devWebIII'
app_devWebIII = Flask (__name__) 

# Criando uma nova rota raiz como homepage da página, recebendo uma página html estática
@app_devWebIII.route('/index/<id>')
def pagina_inicial(id):
    # Passando o nome=id (o ID aqui pode ser o nome do usuário)
    return render_template('index.html', nome=id)

#Fazendo a alteração para que a url seja dinâmica e as informações sejam passadas pela URL para
@app_devWebIII.route('/contato/<nome_user>/<email_usuario>/<telefone_usuario>') 
def contato(nome_user, email_usuario, telefone_usuario):
    # Dicionário contendo as informações de contato
    contato_info ={"email": email_usuario, "telefone": telefone_usuario}
    return render_template('contato.html', nome=nome_user, dados=contato_info) 

@app_devWebIII.route("/usuario/<nome_usuario>/<nome_profissao>/<nome_disciplina>") 
def usuario (nome_usuario, nome_profissao, nome_disciplina): 
    dados_usu = {"profissao": nome_profissao, "disciplina": nome_disciplina}
    return render_template("usuario.html", nome=nome_usuario, dados = dados_usu) 

#Criação da rota de login#
@app_devWebIII.route('/login')
def login():
    return render_template("login.html")
    

# Verifica se o arquivo está sendo executado diretamente (não importado por outro módulo)
if __name__ == "__main__" : 
    # Executa o servidor Flask na porta 8080
    app_devWebIII.run(port = 8080, debug=True)