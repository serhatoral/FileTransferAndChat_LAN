import socket
import sys
import threading
from rich.console import Console
import art


class Client:

    FORMAT = 'utf-8'   
    consol = Console()  
    nickname=""  
    client= None

    def connection(self):   
        SERVER = self.consol.input("[bold green]Sunucu IP adresi girin: [/]")
        PORT =  int(self.consol.input("[bold green]Sunucu port numarası girin: [/]"))
        
        ADDR = (SERVER , PORT)

        try:
            self.client = socket.socket(socket.AF_INET , socket.SOCK_STREAM) 
            self.client.connect(ADDR) 
        except:
            print("Sunucuya bağlanılamadı. Lütfen sunucunun açık olduğunu kontrol ediniz.") 
            



    def send(self):
        while True:        
            message = f"|{self.nickname}|=>:; {input()}"                     
            self.client.send(message.encode(self.FORMAT))
            if message.endswith("; çıkış"):                 
                sys.exit()


    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode(self.FORMAT)
                if message == 'NICK?':  # Sunucuya kullanıcı adımızı yolluyoruz.
                    self.client.send(self.nickname.encode(self.FORMAT))
                else:
                    if message =="Sunucuya başarılı bir şekilde bağlandınız." or +\
                    message.endswith("katıldı.") or message.endswith("ayrıldı."):
                        
                        self.consol.print(message,style="cyan")                    
                    else:
                        liste = message.split(":; ",)                        
                        message = f"[magenta]{liste[0]}[/] [yellow]{liste[1]}[/]"
                        print("\n")
                        self.consol.print(message)


            except:
                print("Bağlantı sonlandırıldı")
                self.client.close()
                break

    def start(self):
        self.nickname = self.consol.input("[bold green]Bir kullanıcı adı girin: [/]")        
        self.connection()
        Art = art.text2art("ChatRoom-Client")
        self.consol.print(Art, style="bold dark_turquoise")
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        send_thread = threading.Thread(target=self.send)
        send_thread.start()

        receive_thread.join()  #join fonksiyonları threadler sonlanana kadar 
        send_thread.join()     # menu.py'deki  işlemleri bekletir. 
        
