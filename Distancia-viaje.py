import requests
import sys

API_KEY_ORS = "5b3ce3597851110001cf624828db50540c7e489589a657349b3e21b8"
URL_GEOCODE = "https://api.openrouteservice.org/geocode/search"
URL_DIRECTIONS_BASE = "https://api.openrouteservice.org/v2/directions"

transportes = {
    "auto": "driving-car",
    "camión": "driving-hgv",
    "bicicleta": "cycling-regular",
    "a pie": "foot-walking"
}

def obtener_coordenadas(ciudad):
    params = {
        "api_key": API_KEY_ORS,
        "text": ciudad,
        "size": 1
    }
    response = requests.get(URL_GEOCODE, params=params)
    datos = response.json()
    try:
        coords = datos["features"][0]["geometry"]["coordinates"]
        return coords[0], coords[1]
    except IndexError:
        print(f"❌ No se encontraron coordenadas para '{ciudad}'")
        return None

def calcular_ruta(origen, destino, modo):
    url = f"{URL_DIRECTIONS_BASE}/{modo}"
    body = {
        "coordinates": [origen, destino]
    }
    headers = {
        "Authorization": API_KEY_ORS,
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=body, headers=headers)
    datos = response.json()
    ruta = datos["routes"][0]["summary"]
    distancia_km = ruta["distance"] / 1000
    distancia_mi = distancia_km * 0.621371
    duracion_min = ruta["duration"] / 60
    return distancia_km, distancia_mi, duracion_min

print("🧭 Evaluación DRY7122 – Script de distancia entre ciudades")
print("Escribe 's' para salir en cualquier momento\n")

while True:
    origen_txt = input("Ciudad de origen (Chile): ").strip()
    if origen_txt.lower() == "s":
        sys.exit()
    destino_txt = input("Ciudad de destino (Argentina): ").strip()
    if destino_txt.lower() == "s":
        sys.exit()

    print("\nMedios disponibles: auto, camión, bicicleta, a pie")
    medio = input("Seleccione medio de transporte: ").strip().lower()
    if medio == "s":
        sys.exit()
    if medio not in transportes:
        print("❌ Medio no válido")
        continue

    print("\n🔍 Buscando coordenadas...")
    origen_coords = obtener_coordenadas(origen_txt)
    destino_coords = obtener_coordenadas(destino_txt)
    if not origen_coords or not destino_coords:
        continue

    print("🚀 Calculando ruta...")
    distancia_km, distancia_mi, duracion_min = calcular_ruta(
        origen_coords, destino_coords, transportes[medio])

    horas = int(duracion_min // 60)
    minutos = int(duracion_min % 60)

    print("\n📍 Resultado:")
    print(f"Distancia: {distancia_km:.2f} km | {distancia_mi:.2f} millas")
    print(f"Duración estimada: {horas}h {minutos}min")
    print(f"Narrativa: Desde {origen_txt} hasta {destino_txt} en {medio}, se recorrerán {distancia_km:.2f} km en aproximadamente {horas} horas y {minutos} minutos.\n")
