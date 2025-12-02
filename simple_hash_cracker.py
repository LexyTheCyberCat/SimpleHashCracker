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

    def MD5_hash():
        for i in wordlist:
            hash_supersexy = hashlib.md5(i.encode()).hexdigest()
            # print(f"probando: {i} \nhash: {hash_supersexy} \n") # opcional: para ver el proceso
            
            if password == hash_supersexy:
                print(f"{colors.green}[+] {colors.reset}Contraseña crackeada: {colors.yellow}{i}")
                break
        
        if password != hash_supersexy:
            print(f"{colors.red}[-] {colors.reset}Contraseña no encontrada :(")

    def SHA256_hash():
        for i in wordlist:
            hash_supersexy = hashlib.sha256(i.encode()).hexdigest()
            # print(f"probando: {i} \nhash: {hash_supersexy} \n") # opcional: para ver el proceso
            
            if password == hash_supersexy:
                print(f"{colors.green}[+] {colors.reset}Contraseña crackeada: {colors.yellow}{i}")
                break
        
        if password != hash_supersexy:
            print(f"{colors.red}[-] {colors.reset}Contraseña no encontrada :(")

    def SHA512_hash():
        for i in wordlist:
            hash_supersexy = hashlib.sha512(i.encode()).hexdigest()
            # print(f"probando: {i} \nhash: {hash_supersexy} \n") # opcional: para ver el proceso
            
            if password == hash_supersexy:
                print(f"{colors.green}[+] {colors.reset}Contraseña crackeada: {colors.yellow}{i}")
                break
        
        if password != hash_supersexy:
            print(f"{colors.red}[-] {colors.reset}Contraseña no encontrada :(")

    # def otro():
    #     for i in wordlist:
    #         hash_supersexy = hashlib.hash(i.encode()).hexdigest() # cambiar "hash" por el algoritmo que uses
    #         # print(f"probando: {i} \nhash: {hash_supersexy} \n") # opcional: para ver el proceso
    #         
    #         if password == hash_supersexy:
    #             print(f"{colors.green}[+] {colors.reset}Contraseña crackeada: {colors.yellow}{i}")
    #             break
    #     
    #     if password != hash_supersexy:
    #         print(f"{colors.red}[-] {colors.reset}Contraseña no encontrada :(")

    # Elije la funcion segun cantidad de caracteres
    match caracteres:
            case 32:
                print(f"{colors.green}[+] {colors.reset}Hash MD5 detectado\n")
                MD5_hash()

            case 64:
                print(f"{colors.green}[+] {colors.reset}Hash SHA256 detectado\n")
                SHA256_hash()

            case 128:
                print(f"{colors.green}[+] {colors.reset}Hash SHA512 detectado\n")
                SHA512_hash()

            #case otro:
            #    otro()

if __name__ == "__main__":
    __main__()
