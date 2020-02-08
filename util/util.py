def readjd():
    file = open("jd.txt")
    for line in file:
        print("\"https://item.jd.com/" + line.strip() + ".html\",")
    file.close()


def readtm():
    file = open("tm.txt")
    for line in file:
        print("\"https://detail.tmall.com/item.htm?id=" + line.strip() + "\",")
    file.close()


if __name__ == '__main__':
    readjd()
