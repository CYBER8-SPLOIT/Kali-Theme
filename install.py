import os

logo = '''

  _____                     _     _  _     _  __     _ _ 
 |  __ \                   | |   | || |   | |/ /    | (_)
 | |__) |_ _ _ __ _ __ ___ | |_  | || |_  | ' / __ _| |_           Written By - CYBE R
 |  ___/ _` | '__| '__/ _ \| __| |__   _| |  < / _` | | |          Support Us On Pateron - cyber8
 | |  | (_| | |  | | | (_) | |_     | |   | . \ (_| | | |		   
 |_|   \__,_|_|  |_|  \___/ \__|    |_|   |_|\_\__,_|_|_|          Subscribe - CYBE R
                                                         
'''
menu = '''
(1) Install 
(2) Restore
(3) Exit

For Wallpaper Goto Wallpaper Folder Is Same Directory. 4k Parrot OS Wallpaper
'''

print(logo)
print(menu)

input1 = input("Enter Your Option : ")


try:
	if input1 == 1:
		os.system('rm /root/.bashrc')
		os.system('cp /root/Parrot4Kali/Parrot/.bashrc /root/.bashrc')
		print ("\n\nCongratulation Parrot Os Theme Installed")
		print("\nRestart Your Terminal !!!!!!s") 
		print("\nFor Wallpaper Goto Wallpaper Folder Is Same Directory. 4k Parrot OS Wallpaper")
	
	elif input1 == 2:
		os.system('cp Kali/.bashrc /root/.bashrc')
		print ("\n\nKali Theme Restored")
		print("\nRestart Your Terminal !!!!!!s")
		print("\nFor Wallpaper Goto Wallpaper Folder Is Same Directory. 4k Parrot OS Wallpaper") 		
			
	elif input1 == 3:
		exit
		print ("\n\n\n Have A Nice Day")
			
	else:
		print("OOps! Invalid Options (Did You Mean 1 or 2 or 3)\nFor Wallpaper Goto Wallpaper Folder Is Same Directory. 4k Parrot OS Wallpaper")
			
except:
	print("OOps! Invalid Options (Did You Mean 1 or 2 or 3)\nFor Wallpaper Goto Wallpaper Folder Is Same Directory. 4k Parrot OS Wallpaper")
		

	

#os.system(cp Kali/.bashrc /root/.bashrc)
