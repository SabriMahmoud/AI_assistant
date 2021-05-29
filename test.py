def checkWordsException(message):
    splitedList=message.split()
   
    for i in range(len(splitedList)):
        if splitedList[i]=="Lowe's" :

            splitedList[i]="close"
        elif splitedList[i].lower()=="buddy":
            splitedList[i]="BODY" 
        elif splitedList[i].lower()=="right" :
            splitedList[i]="write" 
        elif splitedList[i].lower()=="metal":
            splitedList[i]="meta"
    
    message=" ".join(splitedList)
    
    return message
def cleaningFromOpenClose(message):
    
    for e in message.split():
        if e!="open" and e!= "close":
            message=e
    return(message.upper())

def checkElements(code):
    element=""
    if(code.__contains__("/")):
        element=code[2:len(code)-1]
        print(element)
    else:
        element=code[1:len(code)-1]
    return(element in ["head"])
baliseListe=["<html>","</html>","<META charset='UTF-8'>","<!DOCTYPE HTML>","<head>", "</head>","<title>","</title>","<body>","</body>","<p>","</p>","<h1>","</h1>","<h2>","</h2>","<H3>","</H3>","<H4>","</H4>","<b>","</b>","<main>","</main>","<section>","</section>","<article>","</article>","<aside>","</aside>","<header>","</header>","<footer>","</footer>"]
print(checkElements("</head>"))