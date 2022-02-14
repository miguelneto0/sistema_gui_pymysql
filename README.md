# sistema_gui_pymysql
Controle de produtos com Python + MySQL + PyQt5 + FPDF + Pyinstaller

Sistema para uma hamburgueria com interface criada no PyQt e QtDesigner, banco de dados MySQL, geracao de PDF com FPDF. Inserir autenticacao com banco SQLITE e gerar executaveis em Python com PYinstaller.

Basicamente, o sistema é composto por 3 telas. Uma tela principal de login, onde os usuarios administradores que possuem cadastros podem ter acesso aos pedidos, uma tela de selecao de itens que irão compor o pedido, e uma tela que lista todos os pedidos e permite pesquisas bem como calculo do lucro dos pedidos buscados. 

Primeiramente é configurado o banco de dados utilizado. Nesse caso, uma base de dados chamada de _cadastro_lanches_ foi criada utilizando o **MySQL**, compondo 2 tabelas: **admins** e **pedidos**.

Em seguida, as telas são criadas usando a ferramenta QtDesigner, instalada juntamente com a biblioteca PyQt5 no Python, através do comando:
- <code>pip install PyQt5</code>

Para acessar a ferramenta, o usuario deve buscar o arquivo executável na pasta <pre>/PYTHON_LOCAL/PYTHON_VERSAO/Lib/site-packages/qt5_applications/Qt/bin</pre> ou <pre>/PYTHON_LOCAL/PYTHON_VERSAO/Lib/site-packages/PyQt/Tools/bin</pre>

Ao executar a ferramenta **qtdesigner.exe** ou **designer.exe**, o proximo é criar a tela e os Widgets da janela clicando e arrastando os itens e configurando-os com ajuda dos menus laterais. Atenção para cada nome do item criado, pois sera usado no codigo Pytho para manipulação, através da biblioteca PyQt, importando as classes PyQt.QtWidgets, PyQt.QtTools, PyQtQApplication, entre outras de acordo com a necessidade. As telas criadas com a interface QtDesigner são salvas com a extensão **.ui** conforme os arquivos telas_lista, telas_login, telas_pyqt.

Após criar as telas e vincular os elementos ao codigo, são definidas as regras que vão ativar os botões e exibir as informacoes para o administrador manusear a aplicação.

## Configuração do Banco de Dados

Manipular o timestamp de cadastros:

<code>ALTER TABLE pedidos ADD time_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;</code>

## Configuração dos botões e telas no código


