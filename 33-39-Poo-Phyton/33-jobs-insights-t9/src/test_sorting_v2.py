# from src.sorting import sort_by
# from ...src.sorting import sort_by
# from ...src import sort_by
from sorting import sort_by

# print(type(sort_by))


def db_test():
    return [
        {"min_salary": 1000, "max_salary": 2500, "date_posted": "2021-01-10"},
        {"min_salary": 3000, "max_salary": 4500, "date_posted": "2021-02-20"},
        {"min_salary": 5000, "max_salary": 7500, "date_posted": "2021-03-30"},
    ]


def test_sort_by_criteria(db_test, sort_by):
    # print(type(db_test))
    # print(type(sort_by))
    data = db_test()
    # print(data)
    sort_by(data, "min_salary")
    assert [el["min_salary"] for el in data] == [1000, 3000, 5000]

    sort_by(data, "max_salary")
    assert [el["max_salary"] for el in data] == [7500, 4500, 2500]

    sort_by(data, "date_posted")
    assert [el["date_posted"] for el in data] == [
        "2021-03-30",
        "2021-02-20",
        "2021-01-10",
    ]


test_sort_by_criteria(db_test, sort_by)
