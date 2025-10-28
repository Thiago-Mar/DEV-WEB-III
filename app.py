# Atividade avaliativa de Desenvolvimento WEB III
# Prof° Dra. Mariela Tamada 
# Acadêmico: Thiago Silva Marques 
# 4° Período de TSI 

# Importação da classe Flask da biblioteca flask
from flask import Flask, render_template, request, redirect, url_for, flash, session

# Instancia o aplicativo Flask e o nomeia como 'app_devWebIII'
app_devWebIII = Flask (__name__) 

app_devWebIII.secret_key = '123456' 

#Dicionário de usuários cadastrados
tabelaUsuarios = {
    "ADM": "tsi",
    "Thiago": "tristeza"
}

#Função para verificar o login 
def verificar_login(login, senha):
    if login in tabelaUsuarios and tabelaUsuarios[login] == senha:
        return True
    return False

# Rota Raiz (NOVA): Redireciona para o login
@app_devWebIII.route('/')
def index_root():
    return redirect(url_for('login'))

# Utilizando a rota index - Homepage
@app_devWebIII.route('/index/<id>')
def pagina_inicial(id):
    return render_template('index.html', nome=id)

# Fazendo a alteração para que a url seja dinâmica e as informações sejam passadas pela URL 
@app_devWebIII.route('/contato/<nome_user>/<email_usuario>/<telefone_usuario>') 
def contato(nome_user, email_usuario, telefone_usuario):
    contato_info ={"email": email_usuario, "telefone": telefone_usuario}
    return render_template('contato.html', nome=nome_user, dados=contato_info) 

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
    # Captura o parâmetro de erro (vindo do redirect)
    error = request.args.get('error') 
    return render_template("login.html", error=error) 

# Implementando a função de autenticar (Modelo da Professora)
@app_devWebIII.route("/autenticar", methods=['GET','POST'])
def autenticar():
    usuario = request.form.get('nome_usuario')
    senha = request.form.get('senha')
    
    if verificar_login(usuario, senha):
        msg = "Login e senha corretos. Acesso permitido."
        return f"{msg} para {usuario} "
    else:
        # Usa flash e redirect (Modelo da Professora)
        flash("Dados inválidos!")
        flash("Login ou senha incorretos. Acesso negado.")
        return redirect ('/login')

#Logout
@app_devWebIII.route('/logout')
def logout():
    # Remove o usuário da sessão, se ele existir
    session.pop('usuario_logado', None)
    flash("Sessão encerrada com sucesso.", "info")
    return redirect(url_for('login'))


# Verifica se o arquivo está sendo executado diretamente (não importado por outro módulo)
if __name__ == "__main__" : 
    # Executa o servidor Flask na porta 8080
    app_devWebIII.run(port = 8080, debug=True)