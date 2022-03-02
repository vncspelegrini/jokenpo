from kivy.app import App 
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from random import randint
from kivy.clock import Clock

class Principal(BoxLayout):
    propriedade = StringProperty('VS')
    gaplacar = StringProperty('0')
    roplacar = StringProperty('0')
    placar_gato = 0
    placar_robo = 0
   
    def mudar(self, r):
        self.ids.eu.source = 'jokenpog.gif'
        self.ids.com.source = 'jokenpoc.gif'
        Clock.schedule_once(self.responder, 3)
        self.eu = r
       
    def principal(self, eu, placar_gato, placar_robo):
           
        com = randint(1, 3)
        resp = str()        
            
        if com == eu :
            if eu == 1:
                self.ids.eu.source = 'pedrad.png'
                self.ids.com.source = 'pedrae.png'
                Clock.schedule_once(self.empate, 3)
            elif eu == 2:
                self.ids.eu.source = 'papeld.png'
                self.ids.com.source = 'papele.png'
                Clock.schedule_once(self.empate, 3)
            else:
                self.ids.eu.source = 'tesourad.png'
                self.ids.com.source = 'tesourae.png'
                Clock.schedule_once(self.empate, 3)
        elif com == 1:
            if eu == 2:
                placar_gato += 1
                self.ids.pgato = placar_gato   
                self.ids.eu.source = 'papeld.png'
                self.ids.com.source = 'pedrae.png'
                Clock.schedule_once(self.gato, 3)
            else:
                placar_robo += 1
                self.ids.probo = placar_robo
                self.ids.eu.source = 'tesourad.png'
                self.ids.com.source = 'pedrae.png'
                Clock.schedule_once(self.robo, 3)
        elif com == 2:
            if eu == 3:
                placar_gato += 1
                self.ids.gato = placar_gato
                self.ids.eu.source = 'tesourad.png'
                self.ids.com.source = 'papele.png'
                Clock.schedule_once(self.gato, 3)
            else:
                placar_robo += 1
                self.ids.robo = placar_robo
                self.ids.eu.source = 'pedrad.png'
                self.ids.com.source = 'papele.png'
                Clock.schedule_once(self.robo, 3)
        else:
            if eu == 1:
                placar_gato += 1
                self.ids.gato = placar_gato
                self.ids.eu.source = 'pedrad.png'
                self.ids.com.source = 'tesourae.png'
                Clock.schedule_once(self.gato, 3)
            else:
                placar_robo += 1
                self.ids.robo = placar_robo 
                self.ids.eu.source = 'papeld.png'
                self.ids.com.source = 'tesourae.png'
                Clock.schedule_once(self.robo, 3)
               
        self.propriedade = resp
        self.roplacar = str(placar_robo)
        self.gaplacar = str(placar_gato)
    
    def responder(self, eu):
        eu = eu
        self.ids.eu.source = 'inicioc.png'
        self.ids.com.source = 'inicioc.png'
        self.principal(self.eu, placar_gato = int(self.gaplacar), placar_robo = int(self.roplacar))
    
      
    def gato (self, *args):
        self.ids.eu.source = 'ganheig.png'
        self.ids.com.source = 'perdic.png'
        Clock.schedule_once(self.fim, 3)
    
    def robo (self, *args):
        self.ids.eu.source = 'perdig.png'
        self.ids.com.source = 'ganheic.png'
        Clock.schedule_once(self.fim, 3)
    
    def empate (self, *args):
        self.ids.eu.source = 'empateg.png'
        self.ids.com.source = 'empatec.png'
        Clock.schedule_once(self.fim, 3)
    
    
    def fim (self, *args):
        self.ids.eu.source = 'iniciog.png'
        self.ids.com.source = 'inicioc.png'
                       
class MainApp(App):
    def build(self):
        
        return Principal()
    
MainApp().run()