def Read_Data():
    data = {}
    with open(r'C:\Users\aravi\OneDrive\Desktop\Sample.txt', 'r') as input_data:
        for line in input_data:
            data1 = line.strip()
            lenght = len(line.strip('\n').split())
            data[data1] = lenght

    for k,v in data.items():
        print(k,v)

    print(data)

if __name__ == '__main__':
    Read_Data()