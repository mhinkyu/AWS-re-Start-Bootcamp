import re # regular expression


def main():
    text =  """Python is powerful... and fast
plays well with others
runs everywhere
is friendly & easy to learn
is Open
These are some of the reasons people who use Python would rather not use anything else"""

    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    words = list(text.split())
    ls = []
    for i in words:
        if i not in ls:
            ls.append(i)
    print(ls)
main()

