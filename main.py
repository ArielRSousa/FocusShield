# main.py

import os
import sys
import platform
import ctypes
from colorama import init, Fore, Style

from banner import print_banner, spinner_animation
from focus_shield import FocusShield

def checar_permissoes():
    """
    Verifica se o script está sendo executado como administrador (no Windows)
    ou superusuário/root (no Linux). Se não estiver, pede para que
    o usuário execute corretamente e encerra.
    """
    so = platform.system()  # "Windows", "Linux", "Darwin", etc.

    if so == "Windows":
        # Tenta verificar privilégios no Windows
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        except:
            is_admin = False

        if not is_admin:
            print(Fore.RED + "Por favor, execute este script como Administrador.")
            print("No Windows, abra o Prompt de Comando (ou PowerShell) como Admin,")
            print("ou clique com o botão direito no .py e escolha 'Executar como administrador'." + Style.RESET_ALL)
            sys.exit(1)

    else:
        # Em sistemas Unix (Linux, macOS, etc.)
        if os.geteuid() != 0:
            print(Fore.RED + "Por favor, execute este script como root (ou use 'sudo').")
            print("Exemplo: sudo python3 main.py" + Style.RESET_ALL)
            sys.exit(1)

def menu():
    print(Fore.YELLOW + Style.BRIGHT + """
    [1] Definir horários e INICIAR BLOQUEIO
    [2] PARAR/PAUSAR (desbloquear agora)
    [3] Sair
    """ + Style.RESET_ALL)

def definir_horarios(focus):
    """
    Pede ao usuário para digitar o horário de início e fim do bloqueio (no formato HH:MM)
    e define no objeto FocusShield.
    """
    while True:
        inicio = input(Fore.GREEN + "Digite o horário de INÍCIO do bloqueio (HH:MM): " + Style.RESET_ALL).strip()
        fim = input(Fore.GREEN + "Digite o horário de FIM do bloqueio (HH:MM): " + Style.RESET_ALL).strip()
        
        # Validação simples (apenas formato HH:MM)
        if len(inicio) == 5 and len(fim) == 5 and inicio[2] == ':' and fim[2] == ':':
            focus.set_time_block(inicio, fim)
            print(Fore.GREEN + Style.BRIGHT + f"\nHorários definidos: {inicio} - {fim}\n" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Formato inválido. Tente novamente.\n" + Style.RESET_ALL)

def main():
    # 1. Checar permissões antes de tudo
    checar_permissoes()

    # 2. Inicializa colorama (necessário para cores funcionarem no Windows)
    init(autoreset=True)

    print_banner()
    
    # Mostra um spinner de "carregamento" por 2 segundos
    spinner_animation(duration=2)

    # Ajuste o caminho do arquivo de hosts conforme seu SO
    # Ex. Windows: r"C:\Windows\System32\drivers\etc\hosts"
    # Linux/Mac: "/etc/hosts"
    hosts_file = r"/etc/hosts"

    # Lista de sites para bloqueio
    sites_para_bloquear = [
        "www.facebook.com",
        "facebook.com",
    ]

    # Cria a instância do FocusShield
    focus = FocusShield(sites_para_bloquear, hosts_file)

    while True:
        menu()
        opcao = input(Fore.CYAN + "Selecione uma opção: " + Style.RESET_ALL).strip()

        if opcao == "1":
            # Define horários e inicia o loop de bloqueio
            definir_horarios(focus)
            print(Fore.YELLOW + Style.BRIGHT + 
                  "Iniciando o loop de bloqueio (Ctrl + C para interromper a qualquer momento)\n" 
                  + Style.RESET_ALL)
            focus.start_block_loop(interval=60)  # Verifica a cada 60 segundos

        elif opcao == "2":
            # Para/pausa imediatamente o bloqueio
            if focus.block_loop_active:
                focus.stop_block_loop()
            else:
                print(Fore.RED + "\nNenhum bloqueio está ativo no momento.\n" + Style.RESET_ALL)

        elif opcao == "3":
            print(Fore.MAGENTA + "\nSaindo... Até mais!\n" + Style.RESET_ALL)
            # Se estiver bloqueando, desbloqueia antes de sair
            if focus.block_loop_active:
                focus.stop_block_loop()
            sys.exit()

        else:
            print(Fore.RED + "\nOpção inválida. Tente novamente.\n" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
