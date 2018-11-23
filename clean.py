import operator


def main():
    file = open("saol2018.csv", "r")
    file2 = open("saol2018clean.csv", "w")
    lines = file.readlines()
    unique = set()
    for line in lines:
        unique.add(line)

    sort = sorted(unique, key=lambda line: line.split(",")[1])

    for line in sort:
        file2.write(line)


if __name__ == '__main__':
    main()
