import pandas as pd


def my_fist_function():
    print(2 + 3)


def my_second_function(x, y):
    print(my_fist_function(x, y))


dict_var = {
    "a": [1, 2, 3],
    "b": [2, 3, 4]
}


def read_pandas(dict_input):
    df = pd.DataFrame(dict_input)

    print(df)
