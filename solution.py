
# Python code to demonstrate
# sort a list of dictionary
# where value date is in string
  
import operator
  
# Initialising list of dictionary




ini_list = [{'day':'Sunday', 'key':''},
            {'day':'Monday', 'key':''},
            {'day':'Tuesday', 'key':''},
            {'day':'Wednesday', 'key':''},
            {'day':'Thursday', 'key':''},
            {'day':'Friday', 'key':''},
            {'day':'Saturady', 'key':''}]
            
                  
# printing initial list
print ("initial list : ", str(ini_list))
  
# code to sort list on date
ini_list.sort(key = operator.itemgetter('key'))
  
# printing final list
print ("result", str(ini_list))

