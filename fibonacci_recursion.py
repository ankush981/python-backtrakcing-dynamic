# The regular (head-call) version of the recursive solution for finding the nth Fibonacci number
def fibonacci_head_call(n):
    if n == 0: return 0
    if n == 1: return 1

    return fibonacci_head_call(n-1) + fibonacci_head_call(n-2)

# While the above solution is extremely "intuitive", it's what the mind first reaches for. However, we can do slightly better by optimizing for tail recursion
def fibonacci_tail_call(n, n1 = 0, n2 = 1):
  if (n == 0): return n2
  return fibonacci_tail_call(n - 1, n2, n1 + n2)

if __name__ == "__main__":
    head_call_result = fibonacci_head_call(10)
    tail_call_result = fibonacci_tail_call(10)
    assert head_call_result == tail_call_result
    print(head_call_result)