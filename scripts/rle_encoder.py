import re, shutil

rle = lambda s: re.sub(r'(.)\1*', lambda m: m[1] + str(len(m[0]) if len(m[0]) > 1 else ''), s)

fname = '../data/solutions.txt'

shutil.copy2(fname, 'solutions.txt.bak')

with open(fname) as f:
    rows = [l.split(':', 1) for l in f.read().splitlines() if l]

with open(fname, 'w') as f:
    f.writelines(f"{r[0]}:{rle(r[1])}\n" if len(r)>1 else f"{r[0]}:\n" for r in rows)

print("Done.")
