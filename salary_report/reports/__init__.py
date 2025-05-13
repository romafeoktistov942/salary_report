from .payout import PayoutReport

REPORTS = {
    "payout": PayoutReport(),
}


def get_report(report_type: str):
    if report_type not in REPORTS:
        raise ValueError(f"Unknown report: {report_type}")
    return REPORTS[report_type].generate
