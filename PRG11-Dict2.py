animals = { 'a':'aard', 'b':'baboon', 'c':'coate' }
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
count =0
temp =None
for anml in animals.keys():
    #print(anml)
    if(len(animals[anml])>count):
        temp=anml
        count=len(animals[anml])
print(temp)