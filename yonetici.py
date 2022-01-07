# -*- coding: utf-8 -*-

import ft_fonksiyonlar
import help
import socket
from rich.console import Console

class Yonetici:
    consol = Console()

    def __init__(self, ip, port) :
        listener= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        listener.bind((ip, port))

        listener.listen(0)
        print("Listening")
        (self.connection,address) = listener.accept()
        self.fonk = ft_fonksiyonlar.fonksiyonlar(self.connection)
        print("Connection OK")

    def start(self):
        
        while True:
            try:
                user_input = self.consol.input("[yellow]Enter command:") 

                if user_input=="help":
                    help.Help.help_write()
                    continue
                
                if user_input.startswith("upload "):
                    user_input = user_input.split(" ",1)
                    self.fonk.zipped(user_input)
                
                user_input = self.fonk.check_command(user_input)

                
                if isinstance(user_input,list):
                    if user_input[0] == "download":
                        boyut = self.fonk.command_run(["boyut",user_input[1]])
                        output = self.fonk.run_for_download(user_input,boyut)
                    elif user_input[0] == "upload":
                        output = self.fonk.run_for_upload(user_input)
                    else:
                        output = self.fonk.command_run(user_input)
                else:
                    output = self.fonk.command_run(user_input)
                
                      
                if output=="quit":
                    break
                                  
                if user_input[0] == "download":                        
                    if isinstance(output,list):                      
                        output = self.fonk.save_file(output[1],output[0])
                    else:
                        output = self.fonk.save_file(user_input[1],output)                   
            except Exception:
                output = "Error! Try again."
                
            if output.startswith("Error"):
                self.consol.print(output,style="red")
            else:
                self.consol.print(output,style="green") 
