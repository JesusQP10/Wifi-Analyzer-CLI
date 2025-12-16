# 📡 Wi-Fi Analyzer CLI

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Plataforma](https://img.shields.io/badge/Plataforma-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Licencia](https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-Activo-success?style=for-the-badge)

> **Herramienta CLI para análisis de redes Wi-Fi en tiempo real y visualización de espectro en sistemas Windows.**

---

<img width="927" height="407" alt="Captura de pantalla 2025-12-16 1" src="https://github.com/user-attachments/assets/e84f6aab-d185-4d55-8def-7086e1014e89" />


*(Datos sensibles pixelados por seguridad)*

---

## 🦅 Descripción General

**Wi-Fi Analyzer CLI** es una herramienta de reconocimiento ligera, desarrollada en Python, diseñada para escanear, analizar y visualizar redes inalámbricas locales. Utiliza comandos nativos del sistema Windows (`netsh`) para recuperar datos brutos y los formatea en una interfaz de terminal limpia.

## ⚡ Características

* **Escaneo en Tiempo Real:** Monitorización en vivo de los puntos de acceso disponibles.
* **Procesado de Datos (Parsing):** Extrae SSID, BSSID (Dirección MAC), Potencia de la Señal (RSSI %) y protocolos de Autenticación.
* **Ordenación Inteligente:** Clasifica automáticamente las redes por intensidad de señal (de mayor a menor).
* **Feedback Visual:** Indicadores de señal por colores (Verde/Amarillo/Rojo) para una evaluación de calidad instantánea.
* **Interfaz:** Banner ASCII personalizado.
* **Enfoque en Privacidad:** Diseñado para ejecutarse con privilegios mínimos (aunque se recomienda Administrador para visibilidad total de MACs).

## 🛠️ Instalación

### Requisitos
* Windows 10/11
* Python 3.x
* Tarjeta de Red Wi-Fi

## 🚀 Uso

Ejecuta el script directamente desde tu terminal (PowerShell o CMD para la mejor fidelidad visual):

```bash
python wifi_scan.py
```
## ⚠️ Advertencia

Este proyecto ha sido desarrollado con fines educativos.
No utilizar contra sistemas sin previa autorización.
