## Backtracking Notes

Backtracking is a form of recursion and is a very important solving strategy for the class of problems known as **constraint satisfaction problem**.

### Constraint Satisfaction Problem

The formal defition is rather complex, but the general idea is that in such problems, we are interested in finding a solution that satisfies the given contraints, as opposed to worrying about the most optimal solution for the problem.

### How Backtracking works

Backtracking works by incrementally building candidate solutions to a problem. If at a stage a candidate cannot be completed, it is discarded and the program recurses (backtracks) to evaluate or build the next candidate.

### Why Backtracking

Backtracking not just solves a problem; it's far more efficient to Brute Force as it cna elimiate whole classes of candidates based on certain tests. As such, it becomes a very attractive approach for, for example, combinatorial optimization problems.

### How it works

This is how backtracking works:
- The problem is tackled by creating a tree data structure, the nodes of which are partial candidates to the solution. This is called the "potential search tree".
- The child nodes differ from their parent nodes by an "extension step". The extension step is generic and depends on the problem, of course.
- Once the tree is built out, the leaves represent the potential candidates that cannot be extended any further.
- With this tree in hand, the algorithm performs a Depth-First Search (DFS) to look for a possible solution.
- Very importantly, if a node cannot be completed to a solution, the whole subtree is skipped!

If all this sounds too abstract, think of "game trees" where each node of the tree contains the full state of the game. Any child node that cannot continue while satisfying the constraints (n-queen problem, for example) is discarded, including the entire sub-tree of it. This saves huge amounts of calculations in Chess, for example.