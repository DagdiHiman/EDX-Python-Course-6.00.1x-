animals = { 'a':'aardvark', 'b':'baboon', 'c':'coate' }
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
#print(animals.values())

l=0
for anml in animals.keys():
    '''print(animals[anml])
    l=len(anml)
    print(l)'''
    l += len(animals[anml])
    print(l)
