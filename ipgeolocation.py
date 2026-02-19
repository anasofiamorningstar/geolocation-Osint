import requests

def localizacion_precisa(ip):
    # Usamos IPinfo, que es conocida por tener mejores bases de datos de ciudades
    # Puedes sacar un token gratuito en ipinfo.io para más peticiones
    url = f"https://ipinfo.io/{ip}/json"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if 'loc' in data:
            lat_lon = data['loc'].split(',')
            print(f"\n--- Resultados de Alta Precisión ---")
            print(f"Ciudad: {data.get('city')} ({data.get('region')})")
            print(f"Coordenadas exactas del nodo: {lat_lon[0]}, {lat_lon[1]}")
            print(f"Código Postal: {data.get('postal')}") # Esto ayuda mucho a cerrar el cerco
            
            # Generar link directo a Google Maps con zoom máximo
            google_maps_url = f"https://www.google.com/maps?q={lat_lon[0]},{lat_lon[1]}&z=18"
            print(f"\n🔗 Ver en Google Maps: {google_maps_url}")
        else:
            print("No se pudo obtener la ubicación precisa.")
            
    except Exception as e:
        print(f"Error: {e}")

ip_target = input("Introduce la IP: ")
localizacion_precisa(ip_target)