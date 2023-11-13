def histogram():
    UserValue = input('What are the values of the histogram you want to make? type in format 1,2,3 please')
    values = [int(i) for i in UserValue.split(',')]
    for i in values:
        print('*' * i)

histogram()
