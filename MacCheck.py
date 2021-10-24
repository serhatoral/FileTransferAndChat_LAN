
from subprocess import run, PIPE
from rich.console import Console
from rich.table import Table
import art


class MacCheck:

    def scan(self):
        out = run(["arp","-a"], check=True, stdout=PIPE).stdout        
        out= str(out)        
        lists= out.split("n ") 

        for i in range(0,len(lists)):
            lists[i]= lists[i].replace("\\r\\","")
            
        for i in range(2,len(lists)):
            lists[i]= " ".join(lists[i].split())
            lists[i]= lists[i].split(" ")

        lists.pop(0)
        lists.pop(0)                  
        return lists    

    def print_arp_table(self):
        console = Console()
        
        Art = art.text2art("MacCheck")                       
        console.print(Art, style="bold dark_turquoise")

        table = Table(show_header=True, header_style="bold magenta",width=100)
        table.add_column("IP", style="green", width=20)
        table.add_column("MAC",style="bright_yellow")
        table.add_column("TYPE",justify="center",style="red")
         
        dizi = self.scan()
        for i in dizi:                       
            table.add_row(i[0],i[1],i[2])

        console.print(table) 
                   



