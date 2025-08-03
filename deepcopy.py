a = [1,2,3,4,5]
b = a #directly copying will change the main data also so this is the concept applied in updating the Bank.json file through Bank.data file 
b[0] = 100
print(a)