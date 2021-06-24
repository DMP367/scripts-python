

import platform
import os
import sys 

def system_command(time_desl):
	so = platform.system()

	if so == 'Windows':
		time_desl *= 60
		return "shutdown -s -t " + str(time_desl)
	elif so == 'Linux':
		return "shutdown -s -t " + str(time_desl)
	else:
		exit()



x = int(input("desligar o pc em: "))


command = system_command(x)

#print(command)
os.system(command)