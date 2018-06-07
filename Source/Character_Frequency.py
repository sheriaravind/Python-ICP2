def Write_Data(msg):
    with open(r'C:\Users\aravi\OneDrive\Desktop\Output.txt', 'a') as out_data:
        out_data.write(msg)


def Read_Data():
    with open(r'C:\Users\aravi\OneDrive\Desktop\Sample.txt', 'r') as input_data:
        for line in input_data:
            line = line.strip()
            Write_Data("{0} {1} \n".format(line,len(line)))


if __name__ == '__main__':
    Read_Data()

