import input
import json

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

path = './'
fileName = 'log'


def read():
    data = {}
    if (input.isCarOn == True):
        if (input.BAC <= input.BACMAX):
             #if it is true the car will start
            data['BACcheck'] = 'True'
        else:
            #if it is false the car will not start and the BAC levels are displayed
            data['BACcheck'] = 'False'
        if (input.TID == "User"):
    #If it is true then the fingerprint is recognized and user profile is displayed on screen
            data['TouchID'] = 'True'
        else:
    #If it is false then vehile will deny access and prompt driver to create a profile
            data['TouchID'] = 'False'

        if (input.VID == "User"):
    #If it is true then the fingerprint is recognized and user profile is displayed on screen
            data['VoiceID'] = 'True'
        else:
    #If it is false then vehile will deny access and prompt driver to create a profile
            data['VoiceID'] = 'False'    

        if (input.VA != "void"):
    #If true task is processed can be performed
            data['VA'] = 'True'
        else:
    #If false, either voiced was not recognized or task cannot be performed
            data['VA'] = 'False'

        if (input.SCS == True):
    #If true, collision detected, notifies 911
            data['SCS'] =  'True'
        else:
    #no collision detected
            data['SCS'] = 'False'

        if (input.AutoPark == True):
    #If true, no obstacle detected and parking space is big enough, initiate parking
            data['AutoPark'] = 'True'
        else:
    #if False, obstacle or not enough space, display to the driver to find another parking spot
            data['AutoPark'] = 'False'

        if (input.VS == True):
    #if True, Vehicle has been summoned, calulate safe route to the driver
            data['Summoning'] = 'True'
        else:
    #if False, Vehicle stays in place
            data['Summoning'] = 'False'
    
        if (input.NV < 500):
    #if True, Camera's night vision activated
            data['Cameras'] = 'True'
        else:
    #if False, there is enough light and night vision is not needed
            data['Cameras'] = 'False'

        if (input.CC == True):
    #if True, no obstacle detected, chairs will rotate
            data['Chairs'] = 'True'
        else:
    # obstacle detected, display to driver that there is an obstacle cannot rotate
            data['Chairs'] = 'False'
    
        if (input.LD == True):
    #If true, object is in blindspot, blindspot light turns on
            data['LaneDetection'] = 'True'
        else: 
    #No obstacle in blindspot, light is off
            data['LaneDetection'] = 'False'
        return data
    else:
        return data


writeToJSONFile(path, fileName, read())
