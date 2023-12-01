import tkinter as tk
from tkinter import filedialog
import os

def verificar_arquivos():
    diretorio = filedialog.askdirectory(title="Selecione a pasta do arquivo")
    arquivos_encontrados = []

    for root, dirs, files in os.walk(diretorio):
        for file in files:
            if file.endswith(('.exe', '.bat')):
                arquivos_encontrados.append(os.path.join(root, file))

    if arquivos_encontrados:
        resultado_label.config(text="Arquivos encontrados:")
        lista_arquivos.delete(0, tk.END)  
        for arquivo in arquivos_encontrados:
            lista_arquivos.insert(tk.END, arquivo)
    else:
        resultado_label.config(text="Nenhum arquivo encontrado.")

def excluir_arquivo():
    index = lista_arquivos.curselection()

    if index:
        caminho_arquivo = lista_arquivos.get(index)
        os.remove(caminho_arquivo)
        lista_arquivos.delete(index)
        resultado_label.config(text="Arquivo excluído com sucesso.")
    else:
        resultado_label.config(text="Nenhum arquivo selecionado.")

janela = tk.Tk()
janela.title("Anti-virus")

frame1 = tk.Frame(janela)
frame1.pack(pady=10)

selecionar_botao = tk.Button(frame1, text="Selecionar pasta/arquivo", command=verificar_arquivos)
selecionar_botao.pack(side=tk.LEFT, padx=10)

excluir_botao = tk.Button(frame1, text="Excluir arquivo", command=excluir_arquivo)
excluir_botao.pack(side=tk.LEFT)

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

lista_arquivos = tk.Listbox(janela, selectmode=tk.SINGLE, width=100, height=15)
lista_arquivos.pack(pady=10)

janela.mainloop()
