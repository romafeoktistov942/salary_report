from reports.payout import generate_payout_report
import pytest
from salary_report.reports import get_report


def test_generate_payout_report():
    data = [
        {
            "name": "Alice Johnson",
            "department": "Marketing",
            "hours_worked": "160",
            "hourly_rate": "50",
        },
    ]
    result = generate_payout_report(data)

    expected_lines = [
        "Marketing",
        "----------------  Alice Johnson        160     50  $8000.00",
        "                                      Total:   160  $8000.00",
        "",
    ]
    expected_output = "\n".join(expected_lines)
    assert result == expected_output


def test_invalid_report():
    with pytest.raises(ValueError, match="Unknown report"):
        get_report("unknown")
