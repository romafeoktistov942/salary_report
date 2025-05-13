def normalize_headers(headers: list[str]) -> list[str]:
    normalized = []
    for h in headers:
        h_lower = h.strip().lower()
        if h_lower in ("hourly_rate", "rate", "salary"):
            normalized.append("hourly_rate")
        else:
            normalized.append(h_lower)
    return normalized
