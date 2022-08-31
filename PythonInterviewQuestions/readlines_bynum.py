def read_n(filename, n):
    f = open(filename)

    while True:
        one_section = ''.join(f.readline() for l in range(n))
        if one_section:
            yield one_section
        else:
            break


for each_section in read_n('currents_news.json', 5):
    print(each_section)
