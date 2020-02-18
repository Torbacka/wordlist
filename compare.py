import operator


def main():
    saol13 = [l.strip() for l in open("SAOL13_117224_Ord.txt", "r", encoding="iso-8859-1").readlines()]
    saol13 = clean_saol_13(saol13)
    saol14 = set([l.split(',')[1] for l in open("saol2018clean.csv", "r").readlines()])
    output = open("removed_words.txt", "w")

    unique = set()
    for line in saol13:
        if line not in saol14:
            unique.add(line)

    sort = sorted(unique)

    output.writelines("%s\n" % line for line in sort)


def clean_saol_13(list):
    cleaned = set()
    for word in list:
        split_word = word.split(' ')
        if len(split_word) >= 2:
            try:
                int(split_word[-1])
                del split_word[-1]
            except ValueError:
                cleaned.add(split_word[0])
        elif len(split_word) > 2:
            print(f"Wired word: {word}")
        else:
            cleaned.add(word)
    return cleaned


if __name__ == '__main__':
    main()
