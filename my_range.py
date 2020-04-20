def my_range(arg, *args):
    ####
    # This function is an implementation of range and returns a list object
    # It should (?) work everywhere where you could use similarly defined by arguments range object
    # You shouldn't use it, of course, because it is extremely memory consuming in comparison.
    # But it's a nice exercise.
    ####

    # ARGUMENTS ASSIGNMENT
    # we have one required argument (arg) and optionals (args)

    # if only one argument is passed, it is a 'stop' and start and step are default
    if len(args) == 0:
        start, stop, step = 0, arg, 1

    # if two arguments are passed, it is 'start' and 'stop', step is default
    elif len(args) == 1:
        start, stop, step = arg, args[0], 1

    # if three arguments are passed, it is 'start', 'stop' and 'step'
    # we assign these three even if there are more
    elif len(args) > 1:
        start, stop, step = arg, args[0], args[1]

    # if there are more arguments, inform user but try to continue with first 3
    if len(args) > 2:
        print("Za duża liczba argumentów w range, pierwsze 3 są brane pod uwagę.")


    # WRONG ARGUMENTS CASES

    # create a list object that we will return, if something is wrong it will be returned empty
    my_range=[]

    # do not continue if any argument is not an integer, inform user and return empty list
    if not (isinstance(start, int) and isinstance(stop, int) and isinstance(step, int)):
        print('Argumenty nie są liczbami całkowitymi.')
        return my_range

    # do not continue if assigned variables may cause infinite loop later
    # if step is 0 or step goes in wrong direction, inform user and return empty list
    if step==0 or (stop < start and step > 0) or (stop > start and step < 0):
        print('Nieprawidłowe wartości')
        return my_range

    # ACTUALL LIST CREATION

    # start iteration at start
    iterable=start

    #for positive step
    if step > 0:
        while iterable < stop:
            my_range.append(iterable)
            iterable += step

    #for negative step
    else:
        while iterable > stop:
            my_range.append(iterable)
            iterable += step

    # return proper list
    return my_range

for i in my_range(10,2):
    print(i)