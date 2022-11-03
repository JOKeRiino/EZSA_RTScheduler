def format_output_as_gant(outputdata, filedata):
    print("\nGant Chart:")
    # get longest task name:
    maxlen = 0
    for name in filedata:
        if len(name[0]) > maxlen:
            maxlen = len(name[0])

    for task in filedata:
        gant_string = []
        for val in outputdata:
            if val == task[0]:
                gant_string.append("█")
            else:
                gant_string.append("░")

        print(f'{task[0]:^{maxlen}} |{"".join(gant_string)[0:200]}')

    return True
