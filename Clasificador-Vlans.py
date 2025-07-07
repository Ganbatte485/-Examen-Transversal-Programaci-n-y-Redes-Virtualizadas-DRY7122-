def clasificar_vlan(numero_vlan):
    if numero_vlan == 0 or numero_vlan == 4095:
        return "reservada"
    elif 1 <= numero_vlan <= 1005:
        return "normal"
    elif 1006 <= numero_vlan <= 4094:
        return "extendido"
    else:
        return "inválido"

def main():
    print("CLASIFICADOR DE VLANs (Escribe 'salir' para terminar)")
    while True:
        try:
            entrada = input("Ingrese el número de VLAN (0-4095): ")
            if entrada.strip().lower() == 'salir':
                print("Programa terminado.")
                break
            numero_vlan = int(entrada)
            tipo_vlan = clasificar_vlan(numero_vlan)
            if tipo_vlan == "normal":
                print("TIPO: VLAN de RANGO NORMAL | RANGO: 1 - 1005 | VLANs estándar soportadas por todos los switches\n")
            elif tipo_vlan == "extendido":
                print("TIPO: VLAN de RANGO EXTENDIDO | RANGO: 1006 - 4094 | VLANs extendidas para redes grandes\n")
            elif tipo_vlan == "reservada":
                print("TIPO: VLAN RESERVADA | VLAN reservada por el estándar IEEE 802.1Q\n")
            else:
                print("TIPO: NÚMERO DE VLAN INVÁLIDO | El número debe estar entre 0 y 4095\n")
        except ValueError:
            print("[ERROR] Por favor ingrese un número válido\n")
        except KeyboardInterrupt:
            print("\nPrograma terminado por el usuario.")
            break

if __name__ == "__main__":
    main()
