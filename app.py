from ast import While
from asyncio import events
from multiprocessing import Event
from optparse import Values
from tkinter import Button, EventType
import PySimpleGUI as sg

def criar_janela_inicial():
    sg.theme('Dark2')
    linha = [
        [sg.Checkbox(''),sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas', layout=linha,key='container')],
        [sg.Button('Nova Tarefa'),sg.Button('Resetar')]
    ]

    return sg.Window('Gerenciador de Tarefas', layout=layout,finalize=True)
janela = criar_janela_inicial()

while True:
    event, Values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'],[[sg.Checkbox(''),sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()