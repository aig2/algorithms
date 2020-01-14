# A log(n) implementation of the power function
def fast_power(base,power,result):
	if power <= 1:
		result = result * base
		return result
	if power % 2 == 0:
		base = base * base
		power = power // 2
		return fast_power(base,power,result)
	else:
		power -= 1
		result = result * base
		power = power // 2
		base = base * base
		return fast_power(base,power,result)
