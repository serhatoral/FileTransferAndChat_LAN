import dinleyici
import yonetici
import socket
from rich.console import Console
import art
class FileTransfer:

    consol = Console()

    def alt_menu_names(self):
        self.consol.print("""    
    [bold green][1] [/] [red] Yönetici ol....    
    [bold green][2] [/] [red] Dinleyici ol....
        
        """)



    def start(self):
        self.alt_menu_names()
        secim = self.consol.input("[yellow]Seçmek istediğiniz işlem numarasını giriniz: ")

        Art = art.text2art("FileTransfer")
        self.consol.print(Art, style="bold dark_turquoise")
        if secim == "1":
            ip = socket.gethostbyname(socket.gethostname())
            port =  int(self.consol.input("[bold green] Başlatılmak istenen port numarasını girin: [/]"))
            yonet=yonetici.Yonetici(ip,port)
            yonet.start()        
        elif secim == "2":
            ip = self.consol.input("[bold green]Bağlantı kurulacak ip adresi: [/]")
            port =  int(self.consol.input("[bold green]Bağlantı kurulacak port numarası: [/]"))
            dinle = dinleyici.Dinleyici(ip,port)
            dinle.start()
            
        else:
            self.consol.print("Lütfen geçerli bir seçim yapın!",style="red")

