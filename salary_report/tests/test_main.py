import subprocess
import pytest
from salary_report.main import parse_args


def test_main_output(tmp_path):
    test_file = tmp_path / "data.csv"
    test_file.write_text(
        """id,email,name,department,hours_worked,salary
1,alice@example.com,Alice Johnson,Marketing,160,50
"""
    )

    result = subprocess.run(
        [
            "python3",
            "salary_report/main.py",
            str(test_file),
            "--report",
            "payout",
        ],
        capture_output=True,
        text=True,
    )

    expected_output = """Marketing
----------------  Alice Johnson        160     50  $8000.00
                                      Total:   160  $8000.00
"""
    assert expected_output in result.stdout


def test_invalid_arguments():
    with pytest.raises(SystemExit):
        parse_args([])


def test_invalid_report_type(tmp_path):
    test_file = tmp_path / "data.csv"
    test_file.write_text(
        """id,email,name,department,hours_worked,salary
1,alice@example.com,Alice Johnson,Marketing,160,50
"""
    )

    result = subprocess.run(
        [
            "python3",
            "salary_report/main.py",
            str(test_file),
            "--report",
            "invalid_type",
        ],
        capture_output=True,
        text=True,
    )
    assert "Unknown report" in result.stderr


def test_file_not_found():
    result = subprocess.run(
        [
            "python3",
            "salary_report/main.py",
            "nonexistent.csv",
            "--report",
            "payout",
        ],
        capture_output=True,
        text=True,
    )
    assert "No such file" in result.stderr


def test_invalid_format_combination(tmp_path):
    input_file = tmp_path / "data.csv"
    output_file = tmp_path / "report.txt"

    input_file.write_text(
        "id,email,name,department,hours_worked,salary\n"
        "1,alice@example.com,Alice Johnson,Marketing,160,50\n"
    )

    # Проверяем несоответствие JSON формата и .txt расширения
    result = subprocess.run(
        [
            "python3",
            "salary_report/main.py",
            str(input_file),
            "--report",
            "payout",
            "--format",
            "json",
            "--output",
            str(output_file),
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1
    assert (
        "JSON format requires a file with the .json extension"
        in result.stderr
    )
