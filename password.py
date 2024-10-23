import random
import tkinter as tk
from tkinter import messagebox

def gerar_senha():
    # Obtenção das opções selecionadas
    include_lower = var_lower.get()
    include_upper = var_upper.get()
    include_digits = var_digits.get()
    include_symbols = var_symbols.get()

    # Definindo os grupos de caracteres com base nas escolhas
    letters_lower = "abcdefghijklmnopqrstuvwxyz" if include_lower else ""
    letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if include_upper else ""
    digits = "0123456789" if include_digits else ""
    symbols = "!@#$%^&*?" if include_symbols else ""

    # Combina todos os caracteres para o restante da senha
    all_characters = letters_lower + letters_upper + digits + symbols

    # Verifica se há pelo menos um tipo de caractere selecionado
    if not all_characters:
        messagebox.showwarning("Atenção", "Você deve incluir pelo menos um tipo de caractere.")
        return

    # Obtém o comprimento da senha
    try:
        password_length = int(entry_length.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido para a quantidade de caracteres.")
        return

    # Garantir ao menos um de cada tipo
    password = []
    if include_lower:
        password.append(random.choice(letters_lower))
    if include_upper:
        password.append(random.choice(letters_upper))
    if include_digits:
        password.append(random.choice(digits))
    if include_symbols:
        password.append(random.choice(symbols))

    # Preencher o restante da senha com caracteres aleatórios
    remaining_length = password_length - len(password)

    if remaining_length > 0:
        password += [random.choice(all_characters) for _ in range(remaining_length)]

    # Embaralhar para evitar um padrão previsível
    random.shuffle(password)

    # Unir a lista em uma string
    global senha_gerada
    senha_gerada = ''.join(password)

    # Exibir a senha gerada
    label_result.config(text=f"Sua senha foi gerada com sucesso: {senha_gerada}")

def copiar_senha():
    # Copiar a senha para a área de transferência
    root.clipboard_clear() # Limpar a área de transferência
    root.clipboard_append(senha_gerada) # Copiar a senha gerada
    messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")

# Criar a janela principal
root = tk.Tk()
root.title("Gerador de Senhas")
root.geometry('400x400')
root.configure(background="#808080")

# Variáveis para as opções
var_lower = tk.BooleanVar()
var_upper = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_symbols = tk.BooleanVar()

# Layout
tk.Checkbutton(root, text="Incluir letras minúsculas", variable=var_lower, bg="#808080").pack()
tk.Checkbutton(root, text="Incluir letras maiúsculas", variable=var_upper, bg="#808080").pack()
tk.Checkbutton(root, text="Incluir números", variable=var_digits, bg="#808080").pack()
tk.Checkbutton(root, text="Incluir símbolos", variable=var_symbols, bg="#808080").pack()

tk.Label(root, text="Quantidade de Caracteres:", bg="#808080", fg="black").pack()
entry_length = tk.Entry(root)
entry_length.pack()

tk.Button(root, text="Gerar Senha", command=gerar_senha, bg="#505050", fg="white").pack()

label_result = tk.Label(root, text="", bg="#808080", fg="white")
label_result.pack()

# Botão para copiar a senha
tk.Button(root, text="Copiar Senha", command=copiar_senha, bg="#505050", fg="white").pack()

# Iniciar o loop da interface gráfica
root.mainloop()
