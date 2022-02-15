# sistema_gui_pymysql
Controle de produtos com Python + MySQL + PyQt5 + FPDF + Pyinstaller

Sistema simples de gerenciamento de pedidos (fastfood) que permite controlar os lucros, identificar produtos mais vendidos, bem como clientes mais frequentes. Neste exemplo, é utilizado a ferrameta **PyQt5** para criação da interface gráfica, que vai permitir aos usuários (administradores) registrar pedidos em um banco de dados **MySQL** que se comunica pela linguagem **Python**, podendo gerar relatórios por período (através da biblioteca **FPDF**) e planilhas de excel (.CSV) por meio da biblioteca **Pandas**. Ao final, para gerar um arquivo executável do sistema e utilizá-lo como app em outras máquinas, pode ser usada a ferramenta Pyinstaller para geração do arquivo.

<img src="https://github.com/miguelneto0/sistema_gui_pymysql/blob/main/images/telas.gif" width=600>

Basicamente, o sistema é composto por 3 telas: uma tela principal de login, onde os usuarios administradores que possuem cadastros podem realizar pedidos e acessá-los, uma tela de seleção de itens que irão compor o pedido, e uma tela que lista todos os pedidos e permite pesquisar e calcular o lucro dos registros do banco de dados. 

## Configuração do Banco de Dados

Primeiramente é configurado o banco de dados utilizado. Nesse caso, uma base de dados chamada de _cadastro_lanches_ foi criada utilizando o **MySQL**, compondo 2 tabelas: **admins** e **pedidos**. Para tal, pode ser executado o comando:
- <code>CREATE DATABASE cadastro_lanches;</code>
- <code>CREATE TABLE pedidos (id INT NOT NULL AUTO_INCREMENT, codigo INT NOT NULL, nome VARCHAR(45), descricao VARCHAR(80), Total DOUBLE, PRIMARY KEY (id));</code>

Em seguida, para manipular o timestamp de cadastros a tabela foi alterada para registrar os dados de data e hora automaticamente, com os valores atuais:

<code>ALTER TABLE pedidos ADD time_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;</code>

Para acessar o banco: procurar por _"Arquivos de Programas"/MySQL/MySQL Server VERSAO/bin_ e digitar <code>mysql -u root -p</code>

## Criando telas com PyQt e QtDesigner

Em seguida, as telas são criadas usando a ferramenta QtDesigner, instalada juntamente com a biblioteca PyQt5 no Python, através do comando:
- <code>pip install PyQt5</code>

Para acessar a ferramenta, o usuario deve buscar o arquivo executável na pasta <pre>/PYTHON_LOCAL/PYTHON_VERSAO/Lib/site-packages/qt5_applications/Qt/bin</pre> ou <pre>/PYTHON_LOCAL/PYTHON_VERSAO/Lib/site-packages/PyQt/Tools/bin</pre>

onde PYTHON_LOCAL se refere ao local de instalação do Python e PYTHON_VERSAO a versão em que foi instalado o PyQt;

Ao executar a ferramenta **qtdesigner.exe** ou **designer.exe**, o proximo passo é criar a tela com os Widgets da janela pelo método de "clicar e arrastar" os itens e configurá-los com ajuda dos menus laterais. Atenção para cada nome do item criado, pois deve ser usado no codigo Python para manipulação, através da biblioteca PyQt, importando as classes PyQt.QtWidgets, PyQt.QtTools, PyQtQApplication, entre outras de acordo com a necessidade. As telas criadas com a interface QtDesigner são salvas com a extensão **.ui** conforme os arquivos _telas_lista_, _telas_login_, _telas_pyqt_.

Após criar as telas e vincular os elementos ao codigo, são definidas as regras que vão ativar os botões e exibir as informacoes para o administrador manusear a aplicação.


## Configuração dos botões e telas no código

Para a primeira tela, o login é apresentado, fornecendo também a opção de cadastrar novo usuario, conforme a Figura.

<img src="https://github.com/miguelneto0/sistema_gui_pymysql/blob/main/images/telalogin.png" width=700>

Conforme a Figura, a tela que lista todos os pedidos permite efetuar buscas e calcular o lucro para cada pesquisa (através do botao calcula lucro). Da mesma forma, para gerar um relatorio em PDF com os pedidos por período o botao se comporta de acordo com a definição da Figura. Similarmente, o botao geraCSV define como a planilha CSV é gerada pelo uso da biblioteca Pandas (Figura).

<img src="https://github.com/miguelneto0/sistema_gui_pymysql/blob/main/images/telalista.png" width=500>

<img src="https://github.com/miguelneto0/sistema_gui_pymysql/blob/main/images/geracsv.png" height=250><img src="https://github.com/miguelneto0/sistema_gui_pymysql/blob/main/images/gerapdf.png" height=250>

Especificamente no codigo para geração do CSV, é importante observar que o comando de busca SQL deve ser executado com o objeto **cursor** e método **commit()**.

Para calcular o lucro é usado o seguinte codigo da Figura. Nesse exemplo, o valor de j é fixado em 4, para identificar que o valor que se quer buscar e calcular é correspondente à quinta coluna, logo 4, já que a contagem inicia em 0. Assim, o valor obtido em String (str) é convertido em Float e somado para atualizar o texto da labelLucro.

<img src="https://github.com/miguelneto0/sistema_gui_pymysql/blob/main/images/calculalucro.png" width=400>

A animação a seguir detalha os botoes em acoes, bem como a geracao do Relatorio em PDF e a planilha em CSV.

<img src="https://github.com/miguelneto0/sistema_gui_pymysql/blob/main/images/telas2.gif" width=600>
