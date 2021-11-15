def write(word, *data):
    with open('./computerGraphicsLab.txt', 'a') as f:
        f.write(
            f'{word}\n Point one: ({data[0]}, {data[1]})  Point two: ({data[2]}, {data[3]})  Point three: ({data[4]}, {data[5]})\n')


if __name__ == '__main__':
    write("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", 0, 1, 2, 3, 4, 5)
