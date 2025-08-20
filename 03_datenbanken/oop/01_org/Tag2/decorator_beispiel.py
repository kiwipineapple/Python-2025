import time


def time_it(fn):
    def wrapper():
        start = time.perf_counter()
        fn()
        end = time.perf_counter()
        print("say_hello hat gedauert:s", end - start)

    return wrapper


@time_it
def calculate():
    print("los gehts")
    [x for x in range(10**7)]
    print("fertig")


# start = time.perf_counter()
# calculate = time_it(calculate)  schreibt man @time_it
calculate()
# end = time.perf_counter()

# print("say_hello hat gedauert:s", end - start)

# print(calculate)
