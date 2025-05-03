import subprocess
import os
from datetime import datetime

# Banner ASCII
banner = r"""


Hlahaploker 


 ___   _                     _   _            _    _               _____                    
|_ _| | |    _____   _____  | | | | __ _  ___| | _(_)_ __   __ _  |_   _|__  __ _ _ __ ___  
 | |  | |   / _ \ \ / / _ \ | |_| |/ _` |/ __| |/ / | '_ \ / _` |   | |/ _ \/ _` | '_ ` _ \ 
 | |  | |__| (_) \ V /  __/ |  _  | (_| | (__|   <| | | | | (_| |   | |  __/ (_| | | | | | |
|___| |_____\___/ \_/ \___| |_| |_|\__,_|\___|_|\_\_|_| |_|\__, |   |_|\___|\__,_|_| |_| |_|
                                                           |___/                            

                          
      Bienvenidos a Hacking Team Comunidad De Hackers By AnonSec777 Telegram: https://t.me/+74d-97oV7P05OTVk
"""

print(banner)

# Pedir dominio
target = input("Introduce el dominio o URL objetivo (sin http/https): ").strip()

# Crear carpeta de resultados con timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
base_dir = f"hacking_team_results_{target}_{timestamp}"
os.makedirs(base_dir, exist_ok=True)

def run_cmd(cmd, output_file=None):
    print(f"Ejecutando: {' '.join(cmd)}")
    with open(output_file, "w") if output_file else open(os.devnull, "w") as f:
        subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT)

# 1. Escaneo nmap
nmap_file = os.path.join(base_dir, "nmap_scan.txt")
run_cmd(["nmap", "-sC", "-sV", target], nmap_file)

# 2. Recolección de URLs con gau, gauplus, hakrawler, waybackurls
urls_dir = os.path.join(base_dir, "urls")
os.makedirs(urls_dir, exist_ok=True)

gau_file = os.path.join(urls_dir, "gau.txt")
run_cmd(["gau", target], gau_file)

gauplus_file = os.path.join(urls_dir, "gauplus.txt")
run_cmd(["gauplus", target], gauplus_file)

hakrawler_file = os.path.join(urls_dir, "hakrawler.txt")
run_cmd(["hakrawler", "-url", f"https://{target}"], hakrawler_file)

wayback_file = os.path.join(urls_dir, "waybackurls.txt")
run_cmd(["waybackurls", target], wayback_file)

# 2.5. Ejecutar paramspider para encontrar parámetros
paramspider_file = os.path.join(urls_dir, "paramspider.txt")

# Cambia esta ruta a donde tengas paramspider.py
paramspider_path = os.path.expanduser("~/tools/ParamSpider/paramspider.py")

run_cmd(["python3", paramspider_path, "-d", target, "-o", paramspider_file])

# Combinar URLs únicas de todas las fuentes
combined_urls_file = os.path.join(urls_dir, "combined_urls.txt")
seen = set()
for fname in [gau_file, gauplus_file, hakrawler_file, wayback_file, paramspider_file]:
    if os.path.exists(fname):
        with open(fname) as infile:
            for line in infile:
                url = line.strip()
                if url and url not in seen:
                    seen.add(url)

with open(combined_urls_file, "w") as outfile:
    for url in seen:
        outfile.write(url + "\n")

# 3. Verificar URLs con httpx
httpx_file = os.path.join(urls_dir, "httpx_results.txt")
run_cmd(["httpx", "-f", combined_urls_file, "-silent"], httpx_file)

# 4. Escaneo con katana
katana_file = os.path.join(base_dir, "katana_scan.txt")
run_cmd(["katana", "-u", f"https://{target}", "-json", "-o", katana_file])

# 5. Escaneo con nuclei
nuclei_file = os.path.join(base_dir, "nuclei_scan.txt")
run_cmd(["nuclei", "-l", combined_urls_file, "-o", nuclei_file])

# 6. Pruebas con sqlmap (simple, para un parámetro GET)
sqlmap_file = os.path.join(base_dir, "sqlmap_scan.txt")
test_url = f"http://{target}/?id=1"
run_cmd(["sqlmap", "-u", test_url, "--batch", "--level=2", "--risk=2"], sqlmap_file)

# 7. Metasploit (solo mostrar banner y sugerir uso manual)
print("\n[!] Metasploit requiere interacción manual. Ejecuta 'msfconsole' para comenzar.")

print(f"\nResultados guardados en: {base_dir}")
print("Escaneo completado. Revisa los archivos para detalles.")
