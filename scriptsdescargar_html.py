import requests

def descargar_html(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verifica si la solicitud fue exitosa
        return respuesta.text
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

url = "https://www.facebook.com/login/"
html = descargar_html(url)

if html:
    with open("facebook_login.html", "w", encoding="utf-8") as archivo:
        archivo.write(html)
    print("HTML descargado y guardado en facebook_login.html")
else:
    print("No se pudo descargar el HTML")