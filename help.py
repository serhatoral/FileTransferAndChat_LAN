from rich.console import Console
from rich.table import Table

class Help:

    def help_write(self):
        console = Console()
                                    
        table = Table(show_header=True, header_style="bold magenta",width=100, show_lines=True)
        table.add_column("Komut", style="green", width=20)
        table.add_column("Açıklama",style="bright_yellow")       

        table.add_row(
        "dir",
        "Dosya ve klasörleri listeler")
        
        table.add_row(
            "download",
            "Karşı taraftan dosya indirmek için kullanılır.\nÖrn: download YeniKlasör1"
        )

        table.add_row(
            "upload",
            "Karşı taraftan dosya yüklemek için kullanılır.\nÖrn: upload video.mp4"
        )

        table.add_row(
            "cd",
            "Konum değişirmek için kullanılır.\nÖrn: cd .. (bir üst konuma geçer) \ncd C:\\Users"
        )
        table.add_row(
            "quit",
            "Modülü kapatmak için kullanılır."
        )

        table.add_row(
            "type",
            "İndirme işlemi yapmadan karşıdaki dosyanın içeriğini görmek için kullanılır.\nÖrn: type(notlar.txt) , type(test.py)"
        )

        table.add_row(
            "mkdir",
            "Yeni bir klasör oluşturmak için kullanılır.\nÖrn: mkdir Ödevler"
        )

        table.add_row(
            "type nul > dosyaİsmi.uzantı",
            "Boş yeni bir dosya oluşturmak için kullanılır.\nÖrn: type nul > hello.txt"
        )

        table.add_row(
            "del dosyaİsmi.uzantı",
            'Dosya silmek için kullanılır.\nÖrn: del hello.txt , del "merhaba dünya.txt"'
        )

        table.add_row(
            "copy",
            "Kopyalama işlemi için kullanılır. Kopyalanacak dosyanın ismi ve nereye kopyalanacağı girilir."+
            "\nÖrn: copy help.py C:\\Users\\"
        )

        table.add_row(
            "move",
            "Taşıma işlemi için kullanılır. Taşınacak dosyanın ismi ve nereye taşınacağı girilir."+
            "\nÖrn: move help.py C:\\Users\\"
        )

        table.add_row(
            "echo %cd%",
            "Hangi konumda olduğunuzu gösterir."
        )

        table.add_row(
            "ping",
            "Bir adrese ping atmak için kullanılır.\nÖrn: ping 79.123.224.15"
        )

        table.add_row(
            "arp -a",
            "Arp tablosunu görüntülemek için kullanılır."
        )
        console.print(table)






