from periphery import GPIO
import time

GPIO_out = GPIO(0, "out")


GPIO_out.write(True) 
time.sleep(5)
GPIO_out.write(False)
time.sleep(5) 
GPIO_out.write(True) 
time.sleep(5)
GPIO_out.write(False)
time.sleep(5) 
GPIO_out.write(True) 
time.sleep(5)
GPIO_out.write(False)
time.sleep(5) 

GPIO_out.close()

