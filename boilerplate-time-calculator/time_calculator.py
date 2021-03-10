from typing import NewType, Text
import math

def add_time(start, duration,day = 0):

    #split start
    start_hours,temp = start.split(':')
    start_minutes,start_ampm = temp.split(' ')
    if '0' in start_minutes[0]: 
        start_minutes = start_minutes[1]
    
    #split duration
    duration_hours,duration_minutes = duration.split(':')
    if '0' in duration_minutes[0]: 
        duration_minutes = duration_minutes[1]

    duration_minutes = int(duration_minutes)
    duration_hours = int(duration_hours)
    start_hours = int(start_hours)
    start_minutes = int(start_minutes)
 
    add_hours = 0
    new_minutes = 0
    day_count = 0
    new_hours = 0
 
    #calculate new minutes , and hours to add to total
    if (duration_minutes + start_minutes) >= 60: #has to be over 60 mins combined
        if ((duration_minutes+start_minutes) - 60) >= 0: #if over 60
            add_hours +=1 
            new_minutes = (duration_minutes+start_minutes) - 60

    elif((duration_minutes + start_minutes) < 60):
        new_minutes = duration_minutes+start_minutes
    
    add_hours += duration_hours #e.g.30 mins + 30 mins = 1hr + duration hours
    new_hours = start_hours

    for hours in range(add_hours):
        if new_hours == 12:
            new_hours = 0
            if start_ampm == "PM":
                day_count +=1
                start_ampm = "AM"
            elif(start_ampm == "AM"):
                start_ampm = "PM"
        new_hours +=1

        if new_hours == 12 and duration == 0 : #for if the hour ends on 12
            if start_ampm == "PM":
                start_ampm = "AM"
            elif(start_ampm == "AM"):
                start_ampm = "PM"
    #if at end    
    if new_hours == 12:
        if start_ampm == "PM":
            day_count +=1
            start_ampm = "AM"
        elif(start_ampm == "AM"):
            start_ampm = "PM"       

    
    new_minutes = str(new_minutes)
    
    arr_days = ['monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']

    def days_after():
        
        if day != 0:
            inputday_index = arr_days.index(day.lower())
            outputday_index = inputday_index
            for days in range(day_count):
                
                if outputday_index == 6:
                    outputday_index = 0
                else:
                    outputday_index += 1
                
            if day_count == 1: #1 day passed
                return '{} (next day)'.format((arr_days[outputday_index]).capitalize())
            elif(day_count == 0): #same day
                return ', {}'.format((arr_days[outputday_index]).capitalize())
            else: #more than 1 day
                return '({} {} days later)'.format((arr_days[outputday_index]).capitalize(), day_count)
        
        else:
            if day_count == 1:
                return '(next day)'
            elif(day_count == 0):
                return ''
            else:
                return ('{} days later').format(day_count)

    #put 0 infront of minutes if single digit
    if len(new_minutes) == 1 :
        new_minutes = '0' + new_minutes

    output = str(new_hours) + ':' + new_minutes + ' ' + start_ampm + ' ' + days_after()
    print(output)
    return output

   
