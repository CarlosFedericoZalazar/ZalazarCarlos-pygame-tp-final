import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_label import Label
from gui_progressbar import ProgressBar
from background import Background
from class_file import File



class FormMenuA(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background, color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        
        #self.boton1 = Button(master=self,x=600,y=600,w=140,h=50,color_background=None,color_border=None,image_background="images\gui\Gui\Button_M_02.png",on_click=self.on_click_boton1,on_click_param="",text="SUMA +",font="Verdana",font_size=30,font_color=C_WHITE)
        #self.boton2 = Button(master=self,x=20,y=80,w=140,h=50,color_background=None,color_border=None,image_background="images\gui\Gui\Button_M_02.png",on_click=self.on_click_boton2,on_click_param="",text="RESTA -",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton3 = Button(master=self,x=450,y=450,w=160,h=100,color_background=None,color_border=None,image_background="images\gui\Gui\Buttom_play.png",on_click=self.on_click_boton3,on_click_param="form_game_L1",text="",font="Verdana",font_size=30,font_color=C_WHITE)
        #self.boton4 = Button(master=self,x=20,y=200,w=140,h=50,color_background=None,color_border=None,image_background="images\gui\Gui\Button_M_02.png",on_click=self.on_click_boton3,on_click_param="form_menu_B",text="SQL",font="Verdana",font_size=30,font_color=C_WHITE)
        #self.boton5 = Button(master=self,x=20,y=240,w=140,h=50,color_background=None,color_border=None,image_background="images\gui\Gui\Button_M_02.png",on_click=self.on_click_boton3,on_click_param="form_menu_C",text="Vector",font="Verdana",font_size=30,font_color=C_WHITE)
        self.Label_textBox = Label(master = self, x=640, y=400, w=350, h=100,color_border=None, text=f"Name Player", font="Comic Sans MS", font_size=25, font_color=C_WHITE, image_background=None)                     
        self.txt1 = TextBox(master=self,x=640,y=450,w=350,h=100,color_background=None,color_border=None,image_background="images\gui\Gui\\text_box.png",text='',font="Verdana",font_size=30,font_color=C_WHITE)
        #self.pb1 = ProgressBar(master=self,x=200,y=150,w=240,h=50,color_background=None,color_border=None,image_background="images\gui\Gui\Bar_Background01.png",image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",value = 3, value_max=8)
        
        self.lista_widget = [self.boton3,self.txt1]
        #self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4,self.boton5,self.txt1,self.pb1]
        # FONDO DE PANTALLA
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images\gui\Gui\portada_golden.png")
        self.file_game = File('data_game')

    def on_click_boton1(self, parametro):
        self.pb1.value += 1
 
    def on_click_boton2(self, parametro):
        self.pb1.value -= 1
    
    def on_click_boton3(self, parametro):
        self.file_game.new_reg_player(self.txt1._text.upper())
        #self.file_game.new_file()
        print(self.txt1._text)
        self.txt1._text = ''
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
        self.Label_textBox.update()

    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)
        self.Label_textBox.draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()
        