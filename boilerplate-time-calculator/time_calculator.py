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
    arr_days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

    #calculate new minutes , and hours to add to total

    if (duration_minutes + start_minutes) >= 60: #has to be over 60 mins combined
        if ((duration_minutes+start_minutes) - 60) >= 0: #if over 60
            add_hours +=1 
            new_minutes = (duration_minutes+start_minutes) - 60 #(75) -60 = 15 mins left

    elif((duration_minutes + start_minutes) < 60):
        new_minutes = duration_minutes+start_minutes
    
    add_hours += duration_hours #e.g.30 mins + 30 mins = 1hr + duration hours

   
    #if hours are longer than 1 day that are input
    # if add_hours >= 24   :    
    #     day_count += math.floor(add_hours / 24)
    #     #print('add hours before = ',add_hours)
    #     add_hours = add_hours % 24 
    #     #print('add hours after % 24= ',add_hours)

    
    #to addhours is total minutes and hours to add , the days count variable just changes the day in the array

    new_hours = start_hours
    #print('new hours',new_hours)

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
    
    # if day_count != 0:
    #     day_count += 1
    
    
    
    #print('daycount = ',day_count)
    
    new_minutes = str(new_minutes)

   
    def days_after():
        if day_count == 1:
            return '(next day)'
        elif(day_count == 0):
            return ''
        else:
            return '({} days later)'.format(day_count)


    if len(new_minutes) == 1 :
        new_minutes = '0' + new_minutes

    if day != 0:
        #day_value = day.lower()
        day_index = arr_days.index(day.lower())
        print(day_index)
        
        for days in range(day_count):
            pass

    else:
        output = str(new_hours) + ':' + new_minutes + ' ' + start_ampm + ' ' + days_after()
        print(output)
        return output

   
    


add_time("3:30 PM", "2:12",'monday')
#expected = "5:42 PM"

  
add_time("11:55 AM", "3:12")
#expected = "3:07 PM"

add_time("9:15 PM", "5:30")
#expected = "2:45 AM (next day)"


add_time("11:40 AM", "0:25")
##expected = "12:05 PM"

add_time("2:59 AM", "24:00")
#expected = "2:59 AM (next day)"

add_time("11:59 PM", "24:05")
#expected = "12:04 AM (2 days later)"

add_time("8:16 PM", "466:02")
#expected = "6:18 AM (20 days later)"
add_time("5:01 AM", "0:00")
#expected = "5:01 AM"


add_time("3:30 PM", "2:12", "Monday")
#expected = "5:42 PM, Monday"


add_time("2:59 AM", "24:00", "saturDay")
#expected = "2:59 AM, Sunday (next day)"


add_time("11:59 PM", "24:05", "Wednesday")
#expected = "12:04 AM, Friday (2 days later)"

add_time("8:16 PM", "466:02", "tuesday")
#expected = "6:18 AM, Monday (20 days later)"
