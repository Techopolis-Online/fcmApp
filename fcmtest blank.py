from pyfcm import FCMNotification
import cgi

form = cgi.FieldStorage()

def push_to_topic(topic, title, body, sound):
    # todo: remove API key and ask user for input.
    push_service = FCMNotification(api_key="AAAA_EcosCc:APA91bFQpUawMdkkZ0UHdOpJouwFRmmC9FUJFecfAM62_1sVxdpYEKrAYJODnbEAQ4vOJdBJUzw0A30w7MLu80dom6UQzOGaT-8dwu7u4CasDLCLmtPS3-pCcY8NUHU9Ykk66uIJPl3p")
    result = push_service.notify_topic_subscribers(topic_name=topic, message_body=body, message_title=title, sound=sound)
    return result

def main():
    # todo: get title from user
    title = ""
    # todo: get top from user
    topic = "commtech"
    #todo: get body from user
    body = ""

    sound = "default"
    # todo: get sound from user
    result = push_to_topic(sound=sound, topic=topic, body=body, title=title)
    # todo: make submit button
    print(result)
# todo: display the result to user in text control

if __name__ == "__main__":
    main()
