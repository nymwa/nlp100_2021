import re
import sys
import spacy

def main():
    nlp = spacy.load('en')
    pattern = re.compile(r'\s+')
    for x in sys.stdin:
        x = x.strip()
        x = pattern.sub(' ', x)
        x = nlp.make_doc(x)
        x = ' '.join([doc.text for doc in x])
        print(x)

if __name__ == '__main__':
    main()

