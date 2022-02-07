import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit

import mysql.connector

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        # Definicoes da area da janela
        self.topo     = 100
        self.esquerda = 100
        self.largura  = 800
        self.altura   = 600
        self.titulo    = "Janela de Sistema"

        # configuracoes do botao "Enviar"

        botao = QPushButton('Enviar', self)
        botao.move(int(np.ceil(self.largura*0.8)),int(np.ceil(self.altura*0.8)))
        botao.resize(120,60)
        botao.setStyleSheet('QPushButton {background-color: #ee8800;font:bold;font-size:20pt}')
        botao.clicked.connect(self.botaoClick)

        # configurando Labels

        labelTitulo = QLabel(self)
        labelTitulo.setText('Controle de Vendas')
        labelTitulo.setStyleSheet('QLabel {font-size:14pt}')
        labelTitulo.resize(300,50)
        labelTitulo.move(int(self.largura*0.35),int(self.altura*0.02))
        # Caso precise utilizar o label para ser alterado, usar self.label

        # configurando caixas de texto
        self.caixaTexto = QLineEdit(self)
        self.caixaTexto.move(300,300)
        self.caixaTexto.resize(200,60)

        # renderiza a janela
        self.carregaJanela()

    def botaoClick(self):
        teto = int(np.ceil(self.largura*0.8))
        print(f'Botao "Enviar" clicado. Teto = {teto}')

    def carregaJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())