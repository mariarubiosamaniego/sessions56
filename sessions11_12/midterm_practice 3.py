def get_divisors_number(num):
    """
    return a list of all divisors of num
    :param num: the nuber to check
    :return: list of all divisors of num
    """
    divisors = []
    for i in range(1, num +1):  #we add +1 because range doesn't include num
        if num % i == 0:
            divisors.append(i)
    return divisors
print(get_divisors_number(108))
