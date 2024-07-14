import time


def mtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        res=end_time-start_time
        print(f"Function {func.__name__} took {res:.3f} seconds")
        return result
    return wrapper


@mtime
def comsum(n):
    total = sum(range(n))
    return total

print(comsum(1000000))

mtime(comsum(10000))

# mtime(comsum(100000))

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/