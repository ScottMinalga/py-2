import time
#
# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @logger
# def say_hello(name):
#     return f"Hello, {name}!"
#
# print(say_hello("Alice"))

# def finddiff():
#     def timeit(func):
#         def wrapper(*args, **kwargs):
#             start_time = time.time()
#             result = func(*args)
#             end_time = time.time()
#             print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
#             return result
#         return wrapper
#
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper
@timeit
def compute_sum(n):
    """Function to compute the sum of numbers from 1 to n"""
    return sum(range(1, n + 1))

# Example usage
print(compute_sum(1000000000))


def compare_with(func_to_compare):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Time the first function
            start_time_func = time.time()
            result_func = func(*args, **kwargs)
            end_time_func = time.time()
            time_func = end_time_func - start_time_func

            # Time the second function (the one to compare with)
            start_time_compare = time.time()
            result_compare = func_to_compare(*args, **kwargs)
            end_time_compare = time.time()
            time_compare = end_time_compare - start_time_compare

            # Compare and print results
            faster = "first function" if time_func < time_compare else "second function"
            print(f"Average execution time of {func.__name__}: {time_func} seconds.")
            print(f"Average execution time of {func_to_compare.__name__}: {time_compare} seconds.")
            print(f"The {faster} was faster.")

            return result_func, result_compare

        return wrapper

    return decorator


# Usage example
def compute_sum(n):
    """Function to compute the sum of numbers from 1 to n"""
    return sum(range(1, n + 1))

@compare_with(compute_sum)
def compute_product(n):
    """Function to compute the product of numbers from 1 to n"""
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

# Running the comparison
compute_product(100)