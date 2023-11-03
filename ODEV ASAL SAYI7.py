#!/usr/bin/env python
# coding: utf-8

# In[10]:


n = int(input("Sayıyı Giriniz: "))

for sayi in range(2 , n+1):  
      for b in range(2 , sayi):
         if (sayi % b) == 0:
                break
      else:
        print(sayi)
    
    
    


# In[19]:


sayac = 1

while sayac < 3 ** 30:
    sayac *= 3
    print(sayac)
                


# In[17]:


liste = [3, 12 , 18 , 25 , 29 , 100]

for number in liste:
    print(number ** 0.5)
    



# In[ ]:





# In[ ]:




