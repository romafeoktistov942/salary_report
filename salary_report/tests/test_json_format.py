from reports.payout import PayoutReport


def test_json_output():
    report = PayoutReport()
    data = [
        {
            "name": "Alice Johnson",
            "department": "Marketing",
            "hours_worked": "160",
            "hourly_rate": "50",
        }
    ]

    result = report.to_dict(data)
    expected = {
        "departments": {
            "Marketing": {
                "employees": [
                    {
                        "name": "Alice Johnson",
                        "hours": 160,
                        "rate": 50,
                        "payout": 8000.00,
                    }
                ],
                "total_hours": 160,
                "total_payout": 8000.00,
            }
        }
    }

    assert result == expected
