import json
import socket
from datetime import datetime
from pathlib import Path

import a2s

SITE_DIR = Path(__file__).resolve().parent
STATUS_PATH = SITE_DIR / "status.json"

ADDRESS = ("64.31.11.50", 28245)
TIMEOUT = 8.0


def fetch_status():
    socket.setdefaulttimeout(TIMEOUT)
    info = a2s.info(ADDRESS)
    players = a2s.players(ADDRESS)

    player_names = []
    for p in players:
        name = (getattr(p, "name", "") or "").strip()
        if name:
            player_names.append(name)

    return {
        "online": True,
        "players": f"{getattr(info, 'player_count', 0)}/{getattr(info, 'max_players', 0)}",
        "map": getattr(info, "map_name", None),
        "version": getattr(info, "version", None),
        "bots": int(getattr(info, "bot_count", 0) or 0),
        "player_names": player_names,
        "updated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
    }


def offline_payload(error_message: str):
    return {
        "online": False,
        "players": None,
        "map": None,
        "version": None,
        "bots": None,
        "player_names": [],
        "error": error_message,
        "updated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
    }


try:
    data = fetch_status()
except Exception as e:
    data = offline_payload(str(e))

STATUS_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(str(STATUS_PATH))
