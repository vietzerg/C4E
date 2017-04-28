### What is nested list?
A list within another list is said to be **nested**.

### Can a list store both integers and strings in it?

Yes, definitely.

### 11.22 Exercises
#### What is the Python interpreter’s response to the following?
```python
list(range(10, 0, -2))
```
> `>>> [10, 8, 6, 4, 2]`
#### The three arguments to the range function are `start`, `stop`, and `step`, respectively. In this example, `start` is greater than `stop`. What happens if `start` < `stop` and `step` < 0? Write a rule for the relationships among `start`, `stop`, and `step`.
According to Python's API documents on `range` type:
> A range object will be empty if r[0] does not meet the value constraint.

Also,

> For a positive *step*, the contents of a range `r` are determined by the formula `r[i] = start + step*i` where `i >= 0` and `r[i] < stop`.

> For a negative *step*, the contents of the range are still determined by the formula `r[i] = start + step*i`, but the constraints are `i >= 0` and `r[i] > stop`.

#### Consider this fragment of code:
```python
import turtle
tess = turtle.Turtle()
alex = tess
alex.color("hotpink")
```
#### Does this fragment create one or two turtle instances? Does setting the color of `alex` also change the color of `tess`? Explain in detail.

The line `tess = turtle.Turtle()` creates an instance (an object of `Turtle` class). The next line, `alex = tess` does not create a new object, but instead it refers to the object that was previously created under the name `tess`.

Therefore, setting the color of `alex` does change the color of `tess`.
