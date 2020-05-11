#Statemachine til beskrivelse af livets gang
from gpiozero import LED
from time import sleep 

NSred= LED(13)
NSgul=LED(19)
NSgreen=LED(26)
EVred=LED(16)
EVgul=LED(20)
EVgreen=LED(21)


print("Test!")
EVred.on()
sleep(1)
EVgreen.on()
sleep(1)
EVgul.on()
sleep(1)
NSred.on()
sleep(1)
NSgreen.on()
sleep(1)
NSgul.on()
sleep(1)
EVred.off()
EVgreen.off()
EVgul.off()
NSred.off()
NSgreen.off()
NSgul.off()

def redred(x):# Udgangs punkt for lyskrydset
    if x=="NS": #Hvis lyskrydset kommer fra NS skal den gå til EV
        x="EV"
        print("NS RED   EV RED")
        NSred.on()
        EVred.on()
        sleep(2)
        return EV(x)
    elif x=="EV": #Hvis lyskrydset kommer fra EV skal den gå til NS
        x="NS"
        print("NS red   EV red")
        NSred.on()
        EVred.on()
        sleep(2)
        return NS(x)

def NS(x):
    if x=="NS":
        print("NS GREEN   EV RED")
        NSgul.on()
        sleep(2)
        NSred.off()
        NSgul.off()
        NSgreen.on()
        sleep(5)
        NSgreen.off()
        NSgul.on()
        sleep(2)
        NSgul.off()
        return redred(x)
    
def EV(x):
    if x=="EV":
        print("NS RED   EV GREEN")
        EVgul.on()
        sleep(2)
        EVred.off()
        EVgul.off()
        EVgreen.on()
        sleep(5)
        EVgreen.off()
        EVgul.on()
        sleep(2)
        EVgul.off()
        return redred(x)
    

state=redred(x="EV")
while state: state=redred(x="EV")