import json
from typing import Dict, Any


def format_json(data: Dict[str, Any]) -> str:
    return json.dumps(data, indent=4)
