# SimpleHashCracker
El script utiliza unicamente la libreria hashlib y la libreria time (aunque esta se puede quitar) contiene 3 algoritmos ya predefinidos MD5, SHA256 y SHA512 pero pueden cambiarse segun sus necesidades. La funcion otro() esta hecha especificamente para usar un algoritmo distinto sin tener que reescribir todo el codigo, simplemente cambie la palabra "hash" en la linea 33 'hash_supersexy = hashlib.hash(i.encode()).hexdigest()' por el algoritmo que desee usar.

Fin

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
