#importando tkinter

from cProfile import label
from re import A
from tkinter import*
from tkinter import ttk
from turtle import bgcolor
from asyncio.proactor_events import _ProactorDuplexPipeTransport

from matplotlib.pyplot import text



#Cores/Color
cor1 = "#2e2e2d" #black/preta claro
cor2 = "#3b3b3b" #black/ preto escuro
cor3 = "#38576b" #Azul carregado
cor4 = "#ECEFF1" #Cinzenta
cor5 = "#FFAB40" #Orange/Laranja

#Janela Principal
janela = Tk()
janela.title("Calculadora")
janela.geometry("237x318")
janela.config(bg=cor1)


#Janela de Resultado
frame_tela = Frame(janela, width=237, height=50, bg=cor2)
frame_tela.grid(row=0, column=0)

#Janela de Corpo
frame_corpo = Frame(janela, width=237, height=268, bg=cor1)
frame_corpo.grid(row=1, column=0)




#Criando Label

valor_texto = StringVar()

# Variavel Todo Valores

todos_valores = ''
    
#Criando Função

def entrar_valores(evento):

    global todos_valores

    todos_valores = todos_valores + str(evento)

#Passando valor na Tela

    valor_texto.set(todos_valores)


#Função pra Calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))



#Função Limpar Tela

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")
    

app_label = Label(frame_tela, textvariable= valor_texto, bg=cor1, fg=cor4, justify=RIGHT, height=2, width=15, padx=7, relief=FLAT, anchor="e", font=('Ivy 18 bold'))
app_label.place(x=0,y=0)

#Botões

                            # 1° Linha de botões
#Clean
b_1 = Button(frame_corpo, command= limpar_tela, text="C", width=11, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=2)

#Modulo
b_2 = Button(frame_corpo, command = lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=2)

#Divisão
b_3 = Button(frame_corpo,command = lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=180, y=2)


                            # 2° Linha de botões
#7
b_4 = Button(frame_corpo,command = lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=55)

#8
b_5 = Button(frame_corpo, command = lambda: entrar_valores('8'),text="8", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=55)

#9
b_6 = Button(frame_corpo, command = lambda: entrar_valores('9'),text="9", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=55)

#*
b_7 = Button(frame_corpo, command = lambda: entrar_valores('*'),text="*", width=5, height=2, bg=cor5, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=180, y=55)


                            # 3° Linha de botões

#4
b_8 = Button(frame_corpo, command = lambda: entrar_valores('4'),text="4", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=108)

#5
b_9 = Button(frame_corpo, command = lambda: entrar_valores('5'),text="5", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=60, y=108)

#6
b_10 = Button(frame_corpo, command = lambda: entrar_valores('6'),text="6", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=120, y=108)

#-
b_11 = Button(frame_corpo, command = lambda: entrar_valores('-'),text="-", width=5, height=2, bg=cor5, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=180, y=108)

                            # 4° Linha de botões

#1
b_12 = Button(frame_corpo, command = lambda: entrar_valores('1'),text="1", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=161)

#2
b_13 = Button(frame_corpo, command = lambda: entrar_valores('2'),text="2", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=60, y=161)

#3
b_14 = Button(frame_corpo, command = lambda: entrar_valores('3'),text="3", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=120, y=161)

#+
b_15 = Button(frame_corpo, command = lambda: entrar_valores('+'),text="+", width=5, height=2, bg=cor5, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=180, y=161)


                            # 5° Linha de botões
#0
b_16 = Button(frame_corpo, command = lambda: entrar_valores('0'),text="0", width=11, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=214)

#Ponto(.)
b_17 = Button(frame_corpo, command = lambda: entrar_valores('.'),text=".", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=120, y=214)

#Igual(=)
b_18 = Button(frame_corpo, command = calcular, text="=", width=5, height=2, bg=cor5, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=180, y=214)




janela.mainloop()