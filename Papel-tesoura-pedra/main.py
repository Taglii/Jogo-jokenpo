import tkinter
from tkinter import *
from tkinter import ttk

# importando o pillow
from PIL import Image, ImageTk

import random

# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha
fundo = "#3b3b3b"

#configurando a janela
janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)


# dividindo a janela

frame_cima = Frame(janela, width=260, height=100, bg= co1, relief='raised')
frame_cima.grid(row = 0, column = 0, sticky=NW)
frame_baixo = Frame(janela, width=360, height=300, bg= co0, relief='flat')
frame_baixo.grid(row = 1, column = 0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# configurando o frame de cima

app_1 = Label(frame_cima, text= "Jogador", height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_1.place(x=35, y=70)
app_1_linha = Label(frame_cima, text= "", height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_1_linha.place(x=0, y=0)

app_1_point = Label(frame_cima, text= "0", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_1_point.place(x=50, y=20)

app_ = Label(frame_cima, text= ":", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_.place(x=125, y=20)

app_2_point = Label(frame_cima, text= "0", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_2_point.place(x=190, y=20)

app_2 = Label(frame_cima, text= "Maquina", height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_2.place(x=174, y=70)

app_2_linha = Label(frame_cima, text= "", height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_2_linha.place(x=255, y=0)


app_linha_empate = Label(frame_cima, text= "", width=255 ,anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co0)
app_linha_empate.place(x=0, y=95)


app_maquina = Label(frame_baixo, text= "", height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_maquina.place(x=190, y=10)


global voce
global maquina
global rodadas
global pontos_voce
global pontos_maquina

pontos_voce = 0
pontos_maquina = 0
rodadas = 5

# função logica do jogo
def jogar(i):
    global rodadas
    global pontos_voce
    global pontos_maquina

    if rodadas > 0:
        print(rodadas)
        opcoes = ['Pedra','Papel', 'Tesoura']
        maquina = random.choice(opcoes)
        voce = i
        
        app_maquina ['text'] = maquina
        app_maquina ['fg'] = co1

        # Empate
        if voce == 'Pedra' and maquina == 'Pedra':
            print('Empate')
            app_1_linha ['bg'] = co0
            app_2_linha ['bg'] = co0
            app_linha_empate ['bg'] = co3
            
        elif voce == 'Papel' and maquina == 'Papel':
            print('Empate')
            app_1_linha ['bg'] = co0
            app_2_linha ['bg'] = co0
            app_linha_empate ['bg'] = co3

        elif voce == 'Tesoura' and maquina == 'Tesoura':
            print('Empate')
            app_1_linha ['bg'] = co0
            app_2_linha ['bg'] = co0
            app_linha_empate ['bg'] = co3
        
        # pedra/tesoura e pedra/papel
        elif voce == 'Pedra' and maquina == 'Tesoura':
            print('Ponto do jogador')
            app_1_linha ['bg'] = co4
            app_2_linha ['bg'] = co0
            app_linha_empate ['bg'] = co0
            pontos_voce +=10
            

        elif voce == 'Pedra' and maquina == 'Papel':
            print('Ponto da maquina')
            app_1_linha ['bg'] = co0
            app_2_linha ['bg'] = co4
            app_linha_empate ['bg'] = co0
            pontos_maquina += 10

        # Tesoura/papel e Tesoura/pedra
        elif voce == 'Tesoura' and maquina == 'Papel':
            print('Ponto do jogador')
            app_1_linha ['bg'] = co4
            app_2_linha ['bg'] = co0
            app_linha_empate ['bg'] = co0
            pontos_voce +=10
            

        elif voce == 'Tesoura' and maquina == 'Pedra':
            print('Ponto da maquina')
            app_1_linha ['bg'] = co0
            app_2_linha ['bg'] = co4
            app_linha_empate ['bg'] = co0
            pontos_maquina += 10
        
        # Papel/Pedra e Papel/Tesoura
        elif voce == 'Papel' and maquina == 'Pedra':
            print('Ponto do jogador')
            app_1_linha ['bg'] = co4
            app_2_linha ['bg'] = co0
            app_linha_empate ['bg'] = co0
            pontos_voce += 10
           

        elif voce == 'Papel' and maquina == 'Tesoura':
            print('Ponto da maquina')
            app_1_linha ['bg'] = co0
            app_2_linha ['bg'] = co4
            app_linha_empate ['bg'] = co0
            pontos_maquina += 10


        # atualização de pontos
        app_1_point['text'] = pontos_voce
        app_2_point['text'] = pontos_maquina

        # atualização de rodadas
        rodadas -= 1 
        

    else:
        app_1_point['text'] = pontos_voce
        app_2_point['text'] = pontos_maquina

        # chamando a função terminar o jogo

        fim_jogo()
       





# função para iniciar o jogo

def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3
    b_icon_jogar.destroy()

# Pedra
    icon_1 = Image.open('imagens/pedra.png')
    icon_1 = icon_1.resize((60, 60), Image.Resampling.LANCZOS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_baixo, command= lambda: jogar('Pedra'), width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_1.place(x=20, y=60)
# Papel
    icon_2 = Image.open('imagens/papel.png')
    icon_2 = icon_2.resize((60, 60), Image.Resampling.LANCZOS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_baixo, command= lambda: jogar('Papel'), width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_2.place(x=110, y=60)
# Tesoura 
    icon_3 = Image.open('imagens/tesoura.png')
    icon_3 = icon_3.resize((50, 50), Image.Resampling.LANCZOS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_baixo, command= lambda: jogar('Tesoura'), width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_3.place(x=190, y=60)


# função de terminar o jogo

def fim_jogo():
    global rodadas
    global pontos_voce
    global pontos_maquina

    # reiniciando as variaveis para 0
    pontos_voce = 0
    pontos_maquina = 0
    rodadas = 5

    # Tirando os botoes de opções
    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()

    # Calculando o vencedor
    pessoa = int(app_1_point ['text'] )
    jogador_maquina = int(app_2_point ['text'] )

    if pessoa > jogador_maquina:
        app_vencedor = Label(frame_baixo, text= "Parabéns você Ganhou !!!", height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co4)
        app_vencedor.place(x=30, y=60)
    elif pessoa < jogador_maquina:
        app_vencedor = Label(frame_baixo, text= "Perdeuuuu hehe!!", height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co5)
        app_vencedor.place(x=30, y=60)
    else:
        app_vencedor = Label(frame_baixo, text= "Foi um empate", height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
        app_vencedor.place(x=5, y=60)

    # Jogando de novo
    def jogar_dnv():
        app_1_point ['text'] = 0
        app_2_point ['text'] = 0
        app_vencedor.destroy()

        b_jogar_dnv.destroy()
        iniciar_jogo()

        
    b_jogar_dnv = Button(frame_baixo, command=jogar_dnv, width=30, text="Jogar novamente", bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    b_jogar_dnv.place(x=5, y=150)




# configurando o frame de baixo

# botao pra inicio

b_icon_jogar = Button(frame_baixo, command=iniciar_jogo, width=30, text="Começe a jogar!", bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_icon_jogar.place(x=5, y=150)








#loop da janela
janela.mainloop()


