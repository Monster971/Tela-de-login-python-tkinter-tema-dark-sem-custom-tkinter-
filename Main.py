import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Login")
janela.geometry("400x300")
janela.configure(bg="#2e2e2e")


#funções
def registro():
    username = entrada_username.get()
    senha = entrada_senha.get()

    if username == "root" and senha == "12345":
        messagebox.showinfo("Login", "Login bem-sucedido")
    else:
        messagebox.showerror("Erro", "As informações estão erradas")


tk.Label(janela,
         text="Tela de login tema dark sem custom tkinter",
         bg="#2e2e2e",
         fg="white").pack(pady=10)

tk.Label(janela,
         text="Digite seu username",
         bg="#2e2e2e",
         fg="white").pack(pady=10)

#a entrada do username
entrada_username = tk.Entry(janela,
                         bg="#1e1e1e",
                         fg="white")

entrada_username.pack(pady=5)

# a entrada da senha
tk.Label(janela,
         text="agora digite sua senha",
         bg="#2e2e2e",
         fg="white").pack(pady=10)


entrada_senha = tk.Entry(janela,
                         bg="#1e1e1e",
                         fg="white",
                         show="*")

entrada_senha.pack(pady=5)
bt_validar = tk.Button(janela,
                       text="Login",
                       bg="#444444",
                       fg="white",
                       command=registro).pack(pady=5)















janela.mainloop()
