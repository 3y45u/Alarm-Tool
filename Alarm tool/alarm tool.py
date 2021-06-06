import datetime
hour=int(input("Enter the hour"))
mi=int(input("Enter the minute"))
ap=input("am or pm")
st=int(input("Enter the Snooze time :"))
if ap=='pm':
    hour=hour+12

while True:
    if(hour==datetime.datetime.now().hour and mi==datetime.datetime.now().minute):
        print("Uth jaa time ho gya")
        break

print("DO YOU WANT TO SNOOZE THE ALARM\n Y OR N")

sn=input("Enter the response :")

while sn=='Y':
    if sn=='Y':
        ct=datetime.datetime.now().minute
        ct=ct+st
        while True:
            if(ct==datetime.datetime.now().minute):
                print("Wake up")
                break
    sn=input("Enter the response :")
        



