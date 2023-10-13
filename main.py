import pygame

# Inicialize o pygame
pygame.init()

# Função para tocar música
def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Função para parar a reprodução da música
def stop_music():
    pygame.mixer.music.stop()

# Lista de músicas
music_files = []

while True:
    print("Escolha uma música para tocar:")
    for i, music_file in enumerate(music_files):
        print(f"{i + 1}. Música {i + 1}")

    print(f"{len(music_files) + 1}. Parar música")
    print(f"{len(music_files) + 2}. Sair")

    choice = input("Escolha uma opção: ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(music_files):
            play_music(music_files[choice - 1])
        elif choice == len(music_files) + 1:
            stop_music()
        elif choice == len(music_files) + 2:
            pygame.quit()
            break
        else:
            print("Escolha inválida. Tente novamente.")
    else:
        print("Escolha inválida. Tente novamente.")
