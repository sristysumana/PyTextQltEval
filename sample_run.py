from doc_quality import get_metrics, suggest_improvements

filepath = "sample_text.txt"  # Replace with your actual file
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

metrics = get_metrics(content)
suggestions = suggest_improvements(metrics)

print("=== METRIC SCORES ===")
for k, v in metrics.items():
    print(f"{k}: {v}")

print("\n=== SUGGESTIONS ===")
for s in suggestions:
    print(f"- {s}")
