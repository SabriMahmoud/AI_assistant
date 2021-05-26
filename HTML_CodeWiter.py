import speech_recognition as sr
import pyttsx3
r=sr.Recognizer()
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommande():
    with sr.Microphone() as source :
        while(True):
            try:
                audio=r.listen(source)
                get=r.recognize_google(audio)
                print(get)
                break
            except Exception as e : 
                print(e)
                speak("Say that again please")
    return(get)
def translateTo_Code(message):
    code=""   
    if 'document type' in message:
            code+="<!DOCTYPE HTML>"
    elif 'open' in message :
        
        message=cleaning(message)
        code+="<"
        code+=message
        code+=">"
        
    elif 'meta' in message :
        code="<META charset='UTF-8'>"
    elif 'close ' in message :
        message=cleaning(message)
        code+="</"
        code+=message
        code+=">"
    elif 'write' in message :
        message.replace("write","")
        return(message,False) 
    elif 'quit' in message:
        quit()
    
    return(code,True)

def cleaning(message):
    
    for e in message.split():
        if e!="open" and e!= "close":
            message=e
    return(message.upper())


baliseListe=["<HTML>","</HTML>","<META charset='UTF-8'>","<!DOCTYPE HTML>","<HEAD>", "</HEAD>","<TITLE>","</TITLE>","<BODY>","</BODY>","<P>","</P>","<H1>","</H1>","<H2>","</H2>","<H3>","</H3>","<H4>","</H4>","<B>","</B>","<MAIN>","</MAIN>","<SECTION>","</SECTION>","<ARTICLE>","</ARTICLE>","<ASIDE>","</ASIDE>","<HEADER>","</HEADER>","<FOOTER>","</FOOTER>"]
tabulation=""
while(True) : 
    message=takeCommande()
    code=""
    if message=="quit" :
        break
    code,b=translateTo_Code(message)
    if code not in baliseListe  and b:
        speak("Error recognizing try again")
        print(code)
    else :
        f=open("test.html","a")
        f.write(code)
        tabulation+="\t"
        f.write("\n"+tabulation)
        print(code)

    
    
f.close()
