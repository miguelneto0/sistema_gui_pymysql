from re import search
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from matplotlib import font_manager
import mysql.connector
#from reportlab.pdfgen import canvas
from fpdf import FPDF
import random
import pandas as pd

# Conectando o codigo com o banco de dados MySQL
db = mysql.connector.connect(
    host     = "localhost",
    user     = "root",
    passwd   = "root",
    database = "cadastro_lanches"
)

ultimaBusca = ""

# Definindo o calculo do lucro para a tabela atualizada
def calculaLucro():
    lucroFloat = 0.0
    lucro = ""

    print('CALCULA VALOR')
    for i in range(listagem.tablePedidos.rowCount()):
        for j in range(listagem.tablePedidos.columnCount()):
            leitura = listagem.tablePedidos.item(i,j)
            if leitura != None and j==4:
                lucroFloat += float(listagem.tablePedidos.item(i,j).text())
                lucro += listagem.tablePedidos.item(i,j).text()
                # print(lucro)
                # lucroFloat += float(lucro)
    print(lucroFloat)
    listagem.labelLucro.setText("R$ " + str(lucroFloat))
    listagem.labelLucro.setStyleSheet('Label {font:bold,font-size:14}')

# Definindo a geracao de Planilha em .CSV para Relatorios e Analises
def geraCSV():
    listagem.datePeriodoInicio.setDisplayFormat("yyyy-MM-dd hh:mm")
    listagem.datePeriodoFinal.setDisplayFormat("yyyy-MM-dd hh:mm")
    dtinicio = listagem.datePeriodoInicio.dateTime()
    dtfinal  = listagem.datePeriodoFinal.dateTime()
    pinicio = dtinicio.toString(listagem.datePeriodoInicio.displayFormat())
    pfinal = dtfinal.toString(listagem.datePeriodoFinal.displayFormat())
    if len(pinicio) != 0 and len(pfinal) != 0:
        cursor = db.cursor()
        comandoBusca = "SELECT id, codigo, nome, descricao, Total FROM pedidos WHERE (data BETWEEN "
        comandoBusca += "'" + str(pinicio) + "'"
        comandoBusca += " AND '"
        comandoBusca += str(pfinal) + "');" 
        cursor.execute(comandoBusca)
        resultBusca = cursor.fetchall()
        df = pd.DataFrame(resultBusca,columns=['id','codigo','nome','descricao','Total'])
        df.to_csv('Planilha_Relatorio_Pedidos.csv')

# Definindo a geracao do PDF do relatorio
def geraPDF():
    listagem.datePeriodoInicio.setDisplayFormat("yyyy-MM-dd hh:mm")
    listagem.datePeriodoFinal.setDisplayFormat("yyyy-MM-dd hh:mm")
    dtinicio = listagem.datePeriodoInicio.dateTime()
    dtfinal  = listagem.datePeriodoFinal.dateTime()
    pinicio = dtinicio.toString(listagem.datePeriodoInicio.displayFormat())
    pfinal = dtfinal.toString(listagem.datePeriodoFinal.displayFormat())
    if len(pinicio) != 0 and len(pfinal) != 0:
        linhas = pesquisa()
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.cell(200, 10, 'Relatorio de Pedidos',ln=1, align='C')
        for l in linhas:
            pdf.set_font('helvetica', '', 12)
            pdf.cell(0,20, f'{l}', ln=True, border=True)
            # altura_linha+= 10
        pdf.output('Relatorio_pedidos.pdf')

# Definindo o comportamento para o botao de pesquisa
def pesquisa():
    print('PESQUISA realizada')
    
    listagem.tablePedidos.clear()
    listagem.tablePedidos.setHorizontalHeaderLabels(['id', 'codigo', 'nome', 'descricao', 'Total'])
    
    listagem.datePeriodoInicio.setDisplayFormat("yyyy-MM-dd hh:mm")
    listagem.datePeriodoFinal.setDisplayFormat("yyyy-MM-dd hh:mm")
    dtinicio = listagem.datePeriodoInicio.dateTime()
    dtfinal  = listagem.datePeriodoFinal.dateTime()
    pinicio = dtinicio.toString(listagem.datePeriodoInicio.displayFormat())
    pfinal = dtfinal.toString(listagem.datePeriodoFinal.displayFormat())
    
    print(f'Inicio: {pinicio} \t Final: {pfinal}')
    # pinicio = listagem.linePeriodoInicio.text()
    # pfinal = listagem.linePeriodoFinal.text()
    if len(pinicio) != 0 and len(pfinal) != 0:
    # if len(dt_stringFIN) != 0 and len(dt_stringINI) != 0:
        cursor = db.cursor()
        comandoBusca = "SELECT id, codigo, nome, descricao, Total FROM pedidos WHERE (data BETWEEN "
        comandoBusca += "'" + str(pinicio) + "'"
        comandoBusca += " AND '"
        comandoBusca += str(pfinal) + "');" 
        cursor.execute(comandoBusca)
        resultBusca = cursor.fetchall()
        # print(resultBusca)
        df = pd.DataFrame(resultBusca,columns=['id','codigo','nome','descricao','Total'])
        print(df)
        df = df.astype(str)
        lista_pedidos = df.values.tolist()
        print(f'Busca retornada com {len(resultBusca)} registros.')
        listagem.labelDebug.setText('Busca retornada com ' + str(len(resultBusca)) + ' registros.')

        for i in range(0,len(resultBusca)):
            for j in range(0,5):
                listagem.tablePedidos.setItem(i,j,QtWidgets.QTableWidgetItem(str(resultBusca[i][j])))
        ultimaBusca = str(resultBusca)
        return lista_pedidos

# Definindo a busca por nome de cliente
def pesquisaNome():
    print('PESQUISA-NOME realizada')
    
    listagem.tablePedidos.clear()
    listagem.tablePedidos.setHorizontalHeaderLabels(['id', 'codigo', 'nome', 'descricao', 'Total'])

    nomeProc = listagem.lineNomeProc.text()
    
    if len(nomeProc) != 0:
    # if len(dt_stringFIN) != 0 and len(dt_stringINI) != 0:
        cursor = db.cursor()
        comandoBusca = "SELECT id, codigo, nome, descricao, Total FROM pedidos WHERE nome LIKE "
        comandoBusca += "'%" + str(nomeProc) + "%'"
        comandoBusca += ";" 
        cursor.execute(comandoBusca)
        resultBusca = cursor.fetchall()
        # print(resultBusca)
        df = pd.DataFrame(resultBusca,columns=['id','codigo','nome','descricao','Total'])
        print(df)
        df = df.astype(str)
        lista_pedidos = df.values.tolist()
        print(f'Busca retornada com {len(resultBusca)} registros.')
        listagem.labelDebug.setText('Busca retornada com ' + str(len(resultBusca)) + ' registros.')

        for i in range(0,len(resultBusca)):
            for j in range(0,5):
                listagem.tablePedidos.setItem(i,j,QtWidgets.QTableWidgetItem(str(resultBusca[i][j])))
        return lista_pedidos

# Definindo a busca por codigo de cliente
def pesquisaCod():
    print('PESQUISA-COD realizada')
    
    listagem.tablePedidos.clear()
    listagem.tablePedidos.setHorizontalHeaderLabels(['id', 'codigo', 'nome', 'descricao', 'Total'])

    codProc = listagem.lineCodigoProc.text()
    
    if len(codProc) != 0:
    # if len(dt_stringFIN) != 0 and len(dt_stringINI) != 0:
        cursor = db.cursor()
        comandoBusca = "SELECT id, codigo, nome, descricao, Total FROM pedidos WHERE codigo LIKE "
        comandoBusca += "'%" + str(codProc) + "%'"
        comandoBusca += ";" 
        cursor.execute(comandoBusca)
        resultBusca = cursor.fetchall()
        # print(resultBusca)
        df = pd.DataFrame(resultBusca,columns=['id','codigo','nome','descricao','Total'])
        print(df)
        df = df.astype(str)
        lista_pedidos = df.values.tolist()
        print(f'Busca retornada com {len(resultBusca)} registros.')
        listagem.labelDebug.setText('Busca retornada com ' + str(len(resultBusca)) + ' registros.')

        for i in range(0,len(resultBusca)):
            for j in range(0,5):
                listagem.tablePedidos.setItem(i,j,QtWidgets.QTableWidgetItem(str(resultBusca[i][j])))
        return lista_pedidos

# Definindo a busca por descricao do pedido de cliente
def pesquisaDescr():
    print('PESQUISA-DESCR realizada')
    
    listagem.tablePedidos.clear()
    listagem.tablePedidos.setHorizontalHeaderLabels(['id', 'codigo', 'nome', 'descricao', 'Total'])

    descrProc = listagem.lineDescricaoProc.text()
    
    if len(descrProc) != 0:
    # if len(dt_stringFIN) != 0 and len(dt_stringINI) != 0:
        cursor = db.cursor()
        comandoBusca = "SELECT id, codigo, nome, descricao, Total FROM pedidos WHERE descricao LIKE "
        comandoBusca += "'%" + str(descrProc) + "%'"
        comandoBusca += ";" 
        cursor.execute(comandoBusca)
        resultBusca = cursor.fetchall()
        # print(resultBusca)
        df = pd.DataFrame(resultBusca,columns=['id','codigo','nome','descricao','Total'])
        print(df)
        df = df.astype(str)
        lista_pedidos = df.values.tolist()
        print(f'Busca retornada com {len(resultBusca)} registros.')
        listagem.labelDebug.setText('Busca retornada com ' + str(len(resultBusca)) + ' registros.')

        for i in range(0,len(resultBusca)):
            for j in range(0,5):
                listagem.tablePedidos.setItem(i,j,QtWidgets.QTableWidgetItem(str(resultBusca[i][j])))
        return lista_pedidos

# Definindo o preenchimento da tabela com os pedidos
def listaPedidos():
    print('LISTAGEM')
    listagem.show()

    cursor = db.cursor()
    comandoLista = "SELECT id, codigo, nome, descricao, Total FROM pedidos;"
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

# Define o cadastro do pedido do cliente
def ativaBotaoFinalizar():
    observ = "TESTE"
    nome,burg,mis,hot,add,beb,ped,tot = ativaBotaoAdicionar()
    cursor = db.cursor()
    comandoInsert = "INSERT INTO pedidos (codigo,nome,burgers,misto,hotdog,adicionais,bebidas,observacao,descricao,Total) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    dados = (random.randint(1,999),str(nome),burg,mis,hot,add,beb,str(observ),str(ped),tot)
    cursor.execute(comandoInsert,dados)
    db.commit()
    print('Dados cadastrados no Banco de Dados')

# Define o preenchimento do carrinho
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

# Define o Login dos usuarios cadastrados
def botaoLogin():
    log = login.lineUser.text()
    psw = login.linePasswd.text()

    if len(log) != 0 and len(psw) != 0:
        cursor = db.cursor()
        comandoBusca = "SELECT nome,senha FROM admins WHERE nome="
        comandoBusca += "'" + str(log) + "'"
        cursor.execute(comandoBusca)
        resultBusca = cursor.fetchall()
        print(resultBusca)
        # print(resultBusca[0][0])
        # print(resultBusca[0][1])
        if log == resultBusca[0][0] and psw == resultBusca[0][1]:
            print(f'{log} logado com sucesso.')
            formulario.labelRastreioLogin.setText("Logado como " + str(log) + ".")
            login.close()
            formulario.show()
        else:
            login.labelNotificacao.setText("Usuario ou senha incorretos.")

# Define o logout do usuario            
def botaoLogout():
    formulario.close()
    login.show()

## ##################################################################
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
## ##################################################################

aplicacao = QtWidgets.QApplication([])
login = uic.loadUi("C:\\Users\\Miguel\\Documents\\Github\\PyQt+MySQL\\sistema_gui_pymysql\\tela_login.ui")

login.linePasswd.setEchoMode(QtWidgets.QLineEdit.Password)
login.btnLogin.clicked.connect(botaoLogin)

formulario = uic.loadUi("C:\\Users\\Miguel\\Documents\\Github\\PyQt+MySQL\\sistema_gui_pymysql\\tela_vendas.ui")
# configura acoes do botao adicionar
formulario.btnAdicionar.clicked.connect(ativaBotaoAdicionar)
# configura acoes do botao finalizar
formulario.btnFinalizar.clicked.connect(ativaBotaoFinalizar)
# incializa as funcoes dos Widgets
inicializaOpcoes()
# configura a acao de chamada da janela de pedidos
formulario.btnListar.clicked.connect(listaPedidos)
# configura a acao de chamada da janela de pedidos
formulario.btnLogout.clicked.connect(botaoLogout)


listagem = uic.loadUi("C:\\Users\\Miguel\\Documents\\Github\\PyQt+MySQL\\sistema_gui_pymysql\\tela_lista.ui")
listagem.btnPesquisa.clicked.connect(pesquisa)
listagem.btnGeraPDF.clicked.connect(geraPDF)
listagem.btnGeraCSV.clicked.connect(geraCSV)
listagem.btnLucro.clicked.connect(calculaLucro)
listagem.btnNomePesq.clicked.connect(pesquisaNome)
listagem.btnCodPesq.clicked.connect(pesquisaCod)
listagem.btnDescrPesq.clicked.connect(pesquisaDescr)

pdfIcon = QtGui.QIcon("images/pdf-icon.png")
csvIcon = QtGui.QIcon("images/csv-icon.png")
searchIcon = QtGui.QIcon('images/search-icon.png')

listagem.btnGeraCSV.setIcon(QtGui.QIcon(csvIcon))
listagem.btnGeraPDF.setIcon(QtGui.QIcon(pdfIcon))
listagem.btnPesquisa.setIcon(QtGui.QIcon(searchIcon))
listagem.btnNomePesq.setIcon(QtGui.QIcon(searchIcon))
listagem.btnCodPesq.setIcon(QtGui.QIcon(searchIcon))
listagem.btnDescrPesq.setIcon(QtGui.QIcon(searchIcon))

listagem.datePeriodoInicio.setDateTime(QtCore.QDateTime.currentDateTime())
listagem.datePeriodoInicio.setDisplayFormat("dd/MM/yyyy hh:mm")
listagem.datePeriodoFinal.setDateTime(QtCore.QDateTime.currentDateTime())
listagem.datePeriodoFinal.setDisplayFormat("dd/MM/yyyy hh:mm")

formulario.lineAddPrecoObs.setValidator(QtGui.QDoubleValidator(
                0.0,    # minimo
                100.0,  # maximo
                2,      # casa decimais 
                notation=QtGui.QDoubleValidator.StandardNotation
            ))

# formulario.show()
login.show()
aplicacao.exec()

''' id | Codigo | Burgers | Misto | Hotdog | Adicionais | Bebidas | Observacao | Descricao | Total 
'''