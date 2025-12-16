import subprocess
import time
import sys
import re
import os


try:
    from colorama import init, Fore, Style, Back
    init(autoreset=True)
    
    C_HEADER = Fore.CYAN + Style.BRIGHT
    C_GREEN = Fore.GREEN + Style.BRIGHT
    C_WARN = Fore.YELLOW
    C_FAIL = Fore.RED
    C_TEXT = Fore.WHITE
    C_MUTE = Fore.LIGHTBLACK_EX
    C_ACCENT = Fore.MAGENTA + Style.BRIGHT
except:
    C_HEADER = C_GREEN = C_WARN = C_FAIL = C_TEXT = C_MUTE = C_ACCENT = ""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    
    banner = f"""
{C_ACCENT}    _       __ _    ______ _      
{C_ACCENT}   | |     / /(_)  / ____/(_)     
{C_ACCENT}   | | /| / / /   / /_   / /      
{C_ACCENT}   | |/ |/ / /   / __/  / /       
{C_ACCENT}   |__/|__/_/   /_/    /_/        
{C_TEXT}   Wi-Fi Analyzer CLI - QuinteroJ17
    """
    print(banner)

def spinner(duration=2):
    
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    print(f"{C_MUTE}   Scanning environment...", end="", flush=True)
    while time.time() < end_time:
        for char in chars:
            sys.stdout.write(f"\b{C_ACCENT}{char}{C_MUTE}")
            sys.stdout.flush()
            time.sleep(0.1)
    print(f"\r   {C_GREEN}✔ Scan Complete.        ")

def parse_networks(output):
    
    networks = []
    current_net = {}
    
    lines = output.split('\n')
    for line in lines:
        line = line.strip()
        
        # Nuevo SSID 
        if line.startswith("SSID"):
            
            if current_net:
                networks.append(current_net)
            current_net = {"ssid": "Hidden Network", "bssid": "N/A", "signal": "0%", "auth": "Open"}
            
            parts = line.split(":")
            if len(parts) > 1 and parts[1].strip():
                current_net["ssid"] = parts[1].strip()

        # Capturar MAC (BSSID)
        elif line.startswith("BSSID"):
            parts = line.split(":")
            if len(parts) > 1:
                # Reconstruir la MAC 
                current_net["bssid"] = ":".join(parts[1:]).strip()

        # Capturar Señal 
        elif "%" in line:
            # Regex para sacar solo el número
            match = re.search(r'(\d+)%', line)
            if match:
                current_net["signal"] = match.group(1) + "%"
        
        # Capturar Autenticación
        elif "Autenti" in line or "Authenti" in line:
             parts = line.split(":")
             if len(parts) > 1:
                 current_net["auth"] = parts[1].strip()

    # Añadir la última red
    if current_net:
        networks.append(current_net)
        
    return networks

def print_table(networks):
    
    # Cabecera de la tabla
    print(f"\n   {C_HEADER}{'SSID NAME':<25} {C_HEADER}{'BSSID (MAC)':<20} {C_HEADER}{'SIGNAL':<10} {C_HEADER}{'AUTH':<15}")
    print(f"   {C_MUTE}" + "-"*70)

    # Filas
    if not networks:
        print(f"   {C_FAIL}No networks found or interface disabled.")
        return

    # Ordenar por potencia de señal (de mayor a menor)
    networks.sort(key=lambda x: int(x['signal'].strip('%')) if x['signal'] != '0%' else 0, reverse=True)

    for net in networks:
        # Colorear la señal según intensidad
        signal_val = int(net['signal'].strip('%'))
        sig_color = C_FAIL
        if signal_val > 80: sig_color = C_GREEN
        elif signal_val > 50: sig_color = C_WARN

        print(f"   {C_TEXT}{net['ssid']:<25} {C_MUTE}{net['bssid']:<20} {sig_color}{net['signal']:<10} {C_TEXT}{net['auth']:<15}")

def main():
    try:
        clear_screen()
        print_banner()
        
        while True:
            # Ejecutar spinner
            spinner(1.5)
            
            # Obtener datos reales
            try:
                raw_output = subprocess.check_output("netsh wlan show networks mode=bssid", shell=True).decode('latin-1', errors='ignore')
                networks = parse_networks(raw_output)
                print_table(networks)
            except Exception as e:
                print(f"{C_FAIL}Error: {e}")

            print(f"\n   {C_MUTE}[Ctrl+C to Stop]  Refreshing in 5s...")
            time.sleep(5)
            # Limpiar pantalla para el siguiente frame 
            clear_screen()
            print_banner()

    except KeyboardInterrupt:
        print(f"\n\n   {C_ACCENT}Goodbye! 👾\n")

if __name__ == "__main__":
    main()
