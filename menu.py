import arts
import MacCheck
import FileTransfer
import client
import os

from rich.console import Console

class Menu:
    consol = Console()
    cl= client.Client()
    
    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  
            command = 'cls'
        os.system(command)

    def main_menu_names(self):
        self.consol.print("""    
    [bold green][1] [/] [red] Ağ Tarama Modülünü Başlat....
    [bold green][2] [/] [red] Mesaj Modülünü Başlat....
    [bold green][3] [/] [red] Dosya Transfer Modülünü Başlat....
    [bold green][9] [/] [red] Ekranı Temizle....
    [bold green][0] [/] [red] Programı kapat....
        
        """)
    def macCheck_menu_names(self):
        self.consol.print("""    
    [bold green][1] [/] [red] İşlemi Tekrarla....    
    [bold green][0] [/] [red] Bir Önceki Menüye Dön....
        
        """)

    

    def start_menu(self):   
        
        while True:
            self.clearConsole()
            arts.AsciiArt().random_art()
            self.main_menu_names()
            secim = self.consol.input("[green]Seçmek istediğiniz işlem numarasını giriniz: ")
            
            if secim =="1":
                self.clearConsole()
                MacCheck.MacCheck().print_arp_table()
                
                kontrol = True
                while kontrol==True:
                    self.macCheck_menu_names()
                    secim2 = self.consol.input("[yellow]Seçmek istediğiniz işlem numarasını giriniz: ")
                    if secim2 == "0":
                        kontrol=False
                    if secim2 == "1":
                        self.clearConsole()
                        MacCheck.MacCheck().print_arp_table()
                    
                        
            if secim=="2":               
                self.clearConsole()
                self.cl.start()

            if secim == "3":
                self.clearConsole()
                FileTransfer.FileTransfer().start()
                                
            if secim =="9":
                self.clearConsole()
            if secim == "0":
                exit()  
            self.clearConsole()    

a =Menu()
a.start_menu()

