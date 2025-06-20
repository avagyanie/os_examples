import matplotlib.pyplot as plt

# Example dictionary from your script
ext_counts = {'.txt':    5, '.pdf': 3, '.py': 2, '<no_ext>': 1}

# Create bar chart
plt.figure(figsize=(8   , 5))
plt.bar(ext_counts.keys(), ext_counts.values(), color='skyblue')
plt.title('File Count per Extension on Desktop')
plt.xlabel('File Extension')
plt.ylabel('Count')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
