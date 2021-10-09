
# Python code to demonstrate
# sort a list of dictionary
# where value date is in string
  
import operator
  
# Initialising list of dictionary




ini_list = [{'day':'Sunday', 'key':'1'},
            {'day':'Monday', 'key':'2'},
            {'day':'Tuesday', 'key':'3'},
            {'day':'Wednesday', 'key':'4'},
            {'day':'Thursday', 'key':'5'},
            {'day':'Friday', 'key':'6'},
            {'day':'Saturady', 'key':'7'}]
            
                  
# printing initial list
print ("initial list : ", str(ini_list))
  
# code to sort list on date
ini_list.sort(key = operator.itemgetter('key'))
  
# printing final list
print ("result", str(ini_list))

