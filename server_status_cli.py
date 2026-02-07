import os, socket, psutil, sys, time

from rich.live import Live  # pyright: ignore[reportMissingImports]
from rich.panel import Panel # pyright: ignore[reportMissingImports]
from rich.console import Console # pyright: ignore[reportMissingImports]


VERSION = "1.0"
console = Console()

login = os.getlogin()

hostname = socket.gethostname()
localhost = socket.gethostbyname(hostname)

info = os.uname()
os_info = f"{info.sysname} {info.nodename}"

def build_panel(cpu,ram,disk):
    return Panel(f"""
Hi, {login}! 
{os_info}

HOST:{localhost}
CPU:{cpu}%
RAM:{ram}%
DISK:{disk}%""", title="SERVER STATS",style="green")


if "--version" in sys.argv or "-v" in sys.argv:
    print(VERSION)
else:
    with Live(build_panel(0,0,0), console=console, refresh_per_second=4) as Live:
        while True:
            Live.update(build_panel(psutil.cpu_percent(),psutil.virtual_memory().percent, psutil.disk_usage("/").percent))
            time.sleep(0.5)
       
       


