from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file_csv:
        list_dict = list(
            csv.DictReader(file_csv, delimiter=",", quotechar='"')
        )
    return list_dict
