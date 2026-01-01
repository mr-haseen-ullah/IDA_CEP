import nbformat

# Read the executed notebook
with open('analysis_executed.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

total_cells = len(nb.cells)
code_cells = sum(1 for c in nb.cells if c.cell_type == 'code')
markdown_cells = sum(1 for c in nb.cells if c.cell_type == 'markdown')

# Check for errors
errors = []
for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'code' and cell.get('outputs'):
        for output in cell.outputs:
            if 'ename' in output:
                errors.append((i, output.get('ename'), output.get('evalue')))

print(f"Notebook Execution Report")
print("=" * 60)
print(f"Total cells: {total_cells}")
print(f"Code cells: {code_cells}")
print(f"Markdown cells: {markdown_cells}")
print(f"Cells with errors: {len(errors)}")
print()

if errors:
    print("Errors found:")
    for cell_num, error_name, error_val in errors:
        print(f"  Cell {cell_num}: {error_name} - {error_val}")
else:
    print("[OK] All cells executed successfully!")
    print("[OK] No errors detected!")

    
# Check for visualizations
import os
viz_files = [
    'histogram_analysis.png',
    'boxplot_analysis.png',
    'condition_analysis.png',
    'gender_analysis.png',
    'admission_type_analysis.png',
    'qq_plots.png',
    'probability_distribution.png',
    'correlation_matrix.png'
]

print()
print("Visualization Files Generated:")
print("-" * 60)
for viz in viz_files:
    if os.path.exists(viz):
        size_kb = os.path.getsize(viz) / 1024
        print(f"  [OK] {viz:35s} ({size_kb:.1f} KB)")
    else:
        print(f"  [MISSING] {viz:35s} (NOT FOUND)")

