import os
from collections import defaultdict

desktop_path = os.path.expanduser('/Users/avagyani/Desktop')

ext_counts = defaultdict(int)

for file_name in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, file_name)
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(file_name)
        if ext:
            ext_counts[ext.lower()] += 1
        else:
            ext_counts['<no_ext>'] += 1

ext_counts = dict(ext_counts)

print(ext_counts)
