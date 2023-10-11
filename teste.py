import pygame

# Inicialize o Pygame
pygame.init()

# Configurações da primeira janela
window1 = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Janela 1")

# Variável para controlar a exibição da segunda janela
show_second_window = False

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Botão esquerdo do mouse
            if not show_second_window:
                show_second_window = True

    # Desenhe coisas na primeira janela
    window1.fill((255, 0, 0))  # Preencha a primeira janela com vermelho

    if show_second_window:
        # Configurações da segunda janela (simulada)
        window2 = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Janela 2")
        window2.fill((0, 0, 255))  # Preencha a segunda janela com azul

    pygame.display.flip()

# Encerre o Pygame
pygame.quit()
