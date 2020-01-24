#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This algorithm will always loop n times, as n cubed will always be equal to or less than a after n cycles, and not before, due to the loop adding n squared to a. 


b) This algorithm will be one loop longer each time n surpasses a power of 2, as j begins at 1, and multiplies by 2 each time, resulting in it essentially adding a power of 2 to j, while the sum only ever iterates up by 1.


c) This snippet can only ever return 2, as it's a conditional statement that only works when the variable used for the return statement is 1, as 1 - 1 is 0, which will fulfill the bunnies == 0 conditional statement to return a result of 0.  Anything else will return an error, and is worst-case.

## Exercise II

```
eggs = 96
while (n < f):
    print("Didn't break an egg on floor {n}!")

eggs -= 1
print("Broke an egg on floor {n}!")
```


This algorithm will loop through floors starting from 1 until it reaches a floor where an egg breaks (floor f).  While certainly not the most efficient way to find f, this would be an average-case complexity to find floor f, and minimizes the number of eggs you need to break to 1.