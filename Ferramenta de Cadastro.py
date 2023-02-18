
# Importar as libs
import customtkinter as tk
from tkinter import ttk
import datetime as dt

lista_tipos = ["Galão", 'Caixa', 'Saco', 'Unidade']
lista_codigos = []

# Criar uma janela
janela = tk.CTk()

# Criação da Função

def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quant = entry_quant.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime('%d/%m/%Y %H:%M')
    codigo = len(lista_codigos)+1
    codigo_str = "COD-{}".format(codigo)
    lista_codigos.append((codigo_str, descricao, tipo, quant, data_criacao))



# Titulo da janela
janela.title('Ferramenta de Cadastro de Materiais')

# Descrição
label_descricao = tk.CTkLabel(janela, text='Descrição do Material')
label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

# Estrutura do texto
entry_descricao = tk.CTkEntry(janela)
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)


label_tipo_unidade = tk.CTkLabel(janela, text="Tipo da unidade do Material")
label_tipo_unidade.grid(row=3, column=0,padx = 10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx = 10, pady=10, sticky='nswe', columnspan = 2)

label_quantidade = tk.CTkLabel(janela, text='Quantidade na unidade de material')
label_quantidade.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_quant = tk.CTkEntry(janela)
entry_quant.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

botao_criar_codigo = tk.CTkButton(janela, text='Criar Código', command=inserir_codigo)
botao_criar_codigo.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)




janela.mainloop()

print(lista_codigos)
