def write_file(input_name: str, data: []) -> None:
    with open(input_name, 'w') as file:
        for line in data:
            file.write(data[line])


def read_file(input_name: str) -> []:
    with open(input_name) as file:
        tmp = file.read().split('\n')
        data = [(line.split()) for line in tmp]
    return data


def find(data: [], x: int) -> []:
    res = {}
    res[0] = str(x)
    for i in range(1, int(data[0][0])+1):
        inv = 0
        for j in range(int(data[0][0])):
            for k in range(j+1, int(data[0][1])):
                if data[x][j] > data[i][k]:
                    inv += 1
        res[i] = '\n' + str(i) + ' ' + str(inv)

    return res


def main():
    x = int(input())
    input_name = 'files/input2.txt'
    output_name = 'files/output.txt'
    inp = read_file(input_name)
    data = find(inp, x)
    write_file(output_name, data)


if __name__ == '__main__':
    main()
