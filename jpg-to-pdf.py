from tkinter.constants import MULTIPLE
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

#configuração do workspace
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 330, bg = 'paleturquoise', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Conversor de arquivos', bg = 'paleturquoise')
label1.config(font=('Arial', 20))
canvas1.create_window(150, 60, window=label1)

imgs_paths = []
images = []

#função de captura do arquivo:
def getFile (): 
    root.call('wm', 'attributes', '.', '-topmost', True)
    file_paths = filedialog.askopenfilename(multiple=True)
    for img_path in file_paths:
        imgs_paths.append(img_path)

    for file_path in imgs_paths:
        image1 = Image.open(file_path)
        im = image1.convert('RGB')
        images.append(im)
    

browseButton = tk.Button(text="     Selecione o arquivo    ", command=getFile, bg='green', fg='white', font=('Arial', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton)

#pop-up de sucesso:
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Sucesso")
    label = tk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack(pady=5)
    popup.mainloop()
    

#função de conversão:
def convertpdf ():
    export_file_path = filedialog.asksaveasfilename(defaultextension='.pdf')
    images[0].save(export_file_path, save_all=True, append_images=images)
    popupmsg("Seu arquivo foi convertido com sucesso!")

saveAsButton = tk.Button(text='Converter para PDF', command=convertpdf, bg='green', fg='white', font=('Arial', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton)

#função de saída do aplicativo:
def exitApp():
    MsgBox = tk.messagebox.askquestion ('Sair da aplicação','Você tem certeza que deseja sair da aplicação?',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
     
exitButton = tk.Button (root, text='Sair da aplicação',command=exitApp, bg='brown', fg='white', font=('Arial', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()