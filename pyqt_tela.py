from PyQt5 import uic, QtWidgets, QtGui
from cv2 import QT_CHECKBOX
import mysql.connector
#from reportlab.pdfgen import canvas
import random

db = mysql.connector.connect(
    host     = "localhost",
    user     = "root",
    passwd   = "root",
    database = "cadastro_lanches"
)

def geraPdf():
    print('GERAR PDF')
    
    listagem.tablePedidos.clear()
    listagem.tablePedidos.setHorizontalHeaderLabels(['id', 'codigo', 'nome', 'descricao', 'Total'])

    pinicio = listagem.linePeriodoInicio.text()
    pfinal = listagem.linePeriodoFinal.text()
    if len(pinicio) != 0 and len(pfinal) != 0:
        cursor = db.cursor()
        comandoBusca = "SELECT id, codigo, nome, descricao, Total FROM pedidos WHERE (data BETWEEN "
        comandoBusca += "'" + str(pinicio) + "'"
        comandoBusca += " AND '"
        comandoBusca += str(pfinal) + "');" 
        cursor.execute(comandoBusca)
        resultBusca = cursor.fetchall()
        # print(resultBusca)
        print(f'Busca retornada com {len(resultBusca)} registros.')

        for i in range(0,len(resultBusca)):
            for j in range(0,5):
                listagem.tablePedidos.setItem(i,j,QtWidgets.QTableWidgetItem(str(resultBusca[i][j])))


def listaPedidos():
    print('LISTAGEM')
    listagem.show()

    cursor = db.cursor()
    comandoLista = "SELECT id, codigo, nome, descricao, Total FROM pedidos"
    cursor.execute(comandoLista)
    pedidosLista = cursor.fetchall()
    # for i in pedidosLista:
    #     print(pedidosLista[i])

    listagem.tablePedidos.setRowCount(len(pedidosLista))
    listagem.tablePedidos.setColumnCount(5) # id, codigo, nome, descricao, Total

    for i in range(0,len(pedidosLista)):
        for j in range(0,5):
            listagem.tablePedidos.setItem(i,j,QtWidgets.QTableWidgetItem(str(pedidosLista[i][j])))

def checkXTUDO():
    if formulario.radioXTUDO.isChecked():
        formulario.spinBoxXTUDO.setValue(1)
    else:
        formulario.spinBoxXTUDO.setValue(0)
def checkXSALADA():
    if formulario.radioXSALADA.isChecked():
        formulario.spinBoxXSALADA.setValue(1)
    else:
        formulario.spinBoxXSALADA.setValue(0)
def checkXBACON():
    if formulario.radioXBACON.isChecked():
        formulario.spinBoxXBACON.setValue(1)
    else:
        formulario.spinBoxXBACON.setValue(0)
def checkSIMPLES():
    if formulario.radioBurgerSIMPLES.isChecked():
        formulario.spinBoxSIMPLES.setValue(1)
    else:
        formulario.spinBoxSIMPLES.setValue(0)
def checkXDUPLO():
    if formulario.radioXDUPLO.isChecked():
        formulario.spinBoxXDUPLO.setValue(1)
    else:
        formulario.spinBoxXDUPLO.setValue(0)
def checkXCALAB():
    if formulario.radioXCALAB.isChecked():
        formulario.spinBoxXCALAB.setValue(1)
    else:
        formulario.spinBoxXCALAB.setValue(0)
def checkHotdog():
    if formulario.radioHotSimples.isChecked():
        formulario.spinBoxHotSimples.setValue(1)
    else:
        formulario.spinBoxHotSimples.setValue(0)
    if formulario.radioHotCompleto.isChecked():
        formulario.spinBoxHotCompleto.setValue(1)
    else:
        formulario.spinBoxHotCompleto.setValue(0)
def checkMisto():
    if formulario.radioMistoSimples.isChecked():
        formulario.spinBoxMistoSimples.setValue(1)
    else:
        formulario.spinBoxMistoSimples.setValue(0)
    if formulario.radioMistoCompleto.isChecked():
        formulario.spinBoxMistoCompleto.setValue(1)
    else:
        formulario.spinBoxMistoCompleto.setValue(0)
def checkAdicionais():
    if formulario.radioAddCheddar.isChecked():
        formulario.spinBoxAddCheddar.setValue(1)
    else:
        formulario.spinBoxAddCheddar.setValue(0)
    if formulario.radioAddOvo.isChecked():
        formulario.spinBoxAddOvo.setValue(1)
    else:
        formulario.spinBoxAddOvo.setValue(0)
    if formulario.radioAddCarne.isChecked():
        formulario.spinBoxAddCarne.setValue(1)
    else:
        formulario.spinBoxAddCarne.setValue(0)
    if formulario.radioAddCalab.isChecked():
        formulario.spinBoxAddCalab.setValue(1)
    else:
        formulario.spinBoxAddCalab.setValue(0)
    if formulario.radioAddBacon.isChecked():
        formulario.spinBoxAddBacon.setValue(1)
    else:
        formulario.spinBoxAddBacon.setValue(0)

def checkBebidas():
    if formulario.radioSuco.isChecked():
        formulario.spinBoxSuco.setValue(1)
    else:
        formulario.spinBoxSuco.setValue(0)
    if formulario.radioLata.isChecked():
        formulario.spinBoxLata.setValue(1)
    else:
        formulario.spinBoxLata.setValue(0)
    if formulario.radioKS.isChecked():
        formulario.spinBoxKS.setValue(1)
    else:
        formulario.spinBoxKS.setValue(0)
    if formulario.radio1lit.isChecked():
        formulario.spinBox1lit.setValue(1)
    else:
        formulario.spinBox1lit.setValue(0)
    if formulario.radio2lit.isChecked():
        formulario.spinBox2lit.setValue(1)
    else:
        formulario.spinBox2lit.setValue(0)

def inicializaOpcoes():
    formulario.radioXTUDO.stateChanged.connect(checkXTUDO)
    formulario.radioXSALADA.stateChanged.connect(checkXSALADA)
    formulario.radioXDUPLO.stateChanged.connect(checkXDUPLO)
    formulario.radioXBACON.stateChanged.connect(checkXBACON)
    formulario.radioBurgerSIMPLES.stateChanged.connect(checkSIMPLES)
    formulario.radioXCALAB.stateChanged.connect(checkXCALAB)
    formulario.radioHotSimples.stateChanged.connect(checkHotdog)
    formulario.radioHotCompleto.stateChanged.connect(checkHotdog)
    formulario.radioMistoSimples.stateChanged.connect(checkMisto)
    formulario.radioMistoCompleto.stateChanged.connect(checkMisto)
    formulario.radioAddCheddar.stateChanged.connect(checkAdicionais)
    formulario.radioAddOvo.stateChanged.connect(checkAdicionais)
    formulario.radioAddCarne.stateChanged.connect(checkAdicionais)
    formulario.radioAddCalab.stateChanged.connect(checkAdicionais)
    formulario.radioAddBacon.stateChanged.connect(checkAdicionais)
    formulario.radioSuco.stateChanged.connect(checkBebidas)
    formulario.radioKS.stateChanged.connect(checkBebidas)
    formulario.radioLata.stateChanged.connect(checkBebidas)
    formulario.radio1lit.stateChanged.connect(checkBebidas)
    formulario.radio2lit.stateChanged.connect(checkBebidas)

def ativaBotaoFinalizar():
    observ = "TESTE"
    nome,burg,mis,hot,add,beb,ped,tot = ativaBotaoAdicionar()
    cursor = db.cursor()
    comandoInsert = "INSERT INTO pedidos (codigo,nome,burgers,misto,hotdog,adicionais,bebidas,observacao,descricao,Total) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    dados = (random.randint(1,999),str(nome),burg,mis,hot,add,beb,str(observ),str(ped),tot)
    cursor.execute(comandoInsert,dados)
    db.commit()
    print('Dados cadastrados no Banco de Dados')

    #    formulario.restoreState()
    # Percorre todos os elementos e reseta
    # for i in range(formulario.find()): # veriricar o similar ao count()
    #     item = formulario.itemAt(i).widget()
    #     if isinstance(item,QtWidgets.QCheckBox):
    #         item.setChecked(False)
    #     if isinstance(item,QtWidgets.QSpinBox):
    #         item.setValue(0)
    #     if isinstance(item,QtWidgets.QLineEdit):
    #         item.setText("")

def ativaBotaoAdicionar():
    nome = formulario.lineNome.text()
    burgers = 0
    misto   = 0
    hotdog  = 0
    adic    = 0
    bebida  = 0
    total   = 0.0

    pedido = ""
    if len(nome) == 0:
        formulario.labelPedido.setText("PEDIDO DEVE TER UM NOME DE CLIENTE ASSOCIADO")
        formulario.labelPedido.setStyleSheet('color: #ff0000')
    else:
        formulario.labelPedido.setStyleSheet('color: #444')
        # formulario.labelPedido.text()
        if formulario.spinBoxXTUDO.value() != 0:
            burgers += formulario.spinBoxXTUDO.value()
            pedido += str(formulario.spinBoxXTUDO.value())
            pedido += " X-TUDO + "
            total += float(formulario.spinBoxXTUDO.value() * 7)
        if formulario.spinBoxXSALADA.value() != 0:
            burgers += formulario.spinBoxXSALADA.value()
            pedido += str(formulario.spinBoxXSALADA.value())
            pedido += " X-SALADA + "
            total += float(formulario.spinBoxXSALADA.value() * 4.5)
        if formulario.spinBoxXBACON.value() != 0:
            burgers += formulario.spinBoxXBACON.value()
            pedido += str(formulario.spinBoxXBACON.value())
            pedido += " X-BACON + "
            total += float(formulario.spinBoxXBACON.value() * 5)
        if formulario.spinBoxXDUPLO.value() != 0:
            burgers += formulario.spinBoxXDUPLO.value()
            pedido += str(formulario.spinBoxXDUPLO.value())
            pedido += " X-DUPLO + "
            total += float(formulario.spinBoxXDUPLO.value() * 6)
        if formulario.spinBoxXCALAB.value() != 0:
            burgers += int(formulario.spinBoxXCALAB.value())
            pedido += str(formulario.spinBoxXCALAB.value())
            pedido += " X-CALAB + "
            total += float(formulario.spinBoxXCALAB.value() * 5)    
        if formulario.spinBoxSIMPLES.value() != 0:
            burgers += int(formulario.spinBoxSIMPLES.value())
            pedido += str(formulario.spinBoxSIMPLES.value())
            pedido += " BurgerSIMPLES + "
            total += float(formulario.spinBoxSIMPLES.value() * 4.5)
        if formulario.spinBoxHotSimples.value() != 0:
            hotdog += formulario.spinBoxHotSimples.value()
            pedido += str(formulario.spinBoxHotSimples.value())
            pedido += " CACHORRO SIMPLES + "
            total += float(formulario.spinBoxHotSimples.value() * 2.5)
        if formulario.spinBoxHotCompleto.value() != 0:
            hotdog += formulario.spinBoxHotCompleto.value()
            pedido += str(formulario.spinBoxHotCompleto.value())
            pedido += " CACHORRO COMPLETO + "
            total += float(formulario.spinBoxHotSimples.value() * 4)
        if formulario.spinBoxMistoSimples.value() != 0:
            misto += formulario.spinBoxMistoSimples.value()
            pedido += str(formulario.spinBoxMistoSimples.value())
            pedido += " MISTO SIMPLES + "
            total += float(formulario.spinBoxMistoSimples.value() * 2)
        if formulario.spinBoxMistoCompleto.value() != 0:
            misto += formulario.spinBoxMistoCompleto.value()
            pedido += str(formulario.spinBoxMistoCompleto.value())
            pedido += " MISTO COMPLETO + "
            total += float(formulario.spinBoxMistoCompleto.value() * 3)
        if formulario.spinBoxAddCheddar.value() != 0:
            adic += formulario.spinBoxAddCheddar.value()
            pedido += "com mais " + str(formulario.spinBoxAddCheddar.value())
            pedido += " Cheddar + "
            total += float(2)
        if formulario.spinBoxAddOvo.value() != 0:   
            adic += formulario.spinBoxAddOvo.value()
            pedido += "com mais " + str(formulario.spinBoxAddOvo.value())
            pedido += " Ovo + "
            total += float(1)
        if formulario.spinBoxAddCarne.value() != 0:
            adic += formulario.spinBoxAddCarne.value()
            pedido += " com mais" + str(formulario.spinBoxAddCarne.value())
            pedido += " Carne + "
            total += float(3)
        if formulario.spinBoxAddCalab.value() != 0:
            adic += formulario.spinBoxAddCalab.value()
            pedido += "com mais " + str(formulario.spinBoxAddCalab.value())
            pedido += " Calabresa + "
            total += float(2)
        if formulario.spinBoxSuco.value() != 0:
            bebida += formulario.spinBoxSuco.value()
            pedido += str(formulario.spinBoxSuco.value())
            pedido += " Suco + "
            total += float(formulario.spinBoxSuco.value() * 4)
        if formulario.spinBoxLata.value() != 0:
            bebida += formulario.spinBoxLata.value()
            pedido += str(formulario.spinBoxLata.value())
            pedido += " Refri LATA + "
            total += float(formulario.spinBoxLata.value() * 3.5)
        if formulario.spinBoxKS.value() != 0:
            bebida += formulario.spinBoxKS.value()
            pedido += str(formulario.spinBoxKS.value())
            pedido += " Refri KS + "
            total += float(formulario.spinBoxKS.value() * 2)
        if formulario.spinBox1lit.value() != 0:
            bebida += formulario.spinBox1lit.value()
            pedido += str(formulario.spinBox1lit.value())
            pedido += " Refri 1L + "
            total += float(formulario.spinBox1lit.value() * 4.5)
        if formulario.spinBox2lit.value() != 0:
            bebida += formulario.spinBox2lit.value()
            pedido += str(formulario.spinBox2lit.value())
            pedido += " Refri 2L + "
            total += float(formulario.spinBox2lit.value() * 5.5)

        # Verifica o clique do botao de adicionar
        print('Botao clicado ')
        formulario.labelPedido.setText(pedido)
        formulario.labelPedido.setWordWrap(True)
        total_str = str(total)
        formulario.labelTotal.setText(total_str)
        # print(formulario.radioXTUDO.isChecked())    
        # print(formulario.spinBoxXTUDO.value())    
        # if len(nome) != 0:
        #     print('Pedido de ', nome)

        # CRIAR A OBSERVACAO COM CAMPO
        return nome, burgers, misto, hotdog, adic, bebida,  pedido, total


aplicacao = QtWidgets.QApplication([])
formulario = uic.loadUi("C:\\Users\\Miguel\\Documents\\Github\\PyQt+MySQL\\tela_vendas.ui")
# configura acoes do botao adicionar
formulario.btnAdicionar.clicked.connect(ativaBotaoAdicionar)
# configura acoes do botao finalizar
formulario.btnFinalizar.clicked.connect(ativaBotaoFinalizar)
# incializa as funcoes dos Widgets
inicializaOpcoes()

formulario.btnListar.clicked.connect(listaPedidos)

listagem = uic.loadUi("C:\\Users\\Miguel\\Documents\\Github\\PyQt+MySQL\\tela_lista.ui")
listagem.btnPesquisa.clicked.connect(geraPdf)

formulario.lineAddPrecoObs.setValidator(QtGui.QDoubleValidator(
                0.0, # bottom
                100.0, # top
                2, # decimals 
                notation=QtGui.QDoubleValidator.StandardNotation
            ))

formulario.show()
aplicacao.exec()

''' id | Codigo | Burgers | Misto | Hotdog | Adicionais | Bebidas | Observacao | Descricao | Total 
'''