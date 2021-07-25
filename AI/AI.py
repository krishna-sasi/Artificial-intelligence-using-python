import os
import datetime
import speech_recognition as sr
from os import system
from playsound import playsound
import webbrowser
from wikipedia import wikipedia
import pyttsx3
import imaplib
import email
from email.header import decode_header
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

engine = pyttsx3.init()

number = { "neel" : 9033993649,
           "hetal" : 8154993650,
           "chirag" : 9723410008,
           "bhavik" : 7435016794,
           "suncity" : 9879314347,
           "harsh" : 7487830407,
           "hitendra" : 8866130697,
           "milan" : 9510153616
    }

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    mymsg = MIMEMultipart()
    mymsg['From'] = 'neelbhatt783@gmail.com'
    mymsg['To'] = to
    mymsg['Subject'] = subject
    body = content
    mymsg.attach(MIMEText(body, 'plain'))
    text = mymsg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('neelbhatt783@gmail.com', '9033993649')
    server.sendmail('neelbhatt783@gmail.com', to, text)
    server.close()


if __name__ == "__main__":
    # while True:
    if 1:
        query = takeCommand().lower()


        if 'wikipedia' in query:
            system('say Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            system('say According to Wikipedia')
            print(results)
            engine.say(results)
            engine.runAndWait()

        elif 'open youtube' in query:
            system('say Opening YouTube')
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            system('say Opening Google')

        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com")
            system('say Opening stackoverflow')

        elif 'play psycho' in query:
            webbrowser.open("https://www.youtube.com/watch?v=G81Ospnlctw")
            system('say Opening psycho song')

        elif 'open maru sahitya' in query:
            webbrowser.open("http://marusahitya.com")

        elif 'do you know satish pandit' in query:
            print("Satish Pandit is Gujarati Book Writer And He Uploded Around Seven Books Also He Has One Website Wich Name Is marusahitya.com")
            system('say Satish Pandit ".." is "." Gujarati "." Book Writer "." And He Uploded "." Around ".." Seven "." Books "." Also He Has "." One "." Website Wich Name Is ".."maru "." sahitya dot com')
        elif 'what is your name' in query:
            print('I am Your Assistant Neel Bhatt And Now I am In Vavol Gandhinagar')
            system('say I am Your Assistant Neel Bhatt And Now I am In Vavol Gandhinagar')

        elif 'do you know hetal' in query:
            system('say Hetal Bhatt "." Is "." Neels "." mother "." And "." She Is 40 years Old')

        elif 'play music' in query:
            music_dir = '/Users/neelbhatt/Favoraite_Music'
            songs = os.listdir(music_dir)
            print(songs)
            ln = len(songs)
            last = ln-1
            num = random.randint(1, last)
            print("Last Number According to len function : ",ln)
            print("Last Number According - 1 : ", last)
            print("Random Number Genrator : ",num)

            playsound(os.path.join(music_dir ,songs[num]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            engine.say("Sir, the time is " + strTime)
            engine.runAndWait()

        elif 'open code' in query:
            codePath = "open /Applications/Visual\ Studio\ Code.app"
            os.system(codePath)

        elif 'open whatsapp' in query:
            codePath = "open /Applications/Whatsapp.app"
            os.system(codePath)

        elif 'send email' in query:
            try:
                system("say What should Your Email Subject?")
                subject = takeCommand()
                system("say What should I say?")
                content = takeCommand()
                to = "neelbhatt784@gmail.com"
                sendEmail(to, content)
                system("say Email has been sent!")
            except Exception as e:
                print(e)
                system("say Sorry my friend Neel. I am not able to send this email")

        elif 'send a whatsapp' in query:

            system('say Who Do you Want "." to masaage "." sir ?')

            numb = takeCommand().lower()

            num = number.get(numb)

            system('say Whats The Massage sir ?')

            msg = takeCommand()

            system('say Please Click the sent Button in your Whatsapp App')

            url = 'https://wa.me/+91{}?text={}'.format(num, msg)

            webbrowser.open(url)

        elif 'read my emails' in query:
            # account credentials
            username = "neelbhatt783@gmail.com"
            password = "9033993649"


            imap = imaplib.IMAP4_SSL("imap.gmail.com")

            imap.login(username, password)

            status, messages = imap.select("INBOX")


            messages = int(messages[0])

            engine.say(f"You Have Totle {messages} emails")
            engine.runAndWait()
            system('say How Many Email i read sir?')
            num = int(takeCommand())
            N = num

            for i in range(messages, messages - N, -1):

                res, msg = imap.fetch(str(i), "(RFC822)")
                for response in msg:
                    if isinstance(response, tuple):

                        msg = email.message_from_bytes(response[1])

                        subject = decode_header(msg["Subject"])[0][0]
                        if isinstance(subject, bytes):

                            subject = subject.decode()
                        from_ = msg.get("From")
                        e_no = messages-i+1
                        print(e_no)
                        engine.say("Email Number")
                        engine.say(f"{e_no}")
                        print("Email From : ", from_)
                        print("Email Subject : ", subject)



                        engine.say("Email From")
                        engine.say(from_)
                        engine.say("Email Subject")
                        engine.say(subject)
                        engine.runAndWait()

                        if msg.is_multipart():

                            for part in msg.walk():

                                content_type = part.get_content_type()
                                content_disposition = str(part.get("Content-Disposition"))
                                try:

                                    body = part.get_payload(decode=True).decode()
                                except:
                                    pass
                                if content_type == "text/plain" and "attachment" not in content_disposition:
                                    # print("Email Body : ", body)
                                    print("Email Has Been Readed")
                                    # engine.say(body)
                                    # engine.runAndWait()
                                elif "attachment" in content_disposition:

                                    filename = part.get_filename()
                                    if filename:
                                        if not os.path.isdir(subject):

                                            os.mkdir(subject)
                                        filepath = os.path.join(subject, filename)

                                        open(filepath, "wb").write(part.get_payload(decode=True))
                        else:

                            content_type = msg.get_content_type()

                            body = msg.get_payload(decode=True).decode()
                            if content_type == "text/plain":
                                # print only text email parts
                                print(body)
                        if content_type == "text/html":

                            if not os.path.isdir(subject):

                                os.mkdir(subject)
                            filename = f"{subject[:50]}.html"
                            filepath = os.path.join(subject, filename)

                            open(filepath, "w").write(body)

                            webbrowser.open(filepath)
                        print("=" * 100)
            imap.close()
            imap.logout()


        else:
            # sorry = f'say User said: {query} I think You ! ".."',query,'".." But I dont Have An A Answer For That Sorry For That'
            say = f'i think "." you are say ".." {query} ".." but "." I Have "." no Answer "." For This'

            # say="lol"
            # say = "tel bhai mari"
            engine.say(say)
            engine.runAndWait()