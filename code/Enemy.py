#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

# classe para definir o comportamento do Enemy3
class Enemy3(Enemy):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.vertical_speed = ENTITY_SPEED['Enemy3']  
        self.direction = 1 

    def move(self):
        self.rect.centerx -= ENTITY_SPEED['Enemy3'] 
        self.rect.centery += self.vertical_speed * self.direction  

        # Verifica colisões com as bordas da tela
        if self.rect.bottom >= WIN_HEIGHT:  
            self.direction = -1 
        elif self.rect.top <= 0:  
            self.direction = 1 
            self.vertical_speed *= 2  
        else:
            self.vertical_speed = ENTITY_SPEED['Enemy3']  