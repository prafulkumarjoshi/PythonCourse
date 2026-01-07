def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num%2==0:
        return False
    else:
        i=3
        divisors_count=1

        while(i <= num):
            if num % i == 0:
                divisors_count += 1
                divisors.append(i)
            
            if i == num and divisors_count ==2:
                return True
            
            i += 1
        if divisors_count > 2:
            return False
number = 1317
divisors=[1]
print(is_prime(number))
print(divisors)