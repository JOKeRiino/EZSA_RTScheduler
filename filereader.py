def readfile(filename):
    # read data from file
    f = open(filename, 'r')
    data = []
    for line in f.readlines():
        task = []
        # for each comma-separated value in the string (with linebreaks removed)
        for index in line.replace("\n", "").split(","):
            if index.isnumeric():
                # if it's a number cast it into an int
                task.append(int(index))
            else:
                # else just append to task array
                task.append(index)
        # add every line to one array
        data.append(task)
    # print(data)
    return data
