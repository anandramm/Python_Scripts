#Hacker Rank Python Program for Polar Co-ordinates
import cmath

z=complex(input())

x=cmath.phase(z)
y=abs(z)
print(y)
print(x)
