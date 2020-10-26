import time #importing time module
from datetime import date   #importing date module from datetime

#vairable today storing todays date
today = date.today()

#printing todays date and times %12h:%min%sec
print ('Today is', today, 'and it is', time.strftime('%I:%M:%S'))
