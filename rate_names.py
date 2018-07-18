
# coding: utf-8

# In[14]:


import random


# In[15]:


class BabyName:
    
    def __init__(self, name, rating=0):
        self.name = name.title()
        self.rating = rating
    
    def rate(self):
        while self.rating == 0:
            try:
                user_rating = int(input(f"Rate how much you like the name {self.name}\nfrom (least) 1 to 10 (most): "))
                if user_rating not in range(1, 10):
                    print("Nah-ah, keep it reproducible!")
                else:
                    self.rating = user_rating
            except ValueError as e:
                print(f"{e}: Please enter a number from 1 to 10.")
    
    def __repr__(self):
        return f"Baby Name: {self.name}, rated: {self.rating}"
    


# In[16]:


with open('names.csv', 'r') as f:
    name_objs = []
    for line in f.readlines()[1:]:  # skip the first line that holds the column names
        line = line.rstrip()  # remove newline char
        name, rating = line.split(',')  # resolving CSV file (2 datums)
        # creat a BabyName object
        baby_name = BabyName(name, int(rating))  # convert rating to integer
        name_objs.append(baby_name)


# In[17]:


count = 0
while count < 5: # ask only a few every time
    ask = random.choice(name_objs)
    if ask.rating != 0:
        continue
    else:
        ask.rate()
        count += 1


# In[18]:


# write the changed data back to file
str_repr = ""
for name in name_objs:
    str_repr += f"{name.name},{name.rating}\n"

with open('names.csv', 'w') as f:
    f.write("name, rating\n")
    f.write(str_repr)

