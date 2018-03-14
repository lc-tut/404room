import os
import datetime

def slack():

    ### Get Current Time
    now = datetime.datetime.now()
    nowDate = str(now.year) + '/' + str(now.month)  + '/' + str(now.day)
    nowTime = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)

    ### Post to Slack
    TOKEN   = '12345'
    USER    = 'DoorBot'
    CHANNEL = 'door-sensor'
    MESSAGE = 'The door was opened at ' + nowDate + ' ' + nowTime

    os.system('curl -s -XPOST -d token="' + TOKEN + '" -d channel="#' + CHANNEL + '" -d text="' + MESSAGE + '" -d username="' + USER + '" https://slack.com/api/chat.postMessage')
