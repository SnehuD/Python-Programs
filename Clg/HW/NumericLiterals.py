a = 0b1010  # Binary Literals
b = 100  # Decimal Literal
c = 0o310  # Octal Literal
d = 0x12c  # Hexadecimal Literal

# Float Literal
float_1 = 10.5
float_2 = 1.5e2

# Complex Literal
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

"""
In the above program,
We assigned integer literals into different variables. Here, a is binary literal, b is a decimal literal, 
c is an octal literal and d is a hexadecimal literal. When we print the variables, all the literals are converted 
into decimal values. 10.5 and 1.5e2 are floating-point literals. 1.5e2 is expressed with exponential and is 
equivalent to 1.5 * 102. We assigned a complex literal i.e 3.14j in variable x. Then we use imaginary literal (
x.imag) and real literal (x.real) to create imaginary and real parts of complex numbers. """