import re
import sys
import spacy

def main():
    ginza = spacy.load('ja_ginza')
    pattern = re.compile(r'\s+')
    for x in sys.stdin:
        x = x.strip()
        x = pattern.sub(' ', x)
        x = ginza.make_doc(x)
        x = ' '.join([doc.text for doc in x])
        print(x)

if __name__ == '__main__':
    main()

