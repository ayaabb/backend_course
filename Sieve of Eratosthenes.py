def sieve_of_eratosthenes(n):
    main_list = [num for num in range(4, n + 1)]
    prime_list = [2, 3]
    # find a prime num by checking if it divided by a smaller prime number
    # if it is divided remove it from main list ,, -1
    # if it is not divided, add it to prime list and remove it from main list
    # iterate over the main list and delete every num is divided by the new prime num
    # then repeat
    for i in range(len(main_list)):
        for p in prime_list:
            if main_list[i] != -1 and main_list[i] % p == 0:
                main_list[i] = -1
        if main_list[i] != -1:
            prime_list.append(main_list[i])
            tmp = main_list[i]
            for k in range(1, n // tmp + 1):
                if tmp * k in main_list:
                    main_list[main_list.index(tmp * k)] = -1
    print(f"The number of the prime numbers between 2 and {n} is: {len(prime_list)}")
    print(f"The prime numbers between between 2 and {n} are: {prime_list}")



if __name__ == '__main__':
    n = int(input("Enter a number to find the prime numbers between 2 and it: "))
    sieve_of_eratosthenes(n)
