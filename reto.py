import requests

api_key = "70a31adcfebbd27fe9159a663c44eff4"  # Reemplaza con tu clave de API
ciudad = "Tijuana"
url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"

try:
    respuesta = requests.get(url)
    respuesta.raise_for_status()  # Lanza una excepción para códigos de error HTTP
    datos = respuesta.json()

    temperatura = datos["main"]["temp"]
    descripcion = datos["weather"][0]["description"]

    print(f"Clima en {ciudad}:")
    print(f"Temperatura: {temperatura}°C")
    print(f"Descripción: {descripcion}")

except requests.exceptions.RequestException as e:
    print(f"Error al obtener datos del clima: {e}")
except KeyError:
    print("Error: Datos del clima no encontrados en la respuesta.")