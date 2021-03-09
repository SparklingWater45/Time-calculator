from typing import Text


def add_time(start, duration):
    
    #split start
    start_hours,temp = start.split(':')
    start_minutes,start_ampm = temp.split(' ')
    if '0' in start_minutes[0]: 
        start_minutes = start_minutes[1]
    
    #split duration
    duration_hours,duration_minutes = duration.split(':')
    if '0' in duration_minutes[0]: 
        duration_minutes = duration_minutes[1]


    add_hours = 0
    new_minutes = 0
    ampm = start_ampm
    day_count = 0
    new_hours = 0


    #calculate hours added 
    
    #change all to int for calculations
    duration_minutes = int(duration_minutes)
    duration_hours = int(duration_hours)
    start_hours = int(start_hours)
    start_minutes = int(start_minutes)

    #calculate new minutes , and hours to add to total
    if (duration_minutes + start_minutes) > 60: #has to be over 1 hr
        if ((duration_minutes+start_minutes) - 60) >= 0: #if over 61
            add_hours += 1
            new_minutes = (duration_minutes+start_minutes) - 60 #(75) -60 = 15 mins left
    elif((duration_minutes + start_minutes) < 60):
        new_minutes = duration_minutes+start_minutes
    
    add_hours += duration_hours
    add_hours += start_hours

    new_hours = 0


        
    if new_hours % 12 == 0:
        if ampm == 'PM':
            ampm = 'AM'
            day_count += 1
        elif ampm == 'AM':
            ampm = 'PM'
   
        
        




    '''
    input (11:00 PM , 2:00) -> 1:00 AM
    if new_hours = 12, then remaining duration = new_hours, forloop for if over e.g. 24 hours inputted. 
    First determine , minutes_Start + minutes_duration, if over 60 remainder = new minutes , (max could ...)
    '''
    return ''



print(add_time("1:59 PM", "1:59"))   