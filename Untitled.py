#!/usr/bin/env python
# coding: utf-8

# In[1]:


dic= {
    stu={
        "name" : "nirajan",
        "sid" : "23",
        "class" : "cse",
        "grades" : [9,10,7,8,7]
    }
}


# In[2]:


dic= {
    stu{
        "name" : "nirajan",
        "sid" : "23",
        "class" : "cse",
        "grades" : [9,10,7,8,7]
    }
}


# In[3]:


dic= {
    stu : {
        "name" : "nirajan",
        "sid" : 23,
        "class" : "cse",
        "grades" : [9,10,7,8,7]
    }
}


# In[7]:


dic= {
    "stu":{
        "name" : "nirajan",
        "sid" : 23,
        "class" : "cse",
        "grades" : [9,10,7,8,7] }
}


# In[8]:


print(dic)


# In[9]:


stu2={
       "name" : "nir",
       "sid" : 22,
       "class" : "ece",
       "grades" : [10,10,7,8,7]
   }


# In[10]:


dic.add(stu2)


# In[11]:


print(dic.update(stu2))


# In[12]:


print(dic)


# In[34]:


def add(stu,name,i,clas,gra):
    a={"name": name , " sid": i, "class" : clas, "grade" : gra}
    dic[stu]=a
    return
add(" stu " ,"ni",29, "bt",[10,10,7,8,1])
print(dic)
    


# In[46]:


def update(stu,xy,new):
    dic[stu][xy]=new
    return
update("stu", "name" , " jai")
print(dic)


# In[37]:


print(dic)


# In[39]:


print(dic)


# In[40]:


print(dic)


# In[42]:


print(dic)


# In[43]:


print(dic)


# In[ ]:




