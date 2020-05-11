# Power budget(Obligatorisk)
# Programmet skal kunne udregne powerbudget for SFP moduler.
# Opgaven ligner den fra modul 1.1, den skal bare laves i Python i stedet for Excel.
# Husk Flowchart og koden i Github.
from time import sleep 
pb=1
s=Sikkerhedsmargin=3  #Det er et fast tal.
r=Reparationer=0.5 #Det er også et fast tal.

def menu():
    print("1) SM 1310 nm") #Single mode fiber
    print("2) SM 1550 nm")
    print("3) MM 850 nm") #Multimode fiber
    print("4) MM 1300 nm")
    print("5) Stop program")

menu()
menunr=int(input("Indtast 1, 2, 3, 4, og 5"))

while pb==1:
    if menunr==1:
        print("Du har valgt menu nr. 1 (SM fiber 1310 nm)")
        x=float(input("Indtast afsendersignal")) #Output Power =dBm
        y=float(input("Intast modtagersignal")) #Recieve sensitivity =dBm
        print("Brutto overskud=",str(x-y),"dB")
        br=float(x-y) #br forkortelse af Brutto overskud
        a=int(input("Indtast antal splidsninger"))
        b=int(input("Indtast antal konnekteringer"))
        c=float(input("Indtast antal km fiber"))
        sp=float(a*0.1) #Splidsnings tabt pr. stk. = 0.1 dB
        print("Splidsninger=",sp,"dB")
        k=float(b*0.5) #konnekteringer pr. stykke= 0.5 dB
        print("konnekteringer=",k,"dB")
        km=float(c*0.35) #Single  mode fiber taber 0.35 pr. km. ved 1310nm
        lm=float(br-(km+k+sp)) #Linkmargin
        print("Linkmargin=",br-(km+k+sp),"dB")
        print("Sikkerhedmargin",s,"dB")
        print("Reperationer",r,"dB")
        print("Netto overskud=",lm-s-r,"dB")
        N=lm-s-r
        if N>0:
            print("OK")
        else:
            print("Ikke godkendt!")
        sleep(8)
        menu()
        menunr=int(input("Indtast 1, 2, 3, 4, og 5"))

    if menunr==2:
        print("Du har valgt menu nr. 2 (SM fiber 1550 nm)")
        x=float(input("Indtast afsendersignal"))
        y=float(input("Indtast modtagersignal"))
        print("Brutto overskud=",str(x-y),"dB")
        br=float(x-y) #Brutto Overskud
        a=int(input("Indtast antal splidsninger"))
        b=int(input("Indtast antal konnekteringer"))
        c=float(input("Indtast antal km fiber"))
        sp=float(a*0.1) #Splidsningstabt pr. stk. = 0.1 dB
        print("Splidsninger=",sp,"dB")
        k=float(b*0.5) #konnekteringstabt pr. stk. = 0.5 dB
        print("konnekteringer=",k,"dB")
        km=float(c*0.21) #Single  mode fiber taber 0.21 dB pr. km. ved 1550nm
        lm=float(br-(km+k+sp)) #Linkmargin
        print("Linkmargin=",lm,"dB")
        print("Sikkerhedmargin",s,"dB")
        print("Reparationer",r,"dB")
        print("Netto overskud=",lm-s-r,"dB")
        N=lm-s-r
        if N>0:
            print("OK")
        else:
            print("Ikke godkendt!")
        sleep(8)
        menu()
        menunr=int(input("Indtast 1, 2, 3, 4, og 5"))

    if menunr==3:
        print("Du har valgt menu nr. 3 (MM fiber 850 nm)")
        x=float(input("Indtast afsendersignal"))
        y=float(input("Indtast modtagersignal"))
        print("Brutto Overskud=",str(x-y),"dB")
        br=float(x-y)
        a=int(input("Indtast antal splidsninger"))
        b=int(input("Intast antal konnekteringer"))
        c=int(input("Indtast antal km fiber"))
        sp=float(a*0.1) #Splidsnings tabt pr. stk. = 0.1 dB
        print("Splidsninger=",sp,"dB")
        k=float(b*0.5) #Konnekteringstabt pr. stk. = o.5 dB
        print("Konneteringer=",k,"dB")
        km=float(c*2.5) #Multimode fiber taber 2.5 dB pr. km.
        lm=float(br-(km+k+sp)) #Linkmargin
        print("Linkmargin=",lm,"dB")
        print("Sikkerhedsmargin",s,"dB")
        print("Reperationer",r,"dB")
        print("Netto overskud=",lm-s-r,"dB")
        N=lm-s-r
        if N>0:
            print("OK")
        else:
            print("Ikke godkendt!")
        sleep(8)
        menu()
        menunr=int(input("Indtast 1, 2, 3, 4, og 5"))
    if menunr==4:
        print("Du har valgt menu nr. 4 (MM fiber 1300 nm)")
        x=int(input("Indtast afsendersignal"))
        y=int(input("Indtast modtagersignal"))
        print("Brutto Overskud=",str(x-y),"dB")
        br=float(x-y)
        a=int(input("Indtast antal splidsninger"))
        b=int(input("Indtast antal konnekteringer"))
        c=int(input("Intast antal km fiber"))
        sp=float(a*0.1)
        print("Splidsninger=",sp,"dB")
        k=float(b*0.5)
        print("Konnekteringer=",k,"dB")
        km=float(c*2.5)
        lm=float(br-km-k-sp)
        print("Linkemargin=",lm,"dB")
        print("Sikkerhedsmargin=",s,"dB")
        print("Reparationer=",r,"dB")
        print("Netto overskud=",lm-s-r,"dB")
        N=lm-s-r
        if N> 0:
            print("OK")
        else:
            print("Ikke godkendt!")
        sleep(8)
        menu()
        menunr=int(input("Indtast 1, 2, 3, 4, og 5"))
    if menunr==5:
        print("Programmet stopper!")
        pb=2 # ellers kan man også skrive "exit(0)"
        