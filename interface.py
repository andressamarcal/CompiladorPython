# importa a biblioteca que ira trabalhar com o GUI (interface visual)
from Tkinter import *

# Cria a tela
root = Tk()
# widget texto, i sera argumento de label e a janela que sobresai
#fg e bg  sao parametros para cores 
i = Label(root, text="Welcome!!!")
# joga na tela o que foi definido, usado para empacotar o que escreve dentro da tela
i.pack()

# define o tamanho da janela, largura x altura em numero de pixels
root.geometry("800x600")
# define o nome que ficara na janela
root.title("Compilador Python")

root.mainloop()

root.wm_iconbitmap("icone.ico")