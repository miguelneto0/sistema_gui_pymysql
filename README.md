# sistema_gui_pymysql
Controle de produtos com Python + MySQL + PyQt5 + Reportlab + Pyinstaller

Sistema para uma hamburgueria com interface criada no PyQt e QtDesigner, banco de dados MySQL, geracao de PDF com FPDF. Inserir autenticacao com banco SQLITE e gerar executaveis em Python com PYinstaller.

Manipular o timestamp de cadastros:

ALTER TABLE pedidos ADD time_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
