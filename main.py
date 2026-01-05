from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from fpdf import FPDF
import os

# Arka planı beyaz yapar
Window.clearcolor = (1, 1, 1, 1)

class FaturaUygulamasi(App):
    def build(self):
        self.title = "Fatura Hesaplayıcı"
        
        root = ScrollView(size_hint=(1, 1))
        layout = BoxLayout(orientation='vertical', padding=50, spacing=30, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        # Başlık
        layout.add_widget(Label(
            text="HESAPLAMA PANELİ", 
            font_size=42, 
            bold=True, 
            color=(1, 0, 0, 1),
            size_hint_y=None, 
            height=100
        ))

        self.inputs = {}
        self.sonuc_etiketleri = {}
        faturalar = ["Elektrik", "Dogal Gaz", "Su", "Internet"]
        
        for fatura in faturalar:
            fatura_box = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None, height=180)
            
            label = Label(
                text=f"{fatura} Toplamı:", 
                font_size=28, 
                bold=True,
                color=(0, 0, 0, 1)
            )
            
            ent = TextInput(
                text="", 
                multiline=False, 
                input_filter='float', 
                font_size=36, 
                size_hint
