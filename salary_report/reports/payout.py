from typing import List, Dict
from collections import defaultdict
from .base import BaseReport
from .formatters.json_formatter import format_json


class PayoutReport(BaseReport):
    def generate(self, data: List[Dict], format: str = "text") -> str:
        if format == "json":
            return format_json(self.to_dict(data))
        return self._generate_text(data)

    def _generate_text(self, data: List[Dict]) -> str:
        departments = defaultdict(list)

        for row in data:
            hours = int(row["hours_worked"])
            rate = int(row["hourly_rate"])
            payment = float(hours) * float(rate)
            formatted_payment = f"{payment:.2f}"

            departments[row["department"]].append(
                {
                    "name": row["name"],
                    "hours": hours,
                    "rate": rate,
                    "payout": formatted_payment,
                }
            )

        lines = []
        for dept, employees in departments.items():
            lines.append(dept)
            total_hours = total_payout = 0

            for emp in employees:
                total_hours += emp["hours"]
                total_payout += float(emp["payout"])
                lines.append(
                    f"{'-'*16}  {emp['name']:<18} {emp['hours']:>5}  "
                    f"{emp['rate']:>5}  ${emp['payout']:>6}"
                )

            lines.append(
                f"{'':>38}Total: {total_hours:>5}  ${total_payout:>6.2f}"
            )
            lines.append("")

        return "\n".join(lines)

    def to_dict(self, data: List[Dict]) -> Dict:
        result = {"departments": {}}
        for row in data:
            dept = row["department"]
            if dept not in result["departments"]:
                result["departments"][dept] = {
                    "employees": [],
                    "total_hours": 0,
                    "total_payout": 0.0,
                }

            hours = int(row["hours_worked"])
            rate = int(row["hourly_rate"])
            payment = float(hours) * float(rate)

            result["departments"][dept]["employees"].append(
                {
                    "name": row["name"],
                    "hours": hours,
                    "rate": rate,
                    "payout": payment,
                }
            )
            result["departments"][dept]["total_hours"] += hours
            result["departments"][dept]["total_payout"] += payment

        return result


def generate_payout_report(data: List[Dict]) -> str:
    report = PayoutReport()
    return report.generate(data)
