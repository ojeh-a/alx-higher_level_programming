#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))

    result = sub(a, b)
    print("{} - {} = {}".format(a, b, result))

    result = mul(a, b)
    print("{} * {} = {}".format(a, b, result))

    result = div(a, b)
    print("{} / {} = {}".format(a, b, result))
=======
=======
>>>>>>> de9e906 (update from ubuntu)
if __name__=="__main__":
	import calculator_1 as calc

	a = 10
	b = 5
	print(f"{a} + {b} = {calc.add(a, b)}")
	print(f"{a} - {b} = {calc.sub(a, b)}")
	print(f"{a} * {b} = {calc.mul(a, b)}")
	print(f"{a} / {b} = {calc.div(a, b)}")
<<<<<<< HEAD
>>>>>>> de9e906 (update from ubuntu)
=======
>>>>>>> de9e906 (update from ubuntu)
