import os       #operating system
import shutil   #Shell util

# current working directory
print(os.getcwd())    

# disk usage of the system
print(shutil.disk_usage("/"))

#Readable format
total, used, free =shutil.disk_usage("/")
print("total space:",total// (2**30))
print("used space:",used// (2**30))       #Bits to GB format
print("free space:",free// (2**30))

