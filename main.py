import pygame
import random

pygame.init()

#cores

branco = 0, 0, 0
preto = 255, 255, 255
verde = 66, 201, 32
verde_brilhante = 0, 255, 0

#configs tela
lar_x = 720
com_y = 900
tela = pygame.display.set_mode((lar_x, com_y))
titulo = pygame.display.set_caption('Teste seus Reflexos!')
bg = pygame.image.load('sprites/bg.png')

#fps
fps = pygame.time.Clock()

#player
player_x = 335
player_y = 820
player_velocidade = 40
player_image = pygame.image.load('sprites/player.png')

#inimigo eixo x = 50 / eixo y = 60
inimigo_x = 0 #posição x
inimigo_y = 0 #posição y
inimigo_velocidade = 20
inimigo_imagem = pygame.image.load('sprites/inimigo.png')

#inimigo 2
inimigo2_x = 0
inimigo2_y = 0
inimigo2_velocidade = 20
inimigo2_imagem = pygame.image.load('sprites/inimigo.png')


#pontos
pontos = 0


#funções
#desenhar na tela
def desenhar():
    #fonte
    pygame.font.init() 
    #fps
    font = pygame.font.get_default_font()
    font_size = pygame.font.SysFont(font, 20, 1, 0) 
    fps_text = '{}'.format(int(fps.get_fps()))
    fps_text_render = font_size.render(fps_text, False, branco)

    #pontuação
    pontos_text = 'Score:  {}'.format(pontos)
    pontos_size = pygame.font.SysFont(font, 60, 1, 0) 
    pontos_text_render = pontos_size.render(pontos_text, True, verde_brilhante)

    tela.blit(bg,(0, 0))
    tela.blit(player_image, (player_x, player_y))
    tela.blit(inimigo_imagem, (inimigo_x, inimigo_y))
    tela.blit(inimigo2_imagem, (inimigo2_x, inimigo2_y))
    tela.blit(fps_text_render, (705,0))
    tela.blit(pontos_text_render, (0,0))

#movimento
def movimento_inimigo():
    #movimento do PRIMERIO inimigo
    global inimigo_y
    global inimigo_x
    
    inimigo_y += inimigo_velocidade

    if inimigo_y > 910:
        inimigo_y = -20
        inimigo_x = random.randrange(0, 670) 

    #movimento do SEGUNDO inimigo
    global inimigo2_y
    global inimigo2_x

    inimigo2_y += inimigo2_velocidade

    if inimigo2_y > 910:
        inimigo2_y = -20
        inimigo2_x = random.randrange(0, 670)

#colisão
def colision():
    global pontos
    global inimigo_y
    global inimigo2_y

    if inimigo_y > 770 and player_x + 50 > inimigo_x > player_x - 50:
        pontos -= 50
        inimigo_y = -20

    elif inimigo2_y > 770 and player_x + 50 > inimigo2_x > player_x - 50:    
        pontos -= 50
        inimigo2_y = -20
        



while 1:
    fps.tick(60)
    for event in pygame.event.get():
        #print(event)
        
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player_x -= player_velocidade
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player_x += player_velocidade







    if inimigo_x < player_x:
        inimigo_x += 2
    elif inimigo_x > player_x:
        inimigo_x -= 2
    
    if inimigo2_x < player_x:
        inimigo2_x += 2
    elif inimigo2_x > player_x:
        inimigo2_x -= 2

    pontos += 1   

    desenhar()
    colision()
    movimento_inimigo()
    pygame.display.update()