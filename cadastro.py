from PyQt5 import uic, QtWidgets
import mysql.connector
import numpy as np
import pandas as pd


#CRIAR UM BANCO DE DADOS NO MYSQL CHAMADO cadastro_produtos E CRIAR UMA TABELA CHAMADA produtos
#CAMINHO PARA ACESSO DEPOIS DE CRIADO:
#use cadastro_produtos;
#show tables;
#describe produtos;

#infos banco de dados mySql
banco = mysql.connector.connect(
    host="",
    user="",
    passwd = "",
    database = ""
)

def gerar_planilha():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos" #indica a tabela 
    cursor.execute(comando_SQL)
    dados_excel = cursor.fetchall() #executa tudo a cima
    
    #converte a tabela do banco de dados para tabela no excel
    col = 'id nome código validade tipo'.split()
    lin = dados_excel
    dados = pd.DataFrame(data=lin, columns=col)
    dados.to_excel('Produtos.xls')
             
def cadastro():
    
    #importar as linhas de texto pro python
    nome = form.lineEdit.text() 
    codigo = form.lineEdit_2.text() 
    validade = form.lineEdit_3.text() 
    
    tipo=""
    
    #definir o click dos botões
    if form.radioButton.isChecked() :
        print("Comida selecionada")
        tipo ="Comida"
        
    else:
        print("Bebida selecionada")
        tipo ="Bebida"
    
    
    #print feito para retornar um valor visivel para o terminal
    print('Teste')
    print(f'Nome: {nome}')
    print(f'Código: {codigo}')
    print(f'Validade: {validade}')
    
    
    #inserir os dados no banco
    cursor = banco.cursor()
    comando_SQL = "insert into produtos(nome, codigo, validade, tipo) values (%s,%s,%s,%s)"
    dados = (str(nome),str(codigo),str(validade),tipo)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    
    
    #apaga os campos após clicar o botão
    form.lineEdit.setText("") 
    form.lineEdit_2.setText("")
    form.lineEdit_3.setText("")
    
    

def mostra_lista():
    
    lista.show() #chamar a tela da lista 
    
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos" #indica a tabela 
    cursor.execute(comando_SQL)
    dados_lista = cursor.fetchall() #salva tudo a cima na variavel
    
    lista.tableWidget.setRowCount(len(dados_lista)) #setrowcount indicica quantas linhas vai ter a lista
    lista.tableWidget.setColumnCount(4) #quantidade de colunas
    
    for i in range (0, len(dados_lista)):
        for j in range(0,5):
            lista.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lista[i][j]))) #todo esse bloco le a lista
            
            

app = QtWidgets.QApplication([])

#import arquivos
lista = uic.loadUi("lista.ui") 
form = uic.loadUi("form.ui") 

#faz a conexao do botão com a def
form.pushButton.clicked.connect(cadastro)
form.pushButton_2.clicked.connect(mostra_lista)
lista.pushButton.clicked.connect(gerar_planilha)

form.show()
app.exec()

#use cadastro_produtos;
#show tables;
#describe produtos;
    