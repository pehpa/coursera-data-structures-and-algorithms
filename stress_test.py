import time
import random


def stress_test(func, n_param , max_n=1000, n_test=100):
    """_summary_

    Args:
        func (_type_): _description_
        n_param (_type_): _description_
        max_n (int, optional): _description_. Defaults to 1000.
        n_test (int, optional): _description_. Defaults to 100.
    """
    average_times = []
    for test in range(n_test):
        print("run {:>{}}/{:>{}}".format(test+1, len(str(n_test)), n_test, len(str(n_test))), end=" | ")

        params=[]
        for i in range(n_param):
            params.append(int(random.random() * max_n)+1)

        st = time.time()
        output_n = func(*params)
        et = time.time()
        average_times.append(et - st)

        print(params, output_n)

        # print("gcd for {:>{}} and {:>{}} is {}".format(rand_n1, len(str(n_test)), rand_n2, len(str(n_test)), output_n))

    print("average computation time over {} runs is {:.1e} s".format(len(average_times), sum(average_times)/len(average_times)))
    # print(["{:.1e}".format(x) for x in average_times])
