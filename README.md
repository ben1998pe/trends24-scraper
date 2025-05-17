# 📈 Trends24 Scraper – Perú

Este proyecto es un scraper desarrollado en Python que extrae los temas de tendencia en Twitter para Perú desde [trends24.in](https://trends24.in/peru/).

---

## 🚀 Características

- Extrae tendencias desde trends24.in (no requiere API ni login)
- Guarda los datos con fecha y hora
- Salida en formato CSV (`tendencias_peru.csv`)
- Codificación compatible con tildes y caracteres especiales

---

## 📦 Requisitos

- Python 3.8+
- Librerías necesarias:

```
pip install -r requirements.txt
```

---

## 🧠 Cómo usar

1. Ejecuta el script:

```
python trends24_scraper_utf8.py
```

2. Se generará un archivo `tendencias_peru.csv` con las tendencias actuales y la fecha/hora de captura.

---

## 📁 Estructura esperada

- `trends24_scraper_utf8.py`
- `requirements.txt`
- `README.md`
- `tendencias_peru.csv` (se genera automáticamente)

---

## 🧼 Notas

- El script agrega nuevas filas al archivo CSV cada vez que se ejecuta.
- La codificación es `utf-8-sig` para compatibilidad con Excel.

---

## 👨‍💻 Autor

Desarrollado por [@ben1998pe](https://github.com/ben1998pe)

---

## 📄 Licencia

MIT
