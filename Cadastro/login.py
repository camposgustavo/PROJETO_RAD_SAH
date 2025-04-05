import tkinter as tk
from tkinter import messagebox, ttk
from db_connection import DatabaseConnection

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Hotel - Login")
        self.root.geometry("300x200")
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
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(main_frame, text="Usuário:").grid(row=0, column=0, sticky=tk.W)
        self.username_entry = ttk.Entry(main_frame)
        self.username_entry.grid(row=0, column=1)

        ttk.Label(main_frame, text="Senha:").grid(row=1, column=0, sticky=tk.W)
        self.password_entry = ttk.Entry(main_frame, show="•")
        self.password_entry.grid(row=1, column=1)

        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, columnspan=2, pady=15)

        ttk.Button(button_frame, text="Login", command=self.authenticate).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Sair", command=self.root.quit).pack(side=tk.RIGHT, padx=5)

        self.root.bind('<Return>', lambda event: self.authenticate())
        self.username_entry.focus_set()

    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning("Campos Vazios", "Preencha todos os campos!")
            return

        try:
            db = DatabaseConnection()
            cursor = db.connection.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE username = %s AND password = %s", (username, password))
            if cursor.fetchone():
                messagebox.showinfo("Sucesso", "Login bem-sucedido!")
                self.root.destroy()
                import cadastro_interface  # Abre a tela de cadastro
            else:
                messagebox.showerror("Erro", "Credenciais inválidas!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()