import pygame
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # Importar as bibliotecas necessárias

# Inicialize o pygame
pygame.init()

# Inicialize o mixer do pygame
pygame.mixer.init()

# Função para tocar música com um volume específico
def play_music_with_volume(file_path, volume):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()

# Função para parar a reprodução da música
def stop_music():
    pygame.mixer.music.stop()

# Função para escolher um arquivo de música
def choose_music():
    file_path = filedialog.askopenfilename(filetypes=[("Arquivos MP3", "*.mp3")])
    if file_path:
        play_music_with_volume(file_path, volume_slider.get())

# Função para ajustar o volume
def set_volume(value):
    volume = float(value) / 100.0  # Converter para valor entre 0.0 e 1.0
    pygame.mixer.music.set_volume(volume)

# Crie uma janela Tkinter
root = tk.Tk()
root.title("Player de Música com Controle de Volume")

# Defina o fundo preto da janela principal
root.configure(bg="black")

# Carregue a imagem que você deseja exibir no centro da janela
image = Image.open("icons8-music-128.png")  # Substitua pelo caminho da sua imagem
photo = ImageTk.PhotoImage(image)

# Crie um Label para exibir a imagem
image_label = tk.Label(root, image=photo, bg="black")
image_label.grid(row=1, column=1, padx=10, pady=10)

# Botão para escolher uma música com texto branco
choose_button = tk.Button(root, text="Escolher Música", command=choose_music, bg="black", fg="white", bd=2, highlightbackground="dark gray")
choose_button.grid(row=0, column=6, padx=5, pady=5)

# Controle deslizante de volume (vertical e à esquerda) sem borda
volume_slider = tk.Scale(root, from_=100, to=0, orient="vertical", label="Volume",
                         command=lambda value: set_volume(value), bg="black", fg="white", highlightbackground="dark gray", bd=0)
volume_slider.set(50)  # Valor inicial do volume
volume_slider.grid(row=0, column=0, rowspan=5, padx=10, pady=10)

# Botão para tocar música com emoji de Play
play_button = tk.Button(root, text="▶️ Tocar Música", command=lambda: play_music_with_volume(file_path, volume_slider.get()), bg="black", fg="white", bd=2, highlightbackground="dark gray")
play_button.grid(row=1, column=6, padx=5, pady=5)

# Botão para parar música com emoji de Pause
pause_button = tk.Button(root, text="⏸️ Parar Música", command=stop_music, bg="black", fg="white", bd=2, highlightbackground="dark gray")
pause_button.grid(row=2, column=6, padx=5, pady=5)

# Função para encerrar o aplicativo
def quit_app():
    pygame.quit()
    root.destroy()

# Botão para sair com texto branco
quit_button = tk.Button(root, text="Sair", command=quit_app, bg="black", fg="white", bd=2, highlightbackground="dark gray")
quit_button.grid(row=3, column=0, padx=10, pady=10)

root.mainloop()
