from player import *
from constantes import *
from auxiliar import Auxiliar
from class_impact import Impact
import math

class Bullet():
    
    def __init__(self,owner,x_init,y_init,x_end,y_end,speed,path,frame_rate_ms,move_rate_ms,width=5,height=5) -> None:
        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_animation = 0
        self.image = pygame.image.load(path)#.convert()
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.x = x_init
        self.y = y_init
        self.owner = owner
        self.rect.x = x_init
        self.rect.y = y_init
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms
        angle = math.atan2(y_end - y_init, x_end - x_init) #Obtengo el angulo en radianes
        print('El angulo engrados es:', int(angle*180/math.pi))

        self.move_x = math.cos(angle)*speed
        self.move_y = math.sin(angle)*speed
        
        self.is_active = True
        self.list_efect = []
   
    def change_x(self,delta_x):
        self.x = self.x + delta_x
        self.rect.x = int(self.x)   

    def change_y(self,delta_y):
        self.y = self.y + delta_y
        self.rect.y = int(self.y)

    def do_movement(self,delta_ms,plataform_list,enemy_list,player, boss = None):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            self.change_x(self.move_x)
            self.change_y(self.move_y)
            self.check_impact(plataform_list,enemy_list,player, boss)

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            pass
    
    def check_impact(self,plataform_list,enemy_list,player, boss = None):
        number_aux = 50
        if(self.is_active and self.owner != player and self.rect.colliderect(player.rect)):
            print("IMPACTO PLAYER")
            player.receive_shoot()
            if player.direction == DIRECTION_L:
                number_aux *= -1
            self.list_efect.append(Impact(self.rect.x, self.rect.y - 40, 'blood', p_scale=1.5))
            self.is_active = False
        
        for plataform in plataform_list:       
            if(self.rect.colliderect(plataform.rect)):
                 print("IMPACTO PLATAFORMA")
                 self.is_active = False
            else:
                for aux_enemy in enemy_list:
                    if(self.is_active and self.owner != aux_enemy and self.rect.colliderect(aux_enemy.rect)):
                        print("IMPACTO ENEMIGO")
                        self.is_active = False
                        aux_enemy.receive_shoot()#enemy_list.index(aux_enemy))
                        self.list_efect.append(Impact(aux_enemy.rect.x, aux_enemy.rect.y - 40, 'blood', p_scale=1.5))
                        #enemy_list.pop(enemy_list.index(aux_enemy))
        if boss != None:
            if(self.is_active and self.owner != boss and self.rect.colliderect(boss.rect)):
                print("IMPACTO AL BOSS")
                self.is_active = False
                self.list_efect.append(Impact(boss.rect.x, boss.rect.y - 40, 'blood', p_scale=1.5))
                boss.receive_shoot()               
                        

    def update(self,delta_ms,plataform_list,enemy_list,player, boss = None):
        self.do_movement(delta_ms,plataform_list,enemy_list,player, boss)        
        self.do_animation(delta_ms)
        for efect in self.list_efect:
            efect.update(delta_ms)
        for efect in self.list_efect:
            if efect.end_animation:
                self.list_efect.pop(self.list_efect.index(efect))             


    def draw(self,screen):
        
        if(self.is_active):
            if(DEBUG):
                pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            screen.blit(self.image,self.rect)
        for efect in self.list_efect:
            efect.draw(screen)
