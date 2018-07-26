# Herói Social

Versão: 1.0

# ----- Pré-Requisitos: ------
Sistema operacional: Windows

Linguagem: Python 3.6

Para criar o banco: MySQL Workbench 8.0.11

Para rodar a aplicação: XAMPP v3.2.2 ou Wamp Server

# ----- Guia de instalação para rodar o projeto: -----
1. Para baixar o código da aplicação, basta ir no github, no link: “https://github.com/Adailson-Jose/heroi-social.git”, clicar em “Clone or download”, e copiar o link. Você pode importar o projeto pelo próprio Pycharm ou instalando o GIT em sua máquina, para utilizar o Git Bash. Basta criar uma pasta onde ficará o código do projeto, clica nela com o botão direito em “Git bash here”, e ao abrir o terminal do git, colocar:  “git clone https://github.com/Adailson-Jose/heroi-social.git” e esperar fazer o download do projeto.

2. Para criar o banco já povoado, basta abrir o arquivo “Mining_Traffic_Recife.sql” dentro da pasta principal do projeto (“heroi-social”) pelo MySQL Workbench e rodar o script, porém, essa forma pode demorar muito. Uma outra forma mais rápida é abrir o arquivo “traffic_mining_recifel.sql” com um editor de texto de sua preferência (indicamos o Sublime Text), copiar o conteúdo do script, e iniciar o Workbench, criando uma query, onde você vai colar o conteúdo dentro dela, e botar para rodar. Lembre de esperar até todo o processo ser concluído. Pronto o banco será criado, aí é só dar o phyton run.py runserver para rodar a aplicação. Esse processo deve ser feito uma única vez.

3. Indicamos que para rodar essa aplicação, é melhor utilizar um ambiente virtual disponível na própria pasta principal do projeto, cujo o nome é “venv”. Porém, você pode instalar também as bibliotecas utilizadas diretamente na sua máquina.

4. Observação:
As bibliotecas utilizadas no projeto estão no arquivo “requirements.txt” dentro da pasta principal do projeto (“heroi-social”). Caso queira instalar manualmente em sua máquina, basta localizar a pasta onde o Python foi instalado em seu computador, e dentro da pasta “SCRIPT”, copie e cole dentro dela o arquivo “requirements.txt”. Depois você copia o endereço da pasta, abre o CMD, digita “cd” e cola o endereço para entrar nessa pasta. Depois é só digitar “pip install -r requirements.txt” e esperar a instalação de todas as bibliotecas que estão contidas dentro desse arquivo.

5. Para rodar a aplicação, vamos primeiro botar o banco para rodar, utilizando o XAMPP: ao abrir o XAMPP, dar “start” no Apache e MySQL. Se quiser olhar o banco, é só clicar em “Admin” na linha do MySQL.

6. Iniciando o ambiente virtual: copie o endereço da pasta “venv”. Abra o CMD e digite: “cd ” e cole o endereço copiado anteriormente. Agora você está dentro da pasta “venv”. Vamos agora iniciar o ambiente. Digite: “venv\Scripts\activate”. Você verá que vai aparecer no início da linha “(venv)”. Isso indica que o ambiente está pronto para uso.

7. Agora vamos abrir a pasta do projeto. Vá no diretório onde você clonou a pasta do projeto, copie o endereço, abra o CMD e digite: “cd “ e cole o endereço. Depois digite: “python run.py runserver” e espere rodar. Ao rodar, será mostrado o link do ser servidor local (“http://127.0.0.1:5000/”). Copie isso e jogue em um navegador web para abrir a aplicação.


# ----- Autoria: -----
Alunos da Universidade Federal Rural de Pernambuco: 

Adailson José

Caroline Gomes

Eliana França

Gabriela Peixoto

Jadeilson Rocha

Wenderson Leonardo
