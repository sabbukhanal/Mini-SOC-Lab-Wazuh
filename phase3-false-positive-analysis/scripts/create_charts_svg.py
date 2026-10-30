import csv
from pathlib import Path

base = Path(__file__).resolve().parent.parent
source = base / "datasets" / "experiment_results.csv"
reports = base / "reports"
reports.mkdir(parents=True, exist_ok=True)

with source.open(newline="", encoding="utf-8") as file:
    cases = [
        row for row in csv.DictReader(file)
        if row["in_scope"] == "1"
    ]

tp = fp = fn = tn = 0

for case in cases:
    malicious = int(case["malicious"])
    alerted = int(case["rule_100100"])

    if malicious and alerted:
        tp += 1
    elif not malicious and alerted:
        fp += 1
    elif malicious and not alerted:
        fn += 1
    else:
        tn += 1

def rate(n, d):
    return 100 * n / d if d else None

metrics = [
    ("Precision", rate(tp, tp + fp)),
    ("Recall", rate(tp, tp + fn)),
    ("False-positive rate", rate(fp, fp + tn)),
]

bars = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="760" height="480" viewBox="0 0 760 480">',
    '<rect width="760" height="480" fill="#ffffff"/>',
    '<text x="380" y="52" text-anchor="middle" font-size="25" font-family="sans-serif">Wazuh rule 100100: Detection metrics</text>',
    '<line x1="85" y1="355" x2="705" y2="355" stroke="#333" stroke-width="2"/>'
]

for i, (label, value) in enumerate(metrics):
    x = 132 + 203 * i
    height = (value or 0) * 2.35

    bars.append(
        f'<rect x="{x}" y="{355-height:.1f}" '
        f'width="110" height="{height:.1f}" fill="#3274a1"/>'
    )

    value_label = f"{value:.1f}%" if value is not None else "N/A"

    bars.append(
        f'<text x="{x+55}" y="{342-height:.1f}" '
        f'text-anchor="middle" font-size="19" font-family="sans-serif">'
        f'{value_label}</text>'
    )

    bars.append(
        f'<text x="{x+55}" y="391" text-anchor="middle" '
        f'font-size="15" font-family="sans-serif">{label}</text>'
    )

bars.append(
    f'<text x="380" y="442" text-anchor="middle" '
    f'font-size="14" font-family="sans-serif">'
    f'{len(cases)} in-scope synthetic scenarios; not production performance</text>'
)
bars.append("</svg>")

(reports / "detection_metrics.svg").write_text(
    "\n".join(bars), encoding="utf-8"
)

cells = [
    [("TN", tn), ("FP", fp)],
    [("FN", fn), ("TP", tp)]
]

chart = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="720" height="470" viewBox="0 0 720 470">',
    '<rect width="720" height="470" fill="white"/>',
    '<text x="360" y="48" text-anchor="middle" font-size="25" font-family="sans-serif">Wazuh rule 100100: Confusion matrix</text>',
    '<text x="325" y="100" text-anchor="middle" font-size="16" font-family="sans-serif">No custom alert</text>',
    '<text x="535" y="100" text-anchor="middle" font-size="16" font-family="sans-serif">Custom alert</text>'
]

for row, row_name in enumerate(("Benign", "Malicious")):
    y = 120 + 125 * row

    chart.append(
        f'<text x="130" y="{y+69}" text-anchor="middle" '
        f'font-size="17" font-family="sans-serif">{row_name}</text>'
    )

    for col, (kind, count) in enumerate(cells[row]):
        x = 225 + col * 210

        chart.append(
            f'<rect x="{x}" y="{y}" width="200" height="115" '
            f'fill="#e0edf6" stroke="#64748b"/>'
        )

        chart.append(
            f'<text x="{x+100}" y="{y+51}" text-anchor="middle" '
            f'font-size="22" font-family="sans-serif">{kind}</text>'
        )

        chart.append(
            f'<text x="{x+100}" y="{y+84}" text-anchor="middle" '
            f'font-size="29" font-family="sans-serif">{count}</text>'
        )

chart.append(
    f'<text x="360" y="426" text-anchor="middle" '
    f'font-size="14" font-family="sans-serif">'
    f'{len(cases)} in-scope synthetic scenarios; not production performance</text>'
)
chart.append("</svg>")

(reports / "confusion_matrix.svg").write_text(
    "\n".join(chart), encoding="utf-8"
)

print(f"In-scope tests: {len(cases)} | TP={tp}, FP={fp}, FN={fn}, TN={tn}")
print("Created:", reports / "detection_metrics.svg")
print("Created:", reports / "confusion_matrix.svg")
