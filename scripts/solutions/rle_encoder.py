from re import sub
import shutil

if __name__ == "__main__":
    rle = lambda s: sub(r'(.)\1*', lambda m: m[1] + (str(len(m[0])) if len(m[0]) > 1 else ''), s)
    shutil.copy2('solutions.csv', f'solutions.csv.bak')

    with open('solutions.csv','r') as infile:
        lines = infile.read().splitlines()
    outfile = open('solutions.csv','w')
    for line in lines:
        if line:
            name, sequence = line.split(',', 1)
            outfile.write(f"{name},{rle(sequence)}\n")

    print("Done.")
