


















def get_workout(day):
    if day == 'Monday':
        return 'Chest+biceps'
    elif day == 'Tuesday':
        return 'Back+triceps'
    elif day == 'Wednesday':
        return 'Core'
    elif day == 'Thursday':
        return 'Legs'
    elif day == 'Friday':
        return 'Shoulders'
    elif day in ('Saturday', 'Sunday'):
        return 'Rest'
    raise ValueError('Not a day')




if __name__ == "__main__":

    workout = {'Monday': 'Chest+biceps', 'Tuesday' : 'Back+triceps',  'Wednesday': 'Core',
    'Thursday': 'Legs',
    'Friday': 'Shoulders',
    'Saturday': 'Rest',
    'Sunday': 'Rest'}

    def get_workout(day):
        routine  = workout.get(day, None)
        if routine is None:
            raise ValueError('Not a day')
        else:
            return routine

    print(get_workout('Monday'))

    try:
        print(get_workout('nonsense'))
    except ValueError as e:
        print(e)


    #2. Counting inside a loop

    days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()


    for i, day in enumerate(days, 1):
        print(f'{i}, {day}')

    #3 Use the with statement to deal with resources


    with open('/etc/passwd') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
        
