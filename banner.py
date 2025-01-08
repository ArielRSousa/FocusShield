# banner.py
import sys
import time
from colorama import Fore, Style

def print_banner():
    # Exemplo de uso de cores com Fore e Style.
    print(Fore.CYAN + Style.BRIGHT + r"""
  _______  _______ _________  _______  _______
 (  ____ \(  ____ )\__   __/ (  ____ )(  ____ \
 | (    \/| (    )|   ) (    | (    )|| (    \/
 | (__    | (____)|   | |    | (____)|| (__    
 |  __)   |     __)   | |    |     __)|  __)   
 | (      | (\ (      | |    | (\ (   | (      
 | (____/\| ) \ \_____) (____| ) \ \__| (____/\
 (_______/|/   \__/\_______/|/   \__/(_______/
 
               BLOQUEADOR DE SITES
    """ + Style.RESET_ALL)

def spinner_animation(duration=3):
    """
    Exibe um spinner por 'duration' segundos, 
    sobrescrevendo a mesma linha no terminal.
    """
    spinner_chars = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    idx = 0

    while time.time() < end_time:
        # Move o cursor para o início da linha (\r) e não quebra a linha (end='')
        sys.stdout.write(f"\r{Fore.YELLOW}Carregando {spinner_chars[idx]}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.1)
        idx = (idx + 1) % len(spinner_chars)
    
    # Limpa a linha final e coloca uma quebra de linha
    sys.stdout.write("\rCarregamento concluído!        \n")
    sys.stdout.flush()
