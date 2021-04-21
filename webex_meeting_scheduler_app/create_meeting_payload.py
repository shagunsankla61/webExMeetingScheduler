import requests


def create_meeting(payload):

    url = "https://api.webex.com/WBXService/XMLService"
    headers = {
        'cache-control': "no-cache"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.status_code, response.text


payload = """<?xml version="1.0" encoding="UTF-8"?>
<serv:message xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <header>
        <securityContext>
            <siteName>apidemoeu</siteName>
            <webExID>user_name_api_credentials</webExID>
            <password>api_password</password> 
        </securityContext>
    </header>
    <body>
        <bodyContent
            xsi:type="java:com.webex.service.binding.meeting.CreateMeeting">
            <accessControl>
                <meetingPassword>{meeting_password}</meetingPassword>
            </accessControl>
            <metaData>
                <confName>{conf_name}</confName>
                <meetingType>{meeting_type}</meetingType>
                <agenda>{agenda}</agenda>
            </metaData>
            <participants>
                <maxUserNumber>{max_user}</maxUserNumber>
                <attendees>
                    {attendees}
                </attendees>
            </participants>
            <enableOptions>
                <chat>{chat}</chat>
                <poll>{poll}</poll>
                <audioVideo>{auto_video}</audioVideo>
                <supportE2E>{support}</supportE2E>
                <autoRecord>{auto_record}</autoRecord>
            </enableOptions>
            <schedule>
                <startDate>{start_date}</startDate>
                <openTime>{open_time}</openTime>
                <joinTeleconfBeforeHost>{join_teleconf}</joinTeleconfBeforeHost>
                <duration>{duration}</duration>
                <timeZoneID>{time_zone_id}</timeZoneID>
            </schedule>
            <telephony>
                <telephonySupport>CALLIN</telephonySupport>
                <extTelephonyDescription>
                    {phone_number}
                </extTelephonyDescription>
            </telephony>
        </bodyContent>
    </body>
</serv:message>
"""


attendees = """<attendee>
                    <person>
                        <name>{attendee_name}</name>
                        <email>{attendee_email}</email>
                    </person>
                </attendee>
                """