#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 10:14:45 2020

@author: Miguel Alvararenga Rocha
"""

import pygame
import time

def main():
    #As definicoes dos objetos(variaveis)
    pygame.init()
    tela = pygame.display.set_mode([600, 450])
    pygame.display.set_caption("Zig Zag the Blocks!")
    relogio = pygame.time.Clock()
    cor_branca = (255,255,255)
    cor_azul = (108, 194, 236)
    cor_verde = (152, 231, 114)
    cor_vermelha = (227, 57, 9)
    cor_rosa = (242, 107, 152)
    cor_preta = (0, 0, 0)
    sup = pygame.Surface((600, 450))
    sup.fill(cor_preta)

    ret_die = pygame.Rect(570, 180, 55, 80)
    ret_win = pygame.Rect(0, 400, 1000, 1000)
    ret = pygame.Rect(10, 10, 30, 30)
    ret2 = pygame.Rect(10, 35, 555, 6)
    ret3 = pygame.Rect(10, 85, 350, 6)
    ret4 = pygame.Rect(395, 85, 355, 6)
    ret5 = pygame.Rect(10, 130, 555, 6)
    ret6 = pygame.Rect(395, 90, 350, 6)
    ret7 = pygame.Rect(40, 175, 555, 6)
    ret8 = pygame.Rect(10, 215, 350, 6)
    ret9 = pygame.Rect(10, 310, 350, 6)
    ret10 = pygame.Rect(50, 260, 555, 6)
    ret11 = pygame.Rect(395, 310, 555, 6)    
    
    inter = True
    sair = False
    
    pygame.font.init()
    
    font_padrao = pygame.font.get_default_font()
    font_perdeu = pygame.font.SysFont(font_padrao, 45)
    font_ganhou = pygame.font.SysFont(font_padrao, 30)
    
    audio_explosao = pygame.mixer.Sound('explosao.ogg')
    
    
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_pos(20, 20)
                ret2.top = 600
                main()
                
                
                
                
        relogio.tick(150)
        tela.fill(cor_branca)
        tela.blit(sup, [0,0])
        
        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width/2
        ret.top -= ret.height/2
        if ret.colliderect(ret2) or ret.colliderect(ret3) or ret.colliderect(ret4) or ret.colliderect(ret5) or ret.colliderect(ret6) or ret.colliderect(ret7) or ret.colliderect(ret8) or ret.colliderect(ret9) or ret.colliderect(ret10) or ret.colliderect(ret11):
            #text = font_perdeu.render('PERDEU', 1, (255, 0, 0))
            pygame.mouse.set_pos(20, 20)
            #tela.blit(text, (200, 200))
            audio_explosao.set_volume(0.50)
            (ret.left, ret.top) = (xant, yant)
            
        if ret.colliderect(ret_die):
            pygame.mouse.set_pos(20, 20)
            
        if ret.top > 400:
            text = font_perdeu.render('GANHOU!', 1, (255, 0, 0))
            tela.blit(text, (200, 200))
            text = font_perdeu.render('CLIQUE PARA RECOMEÇAR', 1, (255, 0, 0))
            tela.blit(text, (100, 250))
            ret2.left = 602
            ret3.left = 602
            ret4.left = 602
            ret5.left = 602
            ret6.left = 602
            ret7.left = 602
            ret8.left = 602
            ret9.left = 602
            ret10.left = 602
            ret11.left = 602
            ret_die.left = 602


        pygame.draw.rect(tela, cor_vermelha, ret_die)
        pygame.draw.rect(tela, cor_verde, ret_win)
        pygame.draw.rect(tela, cor_vermelha, ret)
        pygame.draw.rect(tela, cor_branca, ret2)
        pygame.draw.rect(tela, cor_branca, ret3)
        pygame.draw.rect(tela, cor_branca, ret4)
        pygame.draw.rect(tela, cor_branca, ret5)
        #pygame.draw.rect(tela, cor_branca, ret6)
        pygame.draw.rect(tela, cor_branca, ret7)
        pygame.draw.rect(tela, cor_branca, ret8)
        pygame.draw.rect(tela, cor_branca, ret9)
        pygame.draw.rect(tela, cor_branca, ret10)
        pygame.draw.rect(tela, cor_branca, ret11)


        pygame.display.update()
    pygame.quit()
    

main()
