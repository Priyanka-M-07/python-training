pairs=[(x,y) for x in [1,2] for y in [3,4]]
print (pairs)


for x in[3,4]:
    for y in [2,1]:
        print (pairs)


labels=['even' if x%2==0 else 'odd' for x in range(5)]
print(labels)
