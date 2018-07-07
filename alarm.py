
# coding: utf-8

# In[ ]:


import time


# In[ ]:


import webbrowser


# In[ ]:


set_alarm=raw_input("Set alarm as H:M:S")
url=raw_input("Enter the website to open:")
at=time.strftime("%I:%M:%S")
while (at!=set_alarm):
    print("The actual time is:"+at)
    at=time.strftime("%I:%M:%S")
    time.sleep(1)
if(at==set_alarm):
    print("Webpage opens")
    webbrowser.open(url)

