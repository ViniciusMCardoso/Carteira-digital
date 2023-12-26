import PySimpleGUI as sg

try:
    arq_saldo = open('saldo.txt', 'r')
except FileNotFoundError:
    arq_saldo = open('saldo.txt', 'w')
    arq_saldo.write('0') 
arq_saldo.close()

arq_pagador = open('pagadores.txt','a')
arq_recebedor = open('recebedores.txt','a')
arq_saldo = open('saldo.txt',"r")
saldo = arq_saldo.read()
arq_saldo.close()


def saldo_atualizado():
     arq_saldo = open('saldo.txt','r')
     return arq_saldo.read()


def criar_janela1():
    layout = [
                [sg.Button('Pagar')],
                [sg.Button('Receber')],
                [sg.Button('Saldo')],
                [sg.Button('Sair')],
             ]
    return sg.Window('Extrado Digital', layout, finalize=True)


def criar_janela2():
    layout = [
                [sg.Text('Dados do Recebedor: ')],
                [],
                [sg.Text('Quantia a pagar: '), sg.Input(key='quantia')],
                [sg.Text('Nome:  '), sg.Input(key='nome')],
                [sg.Button('Salvar'), sg.Button('Sair')],
             ]
    return sg.Window('Alunos', layout, finalize=True)


def criar_janela3():
    layout = [
                [sg.Text('Dados do Pagador: ')],
                [],
                [sg.Text('Quantia recebida: '), sg.Input(key='quantiap')],
                [sg.Text('Nome:  '), sg.Input(key='nomep')],
                [sg.Button('Salvar'), sg.Button('Sair')],
             ]
    return sg.Window('Alunos', layout, finalize=True)


def criar_janela4():
    layout = [
                [sg.Text('Saldo Atual '),sg.Text(saldo,key='saldo')],
                [sg.Button('Sair')],
             ]
    return sg.Window('Alunos', layout, finalize=True)


janela1, janela2, janela3, janela4 = criar_janela1(), None , None , None


print(saldo_atualizado())


while True:
     window, event, values = sg.read_all_windows()
     if window == janela1 and event in (sg.WIN_CLOSED, 'Sair'):
          break


     if window == janela1:
          if event == 'Pagar':
               janela1.hide()
               janela2 = criar_janela2()
          if event == 'Receber':
               janela1.hide()
               janela3 = criar_janela3()
          if event == 'Saldo':
               janela1.hide()
               janela4 = criar_janela4()
         
   
     if window == janela2:
        if event and event in (sg.WIN_CLOSED, 'Sair'):
               janela2.close()
               janela1.un_hide()
        if event == 'Salvar':
               arq_saldo = open('saldo.txt',"w")
               matp = float(values['quantia'])
               nome = values['nome']
               arq_pagador.write(f"{matp} --> {nome} \n")
               saldo = float(saldo) - matp
               arq_saldo.write(f"{saldo}")
               janela2['quantia'].update('')
               janela2['nome'].update('')
               arq_saldo.close()
     if window == janela3:
          if event and event in (sg.WIN_CLOSED, 'Sair'):
               janela3.close()
               janela1.un_hide()
          if event == 'Salvar':
               arq_saldo = open('saldo.txt',"w")
               mat = values['quantiap']
               nome = values['nomep']
               arq_recebedor.write(mat+' --> '+nome+'\n')
               saldo = float(saldo) + float(mat)
               arq_saldo.write(f"{saldo}")
               janela3['quantiap'].update('')
               janela3['nomep'].update('')
               arq_saldo.close()
     
     if window == janela4:
          if event and event in (sg.WIN_CLOSED, 'Sair'):
               janela4.close()
               janela1.un_hide()
          if event == 'Salvar':
               arq_saldo = open('saldo.txt',"w")
               saldo = values['saldo'] + values['saldoa'] - values['saldo']
               arq_saldo.write(saldo)
               janela4['saldo'].update(f'{saldo}')
               arq_saldo.close()


window.close()