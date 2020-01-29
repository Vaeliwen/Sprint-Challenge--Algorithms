#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is an 0(n) function, as it grows linearly more complex as n grows larger, causing the number of times that the while statement must loop to increase with a 1:1 ratio.


b) This function is 0(n) in terms of time complexity, as it only grows more complex each time n passes a power of 2, such as 8, 16, 32, or larger powers of 2.


c) This is an O(n) function, as it grows linearly more complex the larger n is, forcing the recursion to loop one additional time each time n increases by 1.

## Exercise II

Assuming an n-story building, if you wish to find a floor f, where f is the minimum height for an egg to break, it behooves you to find a floor somewhere in the middle of the list of floors within n.  If the egg breaks, then you know every floor above it will also break the egg, and if it does not, you know every floor below will not either.  This solution would be of the O(log n) variety.