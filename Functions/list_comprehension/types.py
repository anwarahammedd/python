#To create a new list

#*nelst=[expression for i in sequence]
#lst=[1,2,3,4,5,6]
#newlist=[i for i in lst]

#True
#newlist=expression for i in sequ if(cond)]
#newlst=[i for i in list if(x%2==0]

#True & False
#newlist=[true_exp if(condition) else false_exp for i in sequence]

cars=['aston martin','bmw','mercedes','audi','toyota','mclaren']
newcars=['dc avanti' if i!='mclaren' else 'mclaren' for i in cars]
print(newcars)

countries=['America','Japan','China','Africa','Canada']
newcountries=[i if i!='America' else 'India' for i in countries]
print(newcountries)

#Check even or odd
#[1,2,3,4,5,6,7]
numbers=[1,2,3,4,5,6,7]
newnumber=['even' if i%2==0 else 'odd' for i in numbers]
print(newnumber)

