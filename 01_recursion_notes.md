## Recursion is not mandatory

Problems solved using recursion can also be solved using iteration, and more efficiently at that. It's just that recursion results is exceedinly elegant solutions, which is why it's a fundamental technique in problem-solving.

## Types of Recursion

Recursion is of two types, as described below.

### Head Recursion

This is the type where the recursive calls generally appears at the beginning (head) of the function. 
- The defining characteristic of head-recursion is that the variables involved in the recursive call are not known or the value of the recursive call (which will produce a result in future) is used in computation.
- There might also be statements to be executed _after_ the recursive call. 
- As a result, the state of the current function call needs to be preserved before the recursive call is made. This uses up more stack memory.

### Tail Recursion

In this type of recursion, the recursive function call appears at the end of the function.
- The defining characteristic of a tail-recursive call is that the function call is the last and _only_ thing the function does.
- The recursive call is not being used in the calling function, and there are no unknown variables or statements to be executed.
- As a result, no extra memory is needed to perform this type of recursion.
- In principle, tail recursion is like a simple iterative loop.

### Last != tail recursion

Just because the recursive call appears at the end of the function doesn't make it tail-recursive. A good example is the factorial function call: `return n * fact(n-1)`. Even if this appears at the end of the function, the call still relies on using `fact(n-1)` for the multiplication and so the state needs to be saved.

A true tail-call version would be to carry the calculations in the function arguments, in a way pushing the state into function arguments, _and_ making sure it's the last and only thing the calling function does. For example, we might rewrite the earlier statement as `return fact(n-1, n * result)`.

See the program `factorial_recursion.py` for concrete examples.




