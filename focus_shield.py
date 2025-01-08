# focus_shield.py

import time
from datetime import datetime
from colorama import Fore, Style

class FocusShield:
    def __init__(self, sites, hosts_file):
        """
        sites: lista de sites para bloqueio
        hosts_file: caminho para o arquivo de hosts do sistema
        """
        self.sites = sites
        self.hosts_file = hosts_file
        
        # Horários de início e fim do bloqueio (strings no formato HH:MM)
        self.block_start = None
        self.block_end = None
        
        # Flag para saber se o loop de bloqueio está ativo
        self.block_loop_active = False

        # IP de redirecionamento
        self.redirect = "127.0.0.1"

    def set_time_block(self, start, end):
        """
        Define os horários de bloqueio (no formato HH:MM).
        """
        self.block_start = start
        self.block_end = end

    def is_within_block_time(self):
        """
        Verifica se a hora atual está dentro do intervalo definido.
        Retorna True se estiver no horário de bloqueio, senão False.
        """
        if not self.block_start or not self.block_end:
            return False  # Se não há horários definidos, não bloqueia.
        
        current_time = datetime.now().strftime("%H:%M")
        return self.block_start <= current_time < self.block_end

    def block_sites(self):
        """
        Adiciona as linhas de redirecionamento para cada site no arquivo de hosts.
        """
        try:
            with open(self.hosts_file, "r+", encoding="utf-8") as file:
                content = file.read()
                for site in self.sites:
                    entry = f"{self.redirect} {site}\n"
                    if entry not in content:
                        file.write(entry)
        except PermissionError:
            print(Fore.RED + "\n[ERRO] Permissão negada! Execute este script como administrador/sudo.\n")
        except Exception as e:
            print(Fore.RED + f"\n[ERRO] Ocorreu um problema ao bloquear sites: {e}\n")

    def unblock_sites(self):
        """
        Remove as linhas de bloqueio (redirecionamento) do arquivo de hosts.
        """
        try:
            with open(self.hosts_file, "r+", encoding="utf-8") as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    # Se a linha não contiver nenhum dos sites, mantemos
                    if not any(site in line for site in self.sites):
                        file.write(line)
                file.truncate()
        except PermissionError:
            print(Fore.RED + "\n[ERRO] Permissão negada! Execute este script como administrador/sudo.\n")
        except Exception as e:
            print(Fore.RED + f"\n[ERRO] Ocorreu um problema ao desbloquear sites: {e}\n")

    def start_block_loop(self, interval=60):
        """
        Inicia um loop que verifica, a cada 'interval' segundos,
        se deve bloquear ou desbloquear os sites.
        """
        self.block_loop_active = True
        
        try:
            while self.block_loop_active:
                if self.is_within_block_time():
                    self.block_sites()
                    print(Fore.GREEN + f"[{datetime.now().strftime('%H:%M:%S')}] Sites BLOQUEADOS!" + Style.RESET_ALL)
                else:
                    self.unblock_sites()
                    print(Fore.BLUE + f"[{datetime.now().strftime('%H:%M:%S')}] Sites LIBERADOS!" + Style.RESET_ALL)
                
                print(Fore.WHITE + f"Verificando novamente em {interval} segundos...\n" + Style.RESET_ALL)
                time.sleep(interval)

        except KeyboardInterrupt:
            # Caso o usuário aperte Ctrl + C, desbloqueia e sai do loop
            self.unblock_sites()
            print(Fore.RED + "\n[!] Loop de bloqueio interrompido pelo usuário. Sites foram desbloqueados.\n" + Style.RESET_ALL)
        finally:
            self.block_loop_active = False

    def stop_block_loop(self):
        """
        Para o loop de bloqueio, desbloqueia os sites imediatamente
        e seta a flag block_loop_active para False.
        """
        self.block_loop_active = False
        self.unblock_sites()
        print(Fore.MAGENTA + "\nBloqueio interrompido. Sites desbloqueados.\n" + Style.RESET_ALL)
