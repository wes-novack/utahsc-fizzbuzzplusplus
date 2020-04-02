def fizzbuzz(num):
    if _divisible_by(num, 3) and _divisible_by(num, 5):
        return "fizzbuzz"
    elif _divisible_by(num, 3):
        return "fizz"
    elif _divisible_by(num, 5):
        return "buzz"
    return str(num)


def _divisible_by(num, divisor):
    return num%divisor == 0