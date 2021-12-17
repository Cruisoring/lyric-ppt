#!/usr/bin/env python

import os.path
from pathlib import Path
from opencc import OpenCC

cc = OpenCC('s2t')


LYRIC_TYPES = ('*.md')
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))


def locate_file(file_path: str):
    matches = []
    for ext in LYRIC_TYPES:
        matches.extend(list(Path('.').rglob(ext)))
    matches = [f for f in matches if file_path in str(f)]
    return str(matches[0])


def all_lines(file_path: str):
    file_path = locate_file(file_path)
    with open(file_path, 'r', encoding='utf-8') as fid:
        lines = [cc.convert(line) for line in fid.readlines()]
        if (lines[-1].strip):
            lines.append('\n')
        return lines


if __name__ == '__main__':
    lines = all_lines('耶和華神已掌權')

    for line in lines:
        print(line)
