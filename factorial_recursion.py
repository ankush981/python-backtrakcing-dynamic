# The factorial function implemented both as a head-call and tail-call recursion

def factorial_head_call(n):
    if n == 1:
        return 1;
    
    return n * factorial_head_call(n - 1)

def factorial_tail_call(n, accumulator = 1):
    if n == 1:
        return accumulator # as the accumulator contains the final result of all multiplications
    
    return factorial_tail_call(n - 1, n * accumulator)

if __name__ == "__main__":
    head_call_result = factorial_head_call(5)
    tail_call_result = factorial_tail_call(5)
    assert head_call_result == tail_call_result
    print(head_call_result)