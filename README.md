# SimpleHashCracker
El script utiliza unicamente las librerias hashlib y time (aunque esta se puede quitar) contiene 4 algoritmos ya predefinidos MD5, SHA1, SHA256 y SHA512 pero pueden cambiarse segun sus necesidades en el apartado:
    
    hash_info = {
        32: {"func": hashlib.md5, "name": "MD5"},
        40: {"func": hashlib.sha1, "name": "SHA-1"},
        64: {"func": hashlib.sha256, "name": "SHA-256"},
        128: {"func": hashlib.sha512, "name": "SHA-512"}
    }

Fin

Para usar el script simplemente ejecute 

    python3 simple_hash_cracker.py

V1.3
    
    [-] Output la misma mrd
    [+] Optimizacion
    [+] Mas facilidad para agregar algoritmos
    [+] Unificación de funciones y eliminación de clases

V1.2

    [+] Limite de intentos en el input de hash y de la ruta de wordlists
    [+] Colores
    [+] Validacion de hashes segun longitud
    [+] Manejo de excepciones
    [-] Horas de sin dormir depurando
