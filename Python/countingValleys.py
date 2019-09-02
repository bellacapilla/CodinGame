"""
Counts the number of valleys crossed in a hike.

Input: 
Array s = [UDDDUDUU], where D is downhill and U is uphill
        _/\      _
           \    /
            \/\/

Starting point is at level see and a valley is counted when a level 
below the see level is reached and returned to see level.
"""

# Complete the countingValleys function below.
def countingValleys(s):
    level = 0
    valleys = 0
    startedValley = 0

    # Check min constrain
    if len(s) >= 2:

        for step in range(0, len(s)):

            # If downhill substracts 1
            if s[step] == 'D':
                level -= 1
                
                # If getting below see level, starts a valley
                if (level < 0 and startedValley == 0):
                    startedValley = 1 # register start of valley
                   
                # If see level was reached and a valley was started, count valley
                elif level == 0 and startedValley == 1:
                    valleys += 1
                    startedValley = 0 # reset valley start
            
            # If uphill adds 1 
            else:
                level += 1

                # If see level reached, count valey and reset valley start
                if level == 0 and startedValley == 1:
                    valleys += 1      
                    startedValley = 0

        return valleys

    else:
        return valleys



