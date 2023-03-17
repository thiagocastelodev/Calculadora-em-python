from tkinter import *
from functools import partial
import Operaçoes


def Botao_Zero():
    entrada.insert(entrada.index(INSERT), '0')


def Botao_Mais():
    entrada.insert(entrada.index(INSERT), '+')


def Botao_Menos():
    entrada.insert(entrada.index(INSERT), '-')


def Botao_Barra():
    entrada.insert(entrada.index(INSERT), '/')


def Botao_Mult():
    entrada.insert(entrada.index(INSERT), 'x')


def Botao_Ponto():
    entrada.insert(entrada.index(INSERT), '.')


def Botao_Fib():
    entrada.insert(entrada.index(INSERT), '!')


def Botao_Porc():
    entrada.insert(entrada.index(INSERT), '%')


def Botao_parentese():
    entrada.insert(entrada.index(INSERT), '()')


def Botao_Clear():
    entrada.delete(0, END)
    entrada.configure(text='')


def Botao_InserirNumero(n):
    entrada.insert(entrada.index(INSERT), f'{n}')


def Botao_Igual():
    if entrada.get() != '':
        Resultado = Operaçoes.Calcular(entrada.get())
        Botao_Clear()
        entrada.insert(END, Resultado)
    else:
        pass


def Botao_Enter(event):
    Botao_Igual()


validos = ['+', '-', 'x', '/', '%', '!', '.', '0',
           '1', '2', '3', '4', '5', '6', '7', '8', '9', '()', '(', ')']


def Valida_Entrada(input):
    if input in validos:
        return True
    elif len(input) > 1 and len(input) == len([c for c in input if c in validos]):
        return True
    else:
        return False


tela = Tk()
tela.title('Calculadora')
tela.resizable(False, False)
tela.iconbitmap('Imagens/Calculadora - ICON.ico')

fonte1 = ('Century', '20')

frame1 = Frame(tela, bg='#D3D3D3', border=1)
frame1.pack()

entrada = Entry(frame1, font=fonte1, width=18, justify=CENTER)
entrada.grid(columnspan=4)
entrada.focus()
reg = entrada.register(Valida_Entrada)
entrada.config(validate="key", validatecommand=(reg, '%S'))

botao_clear = Button(frame1, text='C', background='#ff3353',
                     font=fonte1, width=3, command=Botao_Clear, fg='white')
botao_clear.grid(row=1, column=0, padx=3, pady=3)

botao_fib = Button(frame1, text='!', font=fonte1, width=3,
                   command=Botao_Fib, bg='#00BFFF', fg='white')
botao_fib.grid(row=1, column=1, padx=3)

botao_porc = Button(frame1, text='%', font=fonte1, width=3,
                    command=Botao_Porc, bg='#00BFFF', fg='white')
botao_porc.grid(row=1, column=2, padx=3)

botao_divisao = Button(frame1, text='/', font=fonte1,
                       width=3, command=Botao_Barra, bg='#00BFFF', fg='white')
botao_divisao.grid(row=2, column=3, padx=3)

botao_multiplicaçao = Button(
    frame1, text='x', font=fonte1, width=3, command=Botao_Mult, bg='#00BFFF', fg='white')
botao_multiplicaçao.grid(row=3, column=3, pady=3, padx=3)

botao_subtraçao = Button(frame1, text='-', font=fonte1,
                         width=3, command=Botao_Menos, bg='#00BFFF', fg='white')
botao_subtraçao.grid(row=4, column=3, pady=3, padx=3)

botao_soma = Button(frame1, text='+', font=fonte1, width=3,
                    command=Botao_Mais, bg='#00BFFF', fg='white')
botao_soma.grid(row=5, column=3, pady=3, padx=3)

botao_igual = Button(frame1, text='=', font=fonte1,
                     width=3, command=Botao_Igual, bg='#1fc162', fg='white')
botao_igual.grid(row=5, column=2, pady=3, padx=3)

botao_Botao_ponto = Button(
    frame1, text='.', font=fonte1, width=3, command=Botao_Ponto, bg='#4F4F4F', fg='white')
botao_Botao_ponto.grid(row=5, column=1, pady=3, padx=3)

botao_parentese = Button(
    frame1, text='( )', background='#00BFFF', font=fonte1, width=3, command=Botao_parentese, fg='white')
botao_parentese.grid(row=1, column=3, padx=3, pady=3)

column, row = 0, 4

for b in range(1, 10):
    botao = Button(frame1, text=f'{b}', font=fonte1,
                   width=3, command=partial(Botao_InserirNumero, b), bg='#4F4F4F', fg='white')
    botao.grid(row=row, column=column, pady=3, padx=3)
    if not b % 3 == 0:
        column += 1
    else:
        column, row = 0, row - 1

botao_Botao_zero = Button(frame1, text='0', font=fonte1,
                          width=3, command=Botao_Zero, bg='#4F4F4F', fg='white')
botao_Botao_zero.grid(row=5, column=0, pady=3, padx=3)

entrada.bind('<Return>', Botao_Enter)

tela.mainloop()
