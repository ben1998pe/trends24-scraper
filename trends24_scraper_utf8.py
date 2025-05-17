"""
Scraper de tendencias desde Trends24.in - Perú (versión mejorada con soporte UTF-8)

Este script obtiene los términos más populares y los guarda en un CSV.

Autor: @ben1998pe
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

URL = "https://trends24.in/peru/"

def obtener_tendencias():
    response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    response.encoding = "utf-8"  # Asegura que tildes y ñ se decodifiquen bien
    soup = BeautifulSoup(response.text, "html.parser")

    bloques = soup.select("ol.trend-card__list")
    tendencias = []

    for bloque in bloques:
        for li in bloque.select("li"):
            texto = li.get_text(strip=True)
            if texto:
                tendencias.append(texto)

    return tendencias

def guardar_tendencias_csv(tendencias):
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df = pd.DataFrame({
        "Fecha y hora": [fecha_actual] * len(tendencias),
        "Tendencia": tendencias
    })

    archivo = "tendencias_peru.csv"
    try:
        df_existente = pd.read_csv(archivo)
        df_final = pd.concat([df_existente, df], ignore_index=True)
    except FileNotFoundError:
        df_final = df

    df_final.to_csv(archivo, index=False, encoding="utf-8-sig")
    print(f"[✓] {len(tendencias)} tendencias guardadas en {archivo}")

def main():
    print("[...] Obteniendo tendencias de Perú desde trends24.in ...")
    tendencias = obtener_tendencias()
    if tendencias:
        guardar_tendencias_csv(tendencias)
    else:
        print("[!] No se encontraron tendencias.")

if __name__ == "__main__":
    main()
