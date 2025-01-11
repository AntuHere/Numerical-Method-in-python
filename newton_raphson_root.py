def newton_raphson(f,f_prime,x0, tol=10e-6,max_iter = 100):
    x = x0

    for i in range(max_iter):
        fx = f(x)
        f_prime_x = f_prime(x)

        if f_prime_x == 0:
            raise ValueError("Derivative is zero. No solution found")
        
        x_new = x - fx/f_prime_x

        if abs(x_new-x) <tol :
            return x_new, i+1
        
        x = x_new
    raise ValueError("Maximum iteration reached but no solution found")


f = lambda x: x**2 - 4
f_prime = lambda x: 2*x
x0 = 3
print(newton_raphson(f,f_prime, x0))

