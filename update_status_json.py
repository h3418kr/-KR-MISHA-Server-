import json
import subprocess
from datetime import datetime
from pathlib import Path

SITE_DIR = Path(__file__).resolve().parent
STATUS_PATH = SITE_DIR / 'status.json'

CMD = ['cmd','/c','set PYTHONIOENCODING=utf-8&& python C:\\Users\\INHA\\.openclaw\\workspace\\query_rust_a2s.py']

out = subprocess.run(CMD, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30)
lines = (out.stdout or '').splitlines()

data = {
    'online': False,
    'players': None,
    'map': None,
    'version': None,
    'bots': None,
    'player_names': [],
    'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
}

if out.returncode == 0 and lines:
    data['online'] = True
    for line in lines:
        line=line.strip()
        if line.startswith('players '):
            data['players'] = line.replace('players ','',1).strip()
        elif line.startswith('map '):
            data['map'] = line.replace('map ','',1).strip()
        elif line.startswith('version '):
            data['version'] = line.replace('version ','',1).strip()
        elif line.startswith('bots '):
            try:
                data['bots'] = int(line.replace('bots ','',1).strip())
            except Exception:
                data['bots'] = None
        elif line.startswith('player '):
            name = line.replace('player ','',1).strip()
            if name:
                data['player_names'].append(name)

STATUS_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
print(str(STATUS_PATH))
