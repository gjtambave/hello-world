def nth_root(n):
    """Returns the actual_root function"""
    def actual_root(x):
        """Returns the nth root of x"""
        root = x ** (1/n)
	print(x)
        return root
    return actual_root

square_root = nth_root(2)
cube_root = nth_root(3)
print(square_root(9), cube_root(27))
