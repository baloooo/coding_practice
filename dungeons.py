'''
https://leetcode.com/problems/dungeon-game/discuss/52784/Who-can-explain-why-%22from-the-bottom-right-corner-to-left-top.%22

https://www.geeksforgeeks.org/minimum-positive-points-to-reach-destination/

Todo: Program is as simple as in geeksforgeeks article here, but why are these conditions set up so is not
quite clear.
Also why this exercise cannot be solved from top to down is explained in link1
    Many users have asked question if solution for this problem can also be achieved from top left corner navigating to the bottom right or not. I believe it cannot be achieved.

This is because the path to be taken depends upon the future demons seen on the way to princess, which is not available in top down approach.

e.g. Consider the matrix

0, -2, 0
-3, 0, 0
10, 0 P', -5 P

P' and P are potential positions for princess

If the matrix consists only of two columns (say princess is at P') we would take the path Right->Down->Down (minimize the health and result = -(-2) + 1 = 3

However, if the matrix consists of three columns we would take the path of Down->Down->Right->Right with result = -(-3)+1 = 4
Note that the previous path here would return suboptimal result = -(-2) + -(-5) + 1 = 8

This information cannot be computed when we are at node i=2, j=1 assuming zero based index (i.e. we do not know if we have to minimize the health at current point or take maximum positive value for the sake of higher health cost to account for future demons) This can only be factored in by computing the result in bottom up manner.


Notice that we can override the dungeon grid if we want, we take dp array just to keep things clear.
'''

