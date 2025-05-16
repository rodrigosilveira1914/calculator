#importação das bibliotecas
from tkinter import *
from tkinter import ttk

#definição das cores
cor1 = "#000000"  # preto
cor2 = "#feffff"  # branco
cor3 = "#38576b"  # azul 
cor4 = "#ECEFF1"  # cinza
cor5 = "#FFAB40"  # laranja

#criação do "aplicativo"
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.resizable(width=FALSE, height=FALSE)
janela.config(bg=cor1)

#criação do display
display = Frame(janela, width=235, height=50, bg=cor3)
display.grid(row=0, column=0)

#criação do quadro com botões
quadro = Frame(janela, width=235, height=268)
quadro.grid(row=1, column=0)

#determinação de variáveis
valor_recebido = ""

#criação do label
valor_texto = StringVar()

app_label = Label(display, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy", 18), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

#criação da função para permitir a passagem dos valores para a tela
def valores(argumentos):
    global valor_recebido
    valor_recebido += str(argumentos)  #concatenação dos valores dos botões após o clique
    valor_texto.set(valor_recebido)

#criação da função que calculam os valores
def calcular():
    global valor_recebido
    resultado = eval(valor_recebido)
    valor_texto.set(str(resultado))

#criação da função que limpa a tela
def limpar_tela():
    global valor_recebido
    valor_recebido = ""
    valor_texto.set("")

#criação dos botões
b1 = Button(quadro, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=("Ivy", 13, "bold"), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(quadro, command = lambda: valores("%"), text="%", width=5, height=2, bg=cor4, font=("Ivy", 13, "bold"), relief=RAISED, overrelief=RIDGE)
b2.place(x=118, y=0)
b3 = Button(quadro, command = lambda: valores("/"), text="/", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy", 13, "bold"), relief=RAISED, overrelief=RIDGE)
b3.place(x=177, y=0)

b4 = Button(quadro, command = lambda: valores("7"), text="7", width=5, height=2, bg=cor4, font=("Ivy", 13, "bold"), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=52)
b5 = Button(quadro, command = lambda: valores("8"), text="8", width=5, height=2, bg=cor4, font=("Ivy", 13, "bold"), relief=RAISED, overrelief=RIDGE)
b5.place(x=59, y=52)
b6 = Button(quadro, command = lambda: valores("9"), text="9", width=5, height=2, bg=cor4, font=("Ivy", 13, "bold"), relief=RAISED, overrelief=RIDGE)
b6.place(x=118, y=52)
b7 = Button(quadro, command = lambda: valores("*"), text="*", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy", 13, "bold"), relief=RAISED, overrelief=RIDGE)
b7.place(x=177, y=52)

b8 = Button(quadro, command = lambda: valores("4"), text="4", width=5, height=2, bg=cor4, font=("Ivy", 13, "bold"), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=104)
b9 = Button(quadro, command = lambda: valores("5"), text="5", width=5, height=2, bg=cor4, font=("Ivy", 13, "bold"), relief=RAISED, overrelief=RIDGE)
b9.place(x=59, y=104)
b10 = Button(quadro, command = lambda: valores("6"), text="6", width=5, height=2, bg=cor4, font=("Ivy", 13, "bold"), relief=RAISED, overrelief=RIDGE)
b10.place(x=118, y=104)
b11 = Button(quadro, command = lambda: valores("-"), text="-", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy", 13, "bold"), relief=RAISED, overrelief=RIDGE)
b11.place(x=177, y=104)
 
b12 = Button(quadro, command = lambda: valores("1"), text="1", width=5, height=2, bg=cor4, font=("Ivy", 13, "bold"), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=156)
b13 = Button(quadro, command = lambda: valores("2"), text="2", width=5, height=2, bg=cor4, font=("Ivy", 13, "bold"), relief=RAISED, overrelief=RIDGE)
b13.place(x=59, y=156)
b14 = Button(quadro, command = lambda: valores("3"), text="3", width=5, height=2, bg=cor4, font=("Ivy", 13, "bold"), relief=RAISED, overrelief=RIDGE)
b14.place(x=118, y=156)
b15 = Button(quadro, command = lambda: valores("+"), text="+", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy", 13, "bold"), relief=RAISED, overrelief=RIDGE)
b15.place(x=177, y=156)

b16 = Button(quadro, command = lambda: valores("0"), text="0", width=11, height=2, bg=cor4, font=("Ivy", 13, "bold"), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=208)
b17 = Button(quadro, command = lambda: valores("."), text=".", width=5, height=2, bg=cor4, font=("Ivy", 13, "bold"), relief=RAISED, overrelief=RIDGE)
b17.place(x=118, y=208)
b18 = Button(quadro, command = calcular,  text="=", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy", 13, "bold"), relief=RAISED, overrelief=RIDGE)
b18.place(x=177, y=208)

janela.mainloop()


