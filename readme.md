# Plus-minus calculator
Recursive calculator that parse string to math expression

## How it works
1. Tokenize text to words(function names), signs(`+-*/^`), brackets(`()[]{}`) and numbers
2. Replace all brackets by lists
3. Replace all commas by left-side and right-side lists
4. Replace all function names and signs by their build-in functions(if not defined then `None`)
5. Create calculation binary tree

## How to use it
Check `test.py` or look this example:
```
result = expression_tree.make_expression_array('2/ln(e^(1+log(10, 100)))*(6-2^2)*1/abs(6-3^2)*ln(e^(9*4))')
tree = expression_tree.make_expression_tree(result)
print(tree.calc())
```

output: `16.0`

## Supported constants

* `pi`: 3.14159265359... (`math.pi`)
* `e`: 2.71828182846... (`math.e`)

## Supported functions

* `sin(x)`: sine
* `cos(x)`: cosine
* `tan(x)`, `tg(x)`: tangent
* `cot(x)`, `ctan(x)`, `ctg(x)`: cotangent
* `log(a, x)`: logarithm to base `a`
* `ln(x)`: natural logarithm (to base `e`)
* `lg(x)`: common logarithm (to base 10)
* `abs(x)`: absolute value (modulus)
