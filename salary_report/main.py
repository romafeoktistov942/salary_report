import os
import argparse
import sys
from typing import Optional
from parsers.csv_parser import parse_csv_files
from reports import get_report


def validate_output_format(output: Optional[str], report_format: str) -> None:
    if not output:
        return

    extension = os.path.splitext(output)[1].lower()
    if report_format == "json" and extension != ".json":
        raise ValueError(
            "For JSON report format, a file with "
            "the .json extension is required"
        )
    elif report_format == "text" and extension not in (".txt", ".text"):
        raise ValueError(
            "For text report format, a file with the .txt "
            "or .text extension is required"
        )


def parse_args(args=None):
    parser = argparse.ArgumentParser(description="Salary Report Generator")
    parser.add_argument("files", nargs="+", help="Path to CSV files")
    parser.add_argument(
        "--report",
        required=True,
        help="Type of report to generate",
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Format of the report (default: text)",
    )

    parser.add_argument(
        "--output",
        help="File to save the report to. If not specified, print to stdout",
    )

    args = parser.parse_args(args)

    if args.report not in ["payout"]:
        raise ValueError("Unknown report")
    return args


def main():
    try:
        args = parse_args()
        validate_output_format(args.output, args.format)

        data = parse_csv_files(args.files)
        report = get_report(args.report)
        output = report(data, format=args.format)

        if args.output:
            with open(args.output, "w") as f:
                f.write(output)
        else:
            print(output)

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
