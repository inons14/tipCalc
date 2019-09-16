from tipcalc import waiter
import datetime
#calculate tip by time 
file = open('log.txt','a')
date = str(datetime.datetime.now())
file.write("Date: %s : \n" %(date))
waiters = []
hour = 0.0
totalTip = 0.0
while True:
    name = input("Enter Name: \n")
    if(name!=""):
       newWaiter = waiter(name,float(input("Enter Work Time: \n")),float(input("Enter TipCollected: \n")))
       str1 = "Enter TipCollected:"
       print(len(str1) * "_" + "\n")
       waiters.append(newWaiter)  
    else:
        print(" # No More Waiters #\n")
        break
for waitr in waiters:
    totalTip +=waitr.gettipCollected()
    hour +=waitr.getworkTime()
for waitr in waiters:
    waitr.addtipSalary(waitr.getworkTime()/hour*totalTip)
    print(waitr.getall())
    file.write("{} \n".format(waitr.getall()))
file.write("________________________\n\n")
file.close()