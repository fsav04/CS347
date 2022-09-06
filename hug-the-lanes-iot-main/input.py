import random


#Max BAC, so check if under .08 INT#
BACMAX = .08
#BAC of breath sensor#
BAC = round(random.uniform(0.0, 0.21), 2)

#Current Driver ID STRING#
TID = random.choice(["User", "Invalid"]) 
VID = random.choice(["User", "Invalid"])

#Not sure what the input would be VOID (for now)#
VA = random.choice(["void", "command"])

#True when sensor detects severe crash#
SCS = random.choice([True, False])

#True when there are no obstacles and parking space is big enough#
AutoPark = random.choice([True, False])

#True if driver summons vehicle, if true the car will drive to the driver#
VS = random.choice([True, False])

#Light levels range from 0-2000, NV will turn on if below 500
NV = random.randint(0, 2000)

#Captain's Chairs will rotate if doors are open and no obstacle
CC = random.choice([True, False])

#True if an obstacle is detected in blindspot
LD = random.choice([True,False])

isCarOn = True
