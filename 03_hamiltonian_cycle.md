## Hamiltonian Cycles

Let's start easy. This problem is related to undirected graphs. That is, there's a given graph data structure, and there's no direction to the edges connecting two vertices.

Given all this, let's consider the following definition.

### Hamiltonian Path

In such a graph, a hamiltonian path is one that visit each node in the path exactly once. Notice that sometimes there many not be any Hamiltonian Path in a given undirected graph.

### Hamiltonian Cycle

If we extend a Hamiltonian path such that after visiting the last node, it comes back to the first node (closing the loop, that is), this becomes a Hamiltonian cycle.

Notice that there may be multiple Hamiltonian paths and cycles in an undirected graph!

### Solving vs. Assessing

Although the problem itself is NP-Complete (a hard class of problems in Complexity Theory), assessing whether a solution exists can be done in linear time with the use of topological ordering (sorting; don't worry for now).

One of the most helpful tools we have in assessing such problems is the Dirac Principle.

### Dirac Principle

A simple graph with N vertices is Hamiltonian if every vertex has degree N/2 or higher.

This simple principle allows us to figure out whether or not it's even worthwhile to try to solve the given graph!