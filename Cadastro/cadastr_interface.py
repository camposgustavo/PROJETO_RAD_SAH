import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#from tkcalendar import DateEntry

#funções para os botões
def salvar(): 
    messagebox.showinfo("Salvar", "Cliente Salvo!")
#função para fechar a janela ao clicar no botão "Cancelar"
def Cancelar(): 
    root.destroy()

#configuração da janela principal
root = tk.Tk()
root.title("Sistema de Hotel - Cadastro")

#definição a dimensão da janela (largura X altura)
root.geometry("600x600") #define a largura para 600 pixels e altura para 300 pixels

#adiona um titulo a janela
title = tk.Label(root, text="Cadastro", font=("arial", 15))
title.pack(pady=10)

#menu interação
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Arquivo", menu=file_menu)
file_menu.add_command(label="Novo")
file_menu.add_separator()
file_menu.add_command(label="Sair", command=root.quit)

#cadastro
form_frame= tk.Frame(root)
form_frame.pack(padx=20, pady=20)

#Campo Nome
tk.Label(form_frame, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(form_frame)
entry_name.grid(row=0, column= 1, padx=5, pady=5)

#campo cpf
tk.Label(form_frame, text="CPF:").grid(row=1, column=0, padx=5, pady=5)
entry_cpf = tk.Entry(form_frame)
entry_cpf.grid(row=1, column=1, padx=5, pady=5)

#campo quarto
tk.Label(form_frame, text='Quarto:').grid(row=2, column=0, padx=5, pady=5)
entry_quarto=tk.Entry(form_frame)
entry_quarto.grid(row=2,column=1,padx=5,pady=5)

'''#campo check-in
tk.Label(form_frame, text="Check-in:").grid(row=3, column=0, padx=5, pady=5)
entry_checkin = DateEntry(form_frame, date_pattern='dd/mm/yyyy', width=12)
entry_checkin.grid(row=3, column=1, padx=5, pady=5)

#campo check-out
tk.Label(form_frame, text="Check-out:").grid(row=4, column=0, padx=5, pady=5)
entry_checkout = DateEntry(form_frame, date_pattern='dd/mm/yyyy', width=12)
entry_checkout.grid(row=4, column=1, padx=5, pady=5)'''

#botão de opção café da manhã
tk.Label(form_frame, text="Escolha uma opção: ").grid(row=5, column=0, padx=5, pady=5)
opcao_escolhida=tk.StringVar()
tk.Radiobutton(form_frame, text="Café da Manhã",variable=opcao_escolhida,value="CafédaManhã").grid(row=5, column=1, padx=5, pady=5)
tk.Radiobutton(form_frame, text="Sem Café da Manhã", variable=opcao_escolhida, value="SemCafédaManhã").grid(row=5, column=2, padx=5, pady=5)

#periodo
ttk.Label(form_frame, text="periodo: ").grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
entry_per = tk.Entry(form_frame)
entry_per.grid(row=6, column=1, padx=5, pady=5)

#botões
button_frame=tk.Frame(root)
button_frame.pack(pady=10)

# botão para salvar o cadastro
salvar_button = tk.Button(button_frame, text="Salvar", command=salvar)
salvar_button.grid(row=7, column=0, padx=5) #adiciona o botão frame

# botão para cancelar o cadastro 
cancelar_button = tk.Button(button_frame, text="cancelar", command=Cancelar)
cancelar_button.grid(row=7, column=1, padx=5) #Adiciona o botão frame 

#Inicia o loop principal da interface grafica

if __name__ == "__main__":
    root.mainloop()