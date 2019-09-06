import webbrowser
import time
x = 1
path='C:\Users\nitin\Desktop\Tor Browser\Browser\firefox.exe %s'


while x!=0:
  ##webbrowser.get(path).open('https://www.ghuguti.com/')
  ##time.sleep(15)
  webbrowser.open('https://www.ghuguti.com/')
  time.sleep(15)
  webbrowser.open_new_tab('https://www.ghuguti.com/')
  time.sleep(20)
  x +=1
    
	
