from typing import Text


def add_time(start, duration):
    
    #split start
    hours_start,temp = start.split(':')
    minutes_start,ampm_start = temp.split(' ')
    if '0' in minutes_start[0]: 
        minutes_start = minutes_start[1]
    
    #split duration
    hours_duration,minutes_duration = duration.split(':')
    if '0' in minutes_duration[0]: 
        minutes_duration = minutes_duration[1]


    
        
    


   

    # print('start hours->',hours_start)
    # print('start minutes->',minutes_start)
    # print('start ampm->',ampm_start)
    # print('duration hours->',hours_duration)
    # print('duration minutes->',minutes_duration)
    return ''



print(add_time("11:06 PM", "2:02"))   