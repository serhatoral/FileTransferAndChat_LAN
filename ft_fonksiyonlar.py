import simplejson
import base64
import os
import shutil
from rich.console import Console
from rich.progress import Progress

class fonksiyonlar:

    def __init__(self,conn) :
        self.connection= conn
        self.consol = Console()

    def json_send(self, data):
            json_data = simplejson.dumps(data)
            self.connection.send(json_data.encode("utf-8"))


    def read_file_contents(self, path):
            with open(path, "rb") as file:
                return base64.b64encode(file.read())

    def save_file(self,path,content):        
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "download successful!"
    
    def save_file_for_upload(self,path,content):        
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return bytes("upload successful!","utf-8")

    def zipped(self,user_input):
        if os.path.isdir(user_input[1]):
            shutil.make_archive(user_input[1],"zip",user_input[1])
            user_input[1]= user_input[1]+".zip"
            user_input.append(self.read_file_contents(user_input[1]))
        else:
            user_input.append(self.read_file_contents(user_input[1]))

    def json_receive(self):
        json_data = ""
       
        while True:
            try:
                json_data += self.connection.recv(32767).decode()
                    
                return simplejson.loads(json_data)
            except ValueError:   #tum paketi okuyana kadar devem etmesi icin.
                continue     

    def command_run(self, input):
            self.json_send(input)
            
            if input == "quit":
                self.connection.close()
                return "quit"                                            
            return self.json_receive() 


    def check_command(self, comm):
        command_keys = ["cd ","download "]
        if isinstance(comm, list):
            return comm  
        else: 
            for key in command_keys :
                if comm.startswith(key):                    
                    comm = comm.split(" ", 1)
                    return comm        
            return comm

    def run_for_upload(self, input):
            
            with self.consol.status("[bold green]karşı Tarafa Yükleme Sürüyor...") as status:
                while True:
                    self.json_send(input)
                    
                    if input == "quit":
                        self.connection.close()
                        exit()                                            
                    return self.json_receive()

    def download_for_recieve(self,boyut):
        json_data = ""
        with Progress() as progress:
            task1 = progress.add_task("[red]Downloading...", total=int(boyut))
            comp=0           
            while True:
                try:
                    comp=comp+24600
                    json_data += self.connection.recv(32767).decode()
                    
                    progress.update(task1,completed=comp)
                    return simplejson.loads(json_data)
                except ValueError:   #tum paketi okuyana kadar devem etmesi icin.
                    continue        
    
    def run_for_download(self,input,boyut):
            self.json_send(input)
            
            if input == "quit":
                self.connection.close()
                exit()                                            
            return self.download_for_recieve(boyut)

    def execute_cd_command(self, directory):
        os.chdir(directory)
        return b"chance to directory!"

    def get_file_size(self,filename):
        file_size = os.path.getsize(filename)
        return bytes(str(file_size),"utf-8")
