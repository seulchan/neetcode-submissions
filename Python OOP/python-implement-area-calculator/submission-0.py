import math

class AreaCalc:
    def calculate(self, length, width=None):
        if width is None:
            # Single argument provided: calculate circle area (length acts as radius)
            return round(math.pi * (length ** 2), 2)
        
        # Two arguments provided: calculate rectangle area
        return length * width
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
