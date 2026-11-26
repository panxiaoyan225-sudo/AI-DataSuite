import json

NOTEBOOK_PATH = r"C:\Python\AI-DataSuite\Data-to-Narrative-Pipelines\Compute-Then-Communicate_Expense.ipynb"

with open(NOTEBOOK_PATH, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Find the Excel cell and fix the dim_month column selection
for i, cell in enumerate(nb["cells"]):
    if cell.get("cell_type") == "code":
        source = "".join(cell.get("source", []))
        if 'dim_month = dim_month[["Month Key","Reporting Month","Fiscal Year"]]' in source:
            print(f"Found Excel cell at index {i}")
            source = source.replace(
                'dim_month = dim_month[["Month Key","Reporting Month","Fiscal Year"]]',
                'dim_month = dim_month[["Month Key","Month Sort","Reporting Month","Fiscal Year"]]'
            )
            cell["source"] = source.splitlines(keepends=True)
            cell["execution_count"] = None
            cell["outputs"] = []
            print(f"Cell {i} fixed")
            break

with open(NOTEBOOK_PATH, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook saved.")