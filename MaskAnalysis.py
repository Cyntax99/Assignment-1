#Prof. Berg, Assignment 1, Mohamed Yousif
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
from statistics import mean 
data=pd.read_csv('mask.csv')
stateData=pd.read_csv('State_Codes.csv')
stateAbbr=pd.read_csv('abbr.csv')


# In[2]:


# gives state name of county number, accepts: county number and returns state name
def getState(countyNo):
    county=str(countyNo)
    county=county[0:1]#getting state code
    for i in range(0,len(stateData["State Code (FIPS)"])):
        if county==str(stateData["State Code (FIPS)"][i]):
            return stateData["area"][i]
    return 0        
        
    


# In[3]:


#giving result for user choice WHOLE US ANALYSIS
def byCountyWise():
    print('Avg % of NEVER Category: ',data["NEVER"].mean()*100) #mean of never category
    print('Avg % of RARELY Category: ',data["RARELY"].mean()*100)
    print('Avg % of SOMETIMES Category: ',data["SOMETIMES"].mean()*100)
    print('Avg % of FREQUENTLY Category: ',data["FREQUENTLY"].mean()*100)
    print('Avg % of ALWAYS Category: ',data["ALWAYS"].mean()*100)
    hiRank=1000 #temp BEST MASK wearing country
    temp=0.0
    x=0 # temp for frequently 
    y=0#temp for always
    for i in range(0,len(data["ALWAYS"])):
        x=data["FREQUENTLY"][i]
        y=data["ALWAYS"][i]
        if temp< (x+y): #comparing temp with summing always and frequenlty
            temp=x+y
            hiRank=data["COUNTYFP"][i] 

    #same for worst wearing as described above

    lowRank=1000
    temp=0.99
    x=0
    y=0
    for i in range(0,len(data["NEVER"])):
        x=data["NEVER"][i]
        y=data["RARELY"][i]
        if temp> (x+y):
            temp=x+y
            lowRank=data["COUNTYFP"][i]
#showing results
    print('County with BEST MASK %',hiRank)
    print('County with WORST MASK %',lowRank)
    print('State with BEST MASK %',getState(hiRank))
    print('State with WORST MASK %',getState(lowRank))

    


# In[4]:


#gives state code after giving state abbreviation i,e NY
def getStateCode(state):
    stateName=''
    #state abrevaition to state full name
    for i in range(0,len(stateAbbr["Full State Name"])):
        if state==stateAbbr["State Abbreviation"][i]:#find for state abbreviaion in file
            stateName=stateAbbr["Full State Name"][i]
    stateCode=0
    #state full name to state code
    for i in range(0,len(stateData["State Code (FIPS)"])):
        if stateName==stateData["area"][i]:
            stateCode=stateData["State Code (FIPS)"][i]
    county=0
    return stateCode


# In[5]:





# In[14]:


#Analysis by state wise by taking state abbreviation and giving state analsysis results
def byStateWise(state):
    never=list() #for stroing NEVER category data
    always=list()#for stroing ALWAYS category data
    sometimes=list()#for stroing SOMETIMES category data
    freq=list()#for stroing FREQUENTLY category data
    rare=list()##for stroing RARELY category data
    #getting state code from state abbreviation
    stateCode=getStateCode(state)
    for i in range(0,len(data["COUNTYFP"])):
        stateCode=str(stateCode) 
        x=str(data["COUNTYFP"][i])
        x=x[0:2]
        if(stateCode==x): # if countyfp code equlas requierd state
            #stores that state data to lists
            never.append(data["NEVER"][i]) 
            always.append(data["ALWAYS"][i])
            rare.append(data["RARELY"][i])
            sometimes.append(data["SOMETIMES"][i])
            freq.append(data["FREQUENTLY"][i])
     #giving requied analysy       
    print('Avg % of NEVER Category:',mean(never))
    print('Avg % of RARELY Category:',mean(rare))
    print('Avg % of FREQUENTLY Category:',mean(freq))
    print('Avg % of SOMETIMES Category:',mean(sometimes))
    print('Avg % of ALWAYS Category:',mean(always))
    
    
    
    


# In[16]:


#Main 
inp=5
while inp!=0:
    inp=int(input('Enter your choice: 1) State wise 2) County Wise 0) To Exit  '))
    if(int(inp==1)):#if user choice 1
        print('Showing Whole US Analysis')
        byCountyWise()
    elif inp==2:
        st=input('Enter state Abbreviation :')
        print('Showing State Analysis')
        byStateWise(st)


# In[ ]:





# In[ ]:




