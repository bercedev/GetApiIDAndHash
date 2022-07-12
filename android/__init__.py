from rich.console import Console
from rich.panel import Panel
import sys


console = Console()

def hata (text):
   console.print(Panel(f'[bold red]{text}[/]',width=70),justify="center")                         
def bilgi (text):
   console.print(Panel(f'[blue]{text}[/]',width=70),justify="center")                         
def basarili (text):
   console.print(Panel(f'[bold green] {text}[/]',width=70),justify="center")                         
def onemli (text):
   console.print(Panel(f'[bold cyan]{text}[/]',width=70),justify="center")                         
def soru (soru):
   console.print(Panel(f'[bold yellow]{soru}[/]',width=70),justify="center")                         
   return console.input(f"[bold yellow]>> [/]")
def logo (satirbırak=False):
    text = "█▀▀ █▀▀ █▀█ █▀▀ █▀▀ █▄█ █▄░█\n█▄▄ ██▄ █▀▄ █▄▄ ██▄ ░█░ █░▀█\n\n█░░ ▄▀█ █▄▄\n█▄▄ █▀█ █▄█"
    if satirbırak:
        for i in range(25):
            console.print("\n")
    console.print(Panel(f'[bold medium_purple]{text}[/]',width=90),justify="center")
def tamamlandi (api_id,api_hash):
   console.print(Panel(f"[bold green]Herşey Tamam!\n[i]Bilgileriniz: [/]",width=70),justify="center") 
   onemli("""Api ID:
   {}""".format(str(api_id)))
   onemli("""Api Hash:
   {}""".format(api_hash))
                   
