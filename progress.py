import sys
from tqdm import tqdm

def main():
    for x in tqdm(sys.stdin):
        print(x, end='')

if __name__ == '__main__':
    main()

