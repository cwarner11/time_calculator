def add_time(start, duration, day = ''):
    start1,start2 = start.split()
    hours,minutes = start1.split(':')

    duration_of_hours,duration_of_minutes = duration.split(':')

    duration_of_hours = int(duration_of_hours)
    duration_of_minutes = int(duration_of_minutes)

    hours = int(hours)
    minutes = int(minutes)

    next_day = 0
    count = 0
    
    #sets time in military time (0-23)
    if start2 == 'AM'and hours == 12:
        hours -= 12

    elif start2 == 'PM' and hours < 12:
        hours += 12
    else:
        pass

    #Minutes
    for i in range(duration_of_minutes):
        if minutes >= 59:
            minutes = 0
            hours += 1
            if hours >= 23:
                hours = 0
                next_day += 1
        else:
            minutes += 1
    #Hours
    for j in range(duration_of_hours):
        if hours >= 23:
            hours = 0
            next_day += 1
        else:
            hours += 1

    #sets AM or PM
    if hours < 12:
        start2 = 'AM'
    else:
        start2 = 'PM'

    #sets time in military time (0-23)
    if start2 == 'AM'and hours == 0:
        hours += 12

    #sets time in 12 hour format
    elif start2 == 'PM' and hours > 12:
        hours -= 12
    else:
        pass

    #format minutes to 2 digits
    minutes = str(minutes).zfill(2)
    hours = str(hours)

    # day of the week
    if day != '':
        day = day.lower()
        days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        day_index = days_of_week.index(day)

        l1 = list()
        for i in days_of_week[day_index:]:
            l1.append(i)
        
        l2 = list()
        for i in reversed(days_of_week[:day_index]):
            l2.append(i)
        
        #reverse list and store back into l2
        l2 = l2[::-1]
        
        days_of_week = l1 + l2
        
        while True:
            for new_day in days_of_week:
                if count == next_day:
                    break
                else:
                    count += 1
            break

        if next_day == 1:
            new_time = hours +':' + minutes + ' ' + start2 + ', ' + new_day.capitalize() + ' (next day)'

        elif next_day > 1:
            new_time = hours +':' + minutes + ' ' + start2 + ', ' + new_day.capitalize() + ' (' + str(next_day) + ' days later)'

        else:
            new_time = hours +':' + minutes + ' ' + start2 + ', ' + new_day.capitalize()

    else:
        if next_day == 1:
            new_time = hours +':' + minutes + ' ' + start2 + ' (next day)'

        elif next_day > 1:
            new_time = hours +':' + minutes + ' ' + start2 + ' (' + str(next_day) + ' days later)'

        else:
            new_time = hours +':' + minutes + ' ' + start2

    return new_time
