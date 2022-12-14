def main():
    li = [2, 4, 8, 3, 9, 7, 1]

    kul = []
    for i in range(len(li) - 1):
        if li[i] > li[i + 1]:
            kul.append(int(li[i]) - int(li[i + 1]))

        if li[i] < li[i + 1]:
            kul.append(int(li[i + 1]) - int(li[i]))

        if li[i] > li[i + 1]:
            kul.append(0)

    szum = 0
    for i in range(len(kul)):
        szum += kul[i]

    print(szum)

    li = []
    root = str(2 ^ 1024)
    for i in range(len(root)):
        li.append(root[i])

    kul = []
    for i in range(len(li) - 1):
        if li[i] > li[i + 1]:
            kul.append(int(li[i]) - int(li[i + 1]))

        if li[i] < li[i + 1]:
            kul.append(int(li[i + 1]) - int(li[i]))

        if li[i] > li[i + 1]:
            kul.append(0)

    szum = 0
    for i in range(len(kul)):
        szum += kul[i]

    print(szum)


if __name__ == "__main__":
    main()