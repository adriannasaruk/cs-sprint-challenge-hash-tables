def has_negatives(a):
    cache = {}

    result = []

    for i in a:
        cache[i] = i

        if i != 0 and -i in cache:
            print(i)
            result.append(abs(i)) 
    # Your code here

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
