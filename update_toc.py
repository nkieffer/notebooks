#!/usr/bin/env python
import pathlib
from re import split

notebooks = sorted(pathlib.Path('.').glob('{3}[0-9]*.ipynb'))

with open('ToC.md', 'w') as toc:
    for f in notebooks:
        title_idx = split('[0-9]', f.name).count('')
        name = f.name[title_idx:]
        unit = f.name[:title_idx]
        link_text = name.replace(f.suffix, '').replace('_', ' ')
        toc.write(f"* [Unit {unit}: {link_text}]({name})\n")
    

