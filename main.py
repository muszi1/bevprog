def main():
    oldal = input("Oldalak: ")
    oldalList = []
    li = oldal.split(",")
    for i in li:
        x = i.split("-")
        if len(x) > 1:
            for j in range(int(x[0]), int(x[1]) + 1):
                oldalList.append(j)
        else:
            if len(i) >= 1:
                oldalList.append(int(i))

    print(oldalList)


if __name__ == "__main__":
    main()