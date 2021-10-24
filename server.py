import socket
import sys
import threading
from rich.console import Console
import art


class Server:

    consol= Console()
    clients = []
    nicknames = []

    PORT = int(consol.input("[bold green]Sunucu başlatmak istediğiniz port numarasını girin: [/]"))
    SERVER = socket.gethostbyname(socket.gethostname())  # host isminden local ip'yi getirir.
    ADDR = (SERVER, PORT)
    FORMAT = 'utf-8'


    server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)   
    server.bind(ADDR) 

    def broadcast(self,message, clnt):
        
        for client in self.clients:
            if client != clnt:
                client.send(message)


    def handle_client(self,connection):
        
        while True:
            try:              
                message = str(connection.recv(1024).decode(self.FORMAT)) # client dan mesaj alıyoruz 
                if message.endswith("; çıkış"):
                   sys.exit()
                   
                else:           
                    message= message.encode(self.FORMAT)                                         
                    self.broadcast(message,connection)             
                                            
            except: 
                
                index = self.clients.index(connection)
                self.clients.remove(connection)
                connection.close()

                nickname = self.nicknames[index]
                self.consol.print(f"{nickname} odadan ayrıldı!",style="red") # sunucuda mesajı yazdırıyoruz
                self.broadcast(f'{nickname} odadan ayrıldı.'.encode(self.FORMAT),connection) # sunucuya bağlı tüm istemcilerde mesajı yayınlıyoruz.
                self.nicknames.remove(nickname)
                break



    def start(self):
        print("\n")
        Art = art.text2art("ChatRoom-Server")
        self.consol.print(Art, style="bold dark_turquoise")
        self.server.listen()
        self.consol.print("Sunucu dinleniyor...",style="red")
        while  True:
            connection, address = self.server.accept()
            print("\n")
            self.consol.print(f"{str(address)} ile bağlantı sağlandı.",style="cyan")

            connection.send('NICK?'.encode(self.FORMAT)) # Kullanıcıdan kullanıcı adını istiyoruz.
            nickname= connection.recv(1024).decode(self.FORMAT)  #Kullanıcının yolladığı veriyi alıyoruz.           
            self.nicknames.append(nickname)
            self.clients.append(connection)
            self.consol.print(f"{str(address)}\'nin kullanıcı adı {nickname}\'dir.",style="cyan")               
            connection.send('Sunucuya başarılı bir şekilde bağlandınız.'.encode(self.FORMAT))
            self.broadcast(f'{nickname} odaya katıldı.'.encode(self.FORMAT),connection) 
            

            thread = threading.Thread(target=self.handle_client, args=(connection,))
            thread.start()


a= Server()
print("Sunucu başlatılıyor...")
a.start() 


