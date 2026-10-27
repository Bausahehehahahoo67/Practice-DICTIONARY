from pyscript import document,display
#Dictionary
#comma makes set, colon makes dict
#set1 = {'sample1', "sample2"}
#display(type(set1), target="output1")
#unique keys; values can have duplicates
#my_sample_data = {"Math": 95,
                  #"Science": 97,
                  #"Filipino": 98,
                  #"P.E": 95}        
info1 = ['First Name', "Last Name", "Category"]   
info2 = ["Peter", "Parker", "Hero"]  
details = dict(zip(info1, info2))    
display(details, target="output1")
