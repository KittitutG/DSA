How to write recursion in 3 steps

Given exampple
Factorial
1. it is product of all positive integer less than or equal to N.
2. denoted by N!
3. inly positive numbers
4. 0! =1

Formular
n! = n*(n-1)*(n-2)*....*2*1

# Step 1: Recurcisve case - the flow
n! = n*(n-1)*(n-2)*....*2*1
can be resolved as: n! = n*(n-1)!
notice that both left and right equation share the same properties(now they 're recusive)

# Step2: Base case -the stopping criteria
without stopping case, this will run infenitely
base case for this one is 0! = 1

# Step3: Unintentional case -the constraint
we need to cover edge case as well.
factorial(0.5) ??
factorial(-5) ??