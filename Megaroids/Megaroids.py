#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 19:21:28 2020

@author: Miguel Alvarenga
"""

import time
import pygame
import random

class Recs(object):
    def __init__(self, numeroinicial):
        self.lista = []
        for x in range(numeroinicial):
            leftrandom = random.randrange(2, 560)
            toprandom = random.randrange(-580, -10)
            width = random.randrange(10, 30)
            height = random.randrange(15, 30)
            self.lista.append(pygame.Rect(leftrandom, toprandom, width, height))
            
    def mover(self):
        for retangulo in self.lista:
            retangulo.move_ip(0, 3)
            
    def cor(self, superficie):
        for retangulo in self.lista:
            pygame.draw.rect(superficie, (165, 214, 254), retangulo)
            
    def recriar(self):
        for x in range(len(self.lista)):
            if self.lista[x].top > 481:
                leftrandom = random.randrange(2, 560)
                toprandom = random.randrange(-580, -10)
                width = random.randrange(10, 30)
                height = random.randrange(15, 30)
                self.lista[x] = (pygame.Rect(leftrandom, toprandom, width, height))
            

class Player(pygame.sprite.Sprite):
    def __init__(self, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.top, self.rect.left = (40, 40)
    
    def mover(self, vx, vy):
        self.rect.move_ip(vx, vy)
    
    def update(self, superficie):
        superficie.blit(self.imagem, self.rect)
    
def colisao(player, recs):
    for rec in recs.lista:
        if player.rect.colliderect(rec):
            return True
    return False
    
def main():
    import pygame
    #Delcaração de objetos(variáveis)
    pygame.init()
    tela = pygame.display.set_mode((480, 300))
    sair = False
    
    img_nave = pygame.image.load("nave.png")
    img_nave = pygame.transform.scale(img_nave, (40, 50))
    jogador = Player(img_nave)
    
    imagem_fundo = pygame.image.load("fundo.jpg")
    imagem_fundo = pygame.transform.scale(imagem_fundo, (480, 300))
    
    explosion = pygame.image.load("explosion.png")
    explosion = pygame.transform.scale(explosion, (40, 40))
    
    pygame.mixer.music.load("sonic-bootleg.mp3")
    pygame.mixer.music.play(3)
    
    som_explosao = pygame.mixer.Sound("explosao.ogg")
    
    cor_branca = (255, 255, 255)
    
    
    relogio = pygame.time.Clock()
    
    vx, vy = 0, 0
    velocidade = 10
    leftpress, rightpress, uppress, downpress = False, False, False, False
    
    texto = pygame.font.SysFont("Arial", 20, True, False)

    
    
    
    ret = Recs(30)
    colidiu = False
    
    
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            
            if colidiu == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        leftpress = True
                        vx = - velocidade
                    
                    if event.key == pygame.K_RIGHT:
                        rightpress = True
                        vx = velocidade
                        
                    if event.key == pygame.K_UP:
                        uppress = True
                        vy = - velocidade
                    
                    if event.key == pygame.K_DOWN:
                        downpress = True
                        vy = velocidade
                        
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftpress = False
                        vx = - 0
                    
                    if event.key == pygame.K_RIGHT:
                        rightpress = False
                        vx = 0
                        
                    if event.key == pygame.K_UP:
                        uppress = False
                        vy = - 0
                    
                    if event.key == pygame.K_DOWN:
                        downpress = False
                        vy = 0
        
        if colisao(jogador, ret):
            colidiu = True
            pygame.mixer.music.stop()
            som_explosao.play()
            time.sleep(2)
            pygame.quit()
            
        if colidiu == False:
            ret.mover()
            jogador.mover(vx, vy)
            tela.blit(imagem_fundo, (0, 0))
            segundos = pygame.time.get_ticks()/1000
            segundos = str(segundos)
            contador = texto.render("Pontuação: {}".format(segundos), 0, cor_branca)
            tela.blit(contador, (250, 10))
        
        relogio.tick(20)
        #tela.blit(imagem_fundo, (0, 0))
        ret.cor(tela)
        ret.recriar()   
        jogador.update(tela)
        
        
                
        pygame.display.update()
        
    pygame.quit()
        

main()
                    
                    