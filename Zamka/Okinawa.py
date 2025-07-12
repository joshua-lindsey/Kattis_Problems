from pytz import timezone
from datetime import datetime


currentDT = datetime.now()
print('colorado time')
print (currentDT.strftime("%a, %b %d, %Y"))
print (currentDT.strftime("%I:%M:%S %p"))
print()

japan = timezone('Japan')
#print(japan.zone)
japan_time = datetime.now(japan)
print('japan_time')
print (japan_time.strftime("%a, %b %d, %Y"))
print (japan_time.strftime("%I:%M:%S %p"))
print()

illinois = timezone('US/Central')
#print(illinois.zone)
illinois_time = datetime.now(illinois)
print('illinois_time')
print (illinois_time.strftime("%a, %b %d, %Y"))
print (illinois_time.strftime("%I:%M:%S %p"))