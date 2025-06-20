import os
from collections import defaultdict

desktop_path = os.path.expanduser('/Users/avagyani/Desktop')

ext_sizes = defaultdict(int)

for file_name in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, file_name)
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(file_name)
        size = os.path.getsize(file_path)
        if ext:
            ext_sizes[ext.lower()] += size
        else:
            ext_sizes['<no_ext>'] += size

ext_sizes = dict(ext_sizes)

for ext, size in ext_sizes.items():
    print(f"{ext}: {size / 1024:.2f} KB")
