from parsers.csv_parser import parse_csv_file


def test_parse_csv_file(tmp_path):
    csv_content = (
        "id,email,name,department,hours_worked,salary\n"
        "1,alice@example.com,Alice,Marketing,160,50"
    )
    file_path = tmp_path / "test.csv"
    file_path.write_text(csv_content)
    data = parse_csv_file(str(file_path))
    assert len(data) == 1
    assert data[0]["hourly_rate"] == "50"
