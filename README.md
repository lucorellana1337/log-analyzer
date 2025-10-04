# Log Analyzer for Trading Systems

Este proyecto analiza archivos de log (`server.log`) y genera reportes sobre errores comunes en sistemas de trading.

---

## 📌 Características
- Detecta errores comunes como:
  - `Connection lost`
  - `Timeout`
  - `Invalid order`
- Genera un reporte en formato **JSON** con:
  - Cantidad de errores por tipo.
  - Hora de la última ocurrencia.
- Simula alertas por correo o Slack.
- Fácil de extender a entornos reales.

---

## ⚙️ Instalación

```powershell
git clone <URL_DEL_REPOSITORIO>
cd log-analyzer
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
🚀 Uso
1. Analizar el log:
powershell
Copy code
python analyzer.py
2. Ver el reporte:
Se generará un archivo report.json con el resumen de errores.

Ejemplo de salida:

json
Copy code
{
    "Connection lost": {
        "count": 2,
        "last_occurrence": "2025-10-04 11:33:40"
    },
    "Timeout": {
        "count": 2,
        "last_occurrence": "2025-10-04 12:01:18"
    },
    "Invalid order": {
        "count": 1,
        "last_occurrence": "2025-10-04 10:20:30"
    }
}
🧠 Valor profesional
Este proyecto demuestra capacidad para:

Analizar logs de producción.

Identificar errores sistémicos.

Generar reportes automatizados.

Simular notificaciones técnicas.

Perfecto para un rol de Trading Operations Engineer o Production Support.

📂 Estructura del proyecto
pgsql
Copy code
log-analyzer/
│── analyzer.py
│── server.log
│── report.json
│── requirements.txt
│── README.md
│── venv/
yaml
Copy code

---

¿Quieres que te prepare también un ejemplo realista de `server.log` para probar el script con datos r