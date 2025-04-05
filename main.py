from Cadastro.login import LoginApp
import tkinter as tk

def main():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()