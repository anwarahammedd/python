#list comprehension test
#[1,2,3,4,5]
#[1,2,9,4,25]
#True & False
#newlist=[true_exp if(condition) else false_exp for i in sequence]

numbers=[1,2,3,4,5,6,7,8,9]
newlist=['odd' if(i%2==1) else 'even' for i in numbers]
print(newlist)
