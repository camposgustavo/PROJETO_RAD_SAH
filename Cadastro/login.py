import tkinter as tk
from tkinter import messagebox, ttk

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Hotel - Login")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        
        # Configurar estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.create_widgets()
        self.center_window()

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'+{x}+{y}')

    def create_widgets(self):
        # Container principal
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Labels
        ttk.Label(main_frame, text="Usuário:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Label(main_frame, text="Senha:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        # Entradas
        self.username_entry = ttk.Entry(main_frame)
        self.password_entry = ttk.Entry(main_frame, show="•")
        
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botões
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=15)

        ttk.Button(
            button_frame,
            text="Login",
            command=self.authenticate,
            width=10
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            button_frame,
            text="Sair",
            command=self.root.quit,
            width=10
        ).pack(side=tk.RIGHT, padx=5)

        # Configurar foco e bindings
        self.root.bind('<Return>', lambda event: self.authenticate())
        self.username_entry.focus_set()

    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning(
                "Campos Vazios",
                "Por favor, preencha todos os campos!"
            )
            return

        # Validação de exemplo (substituir por lógica real)
        if username == {username} and password == {password}:
            messagebox.showinfo(
                "Login Bem-sucedido",
                f"Bem-vindo, {username}!\nAcessando o sistema..."
            )
            self.root.destroy()
            # Aqui você chamaria a próxima tela do sistema
        else:
            messagebox.showerror(
                "Falha na Autenticação",
                "Credenciais inválidas!\nTente novamente."
            )
            self.password_entry.delete(0, tk.END)
            self.username_entry.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()