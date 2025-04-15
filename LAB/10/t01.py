def seq(x):
    # result = [x]
    # for k in range(2, n + 1):
    #     result.append(result[-1] * (x * (k - 1)/k))
    # return result
    i = 1
    prev_res = x
    while True:
        i += 1
        return (prev_res * (x * (i - 1)/ i))
        if (i >= 35):
            break



if __name__ == "__main__":
    for i in range (2, 100):
        print(seq(i))