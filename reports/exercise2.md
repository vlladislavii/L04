# Bug reports for exercise2.py

Line: 13
Problem: The clamp function incorrectly uses `max(low, min(x, low))` which results in `min(x, low)` being compared with `low` again in the max, making it always return `low` if `x < low`. This is logically incorrect. It should clamp `x` between `low` and `high`, not just to `low`.
Example: For x=3, low=1, high=10, the function returns max(1, min(3,1)) = max(1,1) = 1, which is correct. But for x=15, low=1, high=10, it returns max(1, min(15,1)) = 1, which is wrong — should return 10.
Fix: return max(low, min(x, high))

Line: 3
Problem: The docstring says "True if the grade is 5 or more", which means grade >= 5. However, the function uses `grade > 5`, which means strictly greater than 5, so it fails for grade exactly 5.
Example: For grade=5, expected output is True (since 5 is "5 or more"), but actual output is False.
Fix: return grade >= 5
