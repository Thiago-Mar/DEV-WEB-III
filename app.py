# Atividade avaliativa de Desenvolvimento WEB III
# Prof° Dra. Mariela Tamada 
# Acadêmico: Thiago Silva Marques 
# 4° Período de TSI 

# Importação da classe Flask da biblioteca flask
# CORREÇÃO: Adicionado redirect e url_for para o redirecionamento
from flask import Flask, render_template, request, redirect, url_for 

# Instancia o aplicativo Flask e o nomeia como 'app_devWebIII'
app_devWebIII = Flask (__name__) 

# Criando uma nova rota raiz como homepage da página, recebendo uma página html estática
@app_devWebIII.route('/index/<id>')
def pagina_inicial(id):
    # Passando o nome=id (o ID aqui pode ser o nome do usuário)
    return render_template('index.html', nome=id) # Usa index.html

# Fazendo a alteração para que a url seja dinâmica e as informações sejam passadas pela URL para
@app_devWebIII.route('/contato/<nome_user>/<email_usuario>/<telefone_usuario>') 
def contato(nome_user, email_usuario, telefone_usuario):
    # Dicionário contendo as informações de contato
    contato_info ={"email": email_usuario, "telefone": telefone_usuario}
    return render_template('contato.html', nome=nome_user, dados=contato_info) # Usa contato.html

# Parâmetros para URL com informação (dinâmico)
@app_devWebIII.route("/usuario/<nome_usuario>/<nome_profissao>/<nome_disciplina>") 
def usuario (nome_usuario, nome_profissao, nome_disciplina): 
    dados_usu = {"profissao": nome_profissao, "disciplina":"Desenvolvimento Web III"}
    return render_template ("usuario.html", nome=nome_usuario, dados = dados_usu) 

# usuarios SEM passagem de argumentos, pois iremos usar DEFAULTS
@app_devWebIII.route("/usuario", defaults={"nome_usuario":"usuário?","nome_profissao":""}) 
def usuarios (nome_usuario, nome_profissao):
    dados_usu = {"profissao": nome_profissao, "disciplina":"Desenvolvimento Web III"}
    return render_template ("usuario.html", nome=nome_usuario, dados = dados_usu)

# Criação da rota de login#
@app_devWebIII.route('/login')
def login():
    return render_template("login.html") # Usa login.html

# Implementando a função de autenticar#
@app_devWebIII.route("/autenticar", methods=['POST'] ) 
def autenticar():
    usuario = request.form.get('nome_usuario')
    senha = request.form.get('senha')
    
    # CORREÇÃO: Lógica de autenticação implementada com redirecionamento correto
    if usuario == "ADM" and senha == "tsi": 
        # Redireciona para a rota 'pagina_inicial' (que chama index.html), passando o ID
        return redirect(url_for('pagina_inicial', id=usuario))
    else:
        # Se falhar, volta para a rota 'login' (que chama login.html)
        return redirect(url_for('login', error="Credenciais inválidas!")) # Usando redirect para exibir erro de forma limpa
    

# Verifica se o arquivo está sendo executado diretamente (não importado por outro módulo)
if __name__ == "__main__" : 
    # Executa o servidor Flask na porta 8080
    app_devWebIII.run(port = 8080, debug=True)