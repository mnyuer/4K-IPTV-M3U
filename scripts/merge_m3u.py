#!/usr/bin/env python3
"""Merge all province M3U files by ISP."""
import glob, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def merge_files(pattern, output):
    files = sorted(glob.glob(pattern))
    if not files:
        print(f'No files matching {pattern}')
        return
    first = True
    total = 0
    with open(output, 'w', encoding='utf-8') as out:
        for fpath in files:
            with open(fpath, 'r', encoding='utf-8') as f:
                for line in f:
                    s = line.strip()
                    if not s:
                        continue
                    if s.startswith('#EXTM3U'):
                        if first:
                            out.write(s + '\n')
                            first = False
                    else:
                        out.write(s + '\n')
                        total += 1
    lines = total + 1
    print(f'{output}: {lines} lines, {total} channels')

merge_files('m3u/*.m3u', 'iptv.m3u')
merge_files('m3u/*电信*.m3u', 'iptv_telecom.m3u')
merge_files('m3u/*联通*.m3u', 'iptv_unicom.m3u')
