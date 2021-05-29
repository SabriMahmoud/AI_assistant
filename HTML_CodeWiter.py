import speech_recognition as sr
import pyttsx3
r=sr.Recognizer()

#################################################################
#################################################################
#################################################################

engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

#################################################################
#################################################################
#################################################################

def takeCommande():

    with sr.Microphone() as source :
        while(True):

            try:
                r.adjust_for_ambient_noise(source)
                audio=r.listen(source)
                get=r.recognize_google(audio)
                print("this is takecommande function "+get+"\n")
                break

            except Exception as e : 

                print(e)
                speak("Say that again please")

    return(get)

#################################################################
#################################################################
#################################################################

def translateTo_Code(message):
    code="" 
      
    message=message.lower()
    
    if 'document type' in message:
            code+="<!DOCTYPE HTML>"
    elif 'open' in message :
        
        
        message=checkWordsException(message)
        message=cleaningFromOpenClose(message)
      
        code+="<"
        code+=message
        code+=">"
        print("Open process :"+code)
        
       
        
    elif 'meta' in message:
        return("<META charset='UTF-8'>",True)
    elif 'write' in message :
        message=message.replace("write","")
        return(message,False)
    elif "close"  in message:
        
        message=checkWordsException(message)
        message=cleaningFromOpenClose(message)
        code+="</"
        code+=message
        code+=">"
        print("this is close process "+code)
        
     
    elif 'quit' in message:
        quit()

    else :

         message=checkWordsException(message)
         if message.split()[0] not in ["close","open","write"] :
             speak("there is no command recognized ")
             message=takeCommande()
         
         translateTo_Code(message)
          
    return(code,True)


#################################################################
#################################################################
#################################################################


def checkWordsException(message):
    message=message.lower()
    splitedList=message.split()

    for i in range(len(splitedList)):

        #check lowe's h3
        if splitedList[i] in ["lowe's","clothes","those","how's","call","low","load","ghost"]:
            splitedList[i]="close"
        elif splitedList[i].lower() in ["buddy","budgie","bundy"]:
            splitedList[i]="body" 
        elif splitedList[i].lower()=="right" :
            splitedList[i]="write" 
        elif splitedList[i].lower()=="metal":
            splitedList[i]="meta"
        elif splitedList[i] in ["heads","hit","that","jed","dad","at","dead"] or message=="closehead"  :
            splitedList[i]="HEAD"
        elif splitedList[i] in ["burger","paragraph","paragraphs"]:
            splitedList[i]="p"
        elif splitedList[i] in ["bolt","bold","bull","ball","bone"] :
            splitedList[i]="b"
        
    if message.__contains__("-") :
        message=message.replace("-"," ")
        
    else:
        message=" ".join(splitedList)
        
    return message

#################################################################
#################################################################
#################################################################
             

    
    
    


#################################################################
#################################################################
#################################################################


def cleaningFromOpenClose(message):
    
    for e in message.split():
        if e!="open" and e!= "close":
            message=e
    return(message.lower())
#################################################################
#################################################################
#################################################################







#################################################################
#################################################################
#################################################################

def checkElements(code):
    element=""
    if(code.__contains__("/")):
        element=code[2:len(code)-1]
    else:
        element=code[1:len(code)-1]
    print(element)
    return(element not in baliseListe)

#################################################################
#################################################################
#################################################################
#there is a problem in close h3

baliseListe=["html","META charset='UTF-8'","!DOCTYPE HTML","head","HEAD","title","body","p","h1","h2","h3","<H4>","</H4>","b","b","<main>","</main>","<section>","</section>","<article>","</article>","<aside>","</aside>","<header>","</header>","<footer>","</footer>"]
tabulation=""

speak("Welcome to HTML CodeWriter")
speak("Start coding")

while(True) : 

    message=takeCommande()
    code=""

    if message=="quit" :
        break

    (code,b)=translateTo_Code(message)
    checkElement=checkElements(code)
    if checkElement  and b:
         
         
        speak("False element Error recognizing try again")
        print(len(code))

    else :

        if code.__contains__("/"):
            speak("closed")

        else :

            if code.__contains__("<") :
                 speak("opened")

        f=open("test.html","a")
        f.write(code)
        tabulation+="\t"
        f.write("\n"+tabulation)
        f.close()
        print(code)

    
    

