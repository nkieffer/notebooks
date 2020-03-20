#!/usr/bin/env python
import pathlib
from re import split
notebooks = sorted(list(pathlib.Path('.').glob('[0-9][0-9][0-9]*.ipynb')))
print(notebooks)
with open('000toc.ipynb', 'w') as toc:
    contents = []
    for f in notebooks:
        title_idx = split('[0-9]', f.name).count('')
        name = f.name[title_idx:]
        unit = f.name[:title_idx]
        link_text = name.replace(f.suffix, '').replace('_', ' ')
        link = f'"* [Unit {unit}: {link_text}]({f.name})\\n"'
        contents.append(link)
    print(contents)
    template = f"""
{{
 "cells": [
  {{
   "cell_type": "markdown",
   "metadata": {{}},
   "source": [
       "# Table of Contents\\n",
    {', '.join(contents)}
    ]
  }}
 ],
 "metadata": {{
  "kernelspec": {{
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }},
  "language_info": {{
   "codemirror_mode": {{
    "name": "ipython",
    "version": 3
   }},
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }}
 }},
 "nbformat": 4,
 "nbformat_minor": 4
}}
"""
    print(template)
    toc.write(template)