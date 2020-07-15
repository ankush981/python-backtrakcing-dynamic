# The obligatory Towers of Hanoi recursion problem
# The interesting thing about this algorithm is that it needs a minimum of 2^n - 1 moves to solve, making its time complexity O(2^n). Thus, it's a very, very slow algorithm.

# As a refreshers, the rules of the game are:
# - Transfer the stack of discs from the first tower to the last one, using the middle one as intermediary.
# - Move only one disk at a time
# - You are not allowed to place a larger disc on a smaller disc

# Remember, nobody fully understands recursion or is able to trace it in their mind, so a bit of a "leap of faith" is always required. In this case, the leap of faith is this: the problem is trivial to solve if we know how to move the top n - 1 plates from first to last rod (tower) and then just worry about moving the final, largest plate to the last rod (and then, of course, out the n - 1 pile on top of it).

def hanoi(n, rod1, rod2, rod3):
    # if only the smallest plate if left (or if there was only one plate)
    if n == 1:
        print("Moving Plate 1 from %s to %s" % (rod1, rod3))
        return
    
    hanoi(n - 1, rod1, rod3, rod2) # move the top n - 1 discs from rod1 to rod2, using rod3 as auxiliary disk
    print("Moving Plate %s from %s to %s" % (n, rod1, rod3)) # now move the remaining largest disc from rod1 to rod3
    hanoi(n - 1, rod2, rod1, rod3) # this time, rod1 becomes the auxiliary rod

# Another way of summarizing the working of this algorithm is to say that with every iteration, we manage to put the largest disc on the final rod. :)

if __name__ == "__main__":
    hanoi(10, 'A', 'B', 'C')