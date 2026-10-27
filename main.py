from pyscript import document,display
#Dictionary
#comma makes set, colon makes dict
#set1 = {'sample1', "sample2"}
#display(type(set1), target="output1")
#unique keys; values can have duplicates

grades = {"Math": 95,
          "Science": 97,
          "Filipino": 98,
          "P.E": 95}   
del grades['P.E']        
display(grades, target="output1")  


#info1 = ['First Name', "Last Name", "Category"]   
#info2 = ["Peter", "Parker", "Hero"]  
#details = dict(zip(info1, info2))    

