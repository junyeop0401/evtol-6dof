from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SI_DIR = ROOT / "logs" / "csv" / "si"


def read_rows(path: Path) -> list[dict[str, float]]:
    with path.open(newline="", encoding="utf-8") as src:
        return [
            {key: float(value) for key, value in row.items()}
            for row in csv.DictReader(src)
        ]


def main() -> None:
    validated = read_rows(SI_DIR / "ball_validated_si.csv")
    builtin = read_rows(SI_DIR / "ball_builtin_si.csv")
    columns = [
        "altitude_m",
        "local_D_m",
        "lat_deg",
        "lon_deg",
        "v_n_mps",
        "v_e_mps",
        "v_d_mps",
        "v_total_mps",
        "mass_kg",
        "ixx_kg_m2",
    ]

    output_path = SI_DIR / "ball_validated_vs_builtin_summary_si.csv"
    with output_path.open("w", newline="", encoding="utf-8") as dst:
        writer = csv.DictWriter(
            dst,
            fieldnames=["column", "max_abs_delta_validated_minus_builtin"],
        )
        writer.writeheader()
        for column in columns:
            max_abs_delta = max(
                abs(left[column] - right[column])
                for left, right in zip(validated, builtin)
            )
            writer.writerow(
                {
                    "column": column,
                    "max_abs_delta_validated_minus_builtin": max_abs_delta,
                }
            )

    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
