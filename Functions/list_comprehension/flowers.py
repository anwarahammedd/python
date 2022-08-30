#list comprehension
#flower=['lilly','rose','lotus','sunflower']
#newlist=['lotus','rose']

flowers=['lilly','rose','lotus','sunflower']
newflowers=[]
for flower in flowers:
    if 'o' in flower:
        newflowers.append(flower)
print(newflowers)


