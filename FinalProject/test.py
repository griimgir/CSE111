def classesTable(num_rows, num_cols):
    # data = open('output/classes/')

    output1 = open('output/classes/class.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/classes/classnumber.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/classes/total.txt', 'r')
    o3 = output3.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i+1], o2[i+1], o3[i+1]]
        print(data[i])
        i = i + 1
    
    return True


def main():
    classesTable(num_rows=5, num_cols=3)

main()




    output1 = open('output/backpacks/.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/backpacks/.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/backpacks/.txt', 'r')
    o3 = output3.readlines()

    output4 = open('output/backpacks/.txt', 'r')
    o4 = output4.readlines()

    output5 = open('output/backpacks/.txt', 'r')
    o5 = output5.readlines()

    output6 = open('output/backpacks/.txt', 'r')
    o6 = output6.readlines()

    output7 = open('output/backpacks/.txt', 'r')
    o7 = output7.readlines()

    output8 = open('output/backpacks/.txt', 'r')
    o8 = output8.readlines()

    output9 = open('output/backpacks/.txt', 'r')
    o9 = output9.readlines()


[o1[i], o2[i], o3[i], o4[i], o5[i], o6[i], o7[i], o8[i], o9[i], o10[i]]




    def Table(num_rows, num_cols):

    output1 = open('output/backpacks/.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/backpacks/.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/backpacks/.txt', 'r')
    o3 = output3.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i]]
        # print(data[i])
        i = i + 1
    return data