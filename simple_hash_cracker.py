import hashlib
import time
def __main__():
    class colors:
        red = '\033[91m'
        blue = '\033[94m'
        cyan = '\033[96m'
        green = '\033[92m'
        reset = '\033[0m'
        magenta = '\033[95m'
        yellow = '\033[93m'
    
    intentos_hash = 0
    intentos_wordlist = 0
    max_intent = 3

    # Validacion de hash
    while intentos_hash <= max_intent:
            
            password = input(f"{colors.blue}[*] {colors.reset}Ingresa el hash: {colors.green}").lower().replace(" ", "").strip()
            caracteres = len(password)
            
            if caracteres < 32:
                print(f"{colors.red}[-] {colors.reset}Hash invalido")
                intentos_hash = 1 + intentos_hash

                if intentos_hash >= max_intent:
                    print(f"{colors.red}[-] {colors.reset}Limite de intentos alcanzado, saliendo..."), time.sleep(0.7)
                    exit()
                continue
            else:
                    break

    # Validacion de ruta
    while intentos_wordlist <= max_intent:
        try:
            ruta = input(f"{colors.blue}[*] {colors.reset}Ingresa la ruta a tu wordlist: {colors.green}").replace(" ", "").strip()
            with open(f"{ruta}", "r", encoding="latin-1") as archivo:
                wordlist = archivo.read().splitlines()
                break
        
        except FileNotFoundError:
            print(f"{colors.red}[-] {colors.reset}Error: Ruta no encontrada")
            intentos_wordlist = 1 + intentos_wordlist
            
            if intentos_wordlist >= max_intent:
                print(f"{colors.red}[-] {colors.reset}Limite de intentos alcanzado, saliendo..."), time.sleep(0.7)
                exit()

    print(f"\n{colors.green}Hash: {colors.reset}{password}\n{colors.blue}[*]{colors.reset} Crackeando, porfavor espere...\n"), time.sleep(1)

    hash_info = {
        32: {"func": hashlib.md5, "name": "MD5"},
        40: {"func": hashlib.sha1, "name": "SHA-1"},
        64: {"func": hashlib.sha256, "name": "SHA-256"},
        128: {"func": hashlib.sha512, "name": "SHA-512"}
    }

    def crackear_hash():      
        if caracteres not in hash_info:
            print(f"{colors.red}[-] {colors.reset}Hash no soportado ({caracteres} chars)")
            return
        
        info = hash_info[caracteres]
        funcion_hash = info["func"]

        for i in wordlist:
            hash_supersexy = funcion_hash(i.encode()).hexdigest()
            # print(f"probando: {i} \nhash: {hash_supersexy} \n") # opcional: para ver el proceso
            
            if password == hash_supersexy:
                print(f"{colors.green}[+] {colors.reset}Contraseña crackeada: {colors.yellow}{i}")
                break
        
        if password != hash_supersexy:
            print(f"{colors.red}[-] {colors.reset}Contraseña no encontrada :(")

    if caracteres in hash_info:
        info = hash_info[caracteres]
        nombre = info["name"] 
        print(f"{colors.green}[+] {colors.reset}Hash {nombre} detectado\n")
        crackear_hash()

if __name__ == "__main__":
    __main__()
