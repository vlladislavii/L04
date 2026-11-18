# Bug reports for exercise1.py

Line: 3  
Problem: The condition `n % 2 == 1` checks if a number is odd, not even. For even numbers, the remainder when divided by 2 should be 0.  
Example: `is_even(4)` returns `False` (correct), but `is_even(2)` should return `True` and currently returns `False` because `2 % 2 == 0`, not `1`.  
Fix: `return n % 2 == 0`

Line: 8  
Problem: The function `rectangle_area` incorrectly returns the sum of width and height instead of the product.  
Example: `rectangle_area(4, 5)` returns `9` instead of `20`.  
Fix: `return width * height`

Line: 13  
Problem: The function `double(n)` adds 2 to `n`, but the docstring says "twice the number n", which means it should return `n * 2`.  
Example: `double(3)` returns `5` instead of `6`.  
Fix: `return n * 2`
