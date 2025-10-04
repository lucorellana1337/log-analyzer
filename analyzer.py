import re
import json
from datetime import datetime

LOG_FILE = 'server.log'
OUTPUT_FILE = 'report.json'

ERROR_PATTERNS = {
    'Connection lost': r'Connection lost',
    'Timeout': r'Timeout',
    'Invalid order': r'Invalid order'
}

def send_alert(error_type, count):
    # Simulación de alerta (puede ser por correo o Slack)
    print(f'🚨 ALERTA SIMULADA: {count} errores de tipo \"{error_type}\" detectados.')

def analyze_log():
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    results = {err: {'count': 0, 'last_occurrence': None} for err in ERROR_PATTERNS}

    for line in lines:
        for err_type, pattern in ERROR_PATTERNS.items():
            if re.search(pattern, line):
                timestamp = line.split(' ')[0] + ' ' + line.split(' ')[1]
                results[err_type]['count'] += 1
                results[err_type]['last_occurrence'] = timestamp

    # Enviar alertas si hay errores
    for err_type, data in results.items():
        if data['count'] > 0:
            send_alert(err_type, data['count'])

    # Guardar reporte JSON
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4)

    print('\\n✅ Reporte generado en', OUTPUT_FILE)
    print(json.dumps(results, indent=4))

if __name__ == '__main__':
    analyze_log()
