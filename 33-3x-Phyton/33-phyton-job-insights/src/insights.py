from src.jobs import read


def get_unique_job_types(path):
    list_dict = read(path)
    jobs_fiter = []
    for job in list_dict:
        if not job["job_type"] in jobs_fiter:
            jobs_fiter.append(job["job_type"])
    return jobs_fiter


def filter_by_job_type(jobs, job_type):
    jobs_filter = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filter.append(job)
    return jobs_filter


def get_unique_industries(path):
    list_dict = read(path)
    industries_filter = []
    for ind in list_dict:
        if not ind["industry"] in industries_filter and ind["industry"] != "":
            industries_filter.append(ind["industry"])
    return industries_filter


def filter_by_industry(jobs, industry):
    job_filter_by_ind = []
    for job in jobs:
        if job["industry"] == industry:
            job_filter_by_ind.append(job)
    return job_filter_by_ind


def get_max_salary(path):
    list_dict = read(path)
    salary_max = 0
    salary_list = []

    for salary in list_dict:
        if salary["max_salary"].isdigit():
            salary_list.append(int(salary["max_salary"]))

    for salary in salary_list:
        if salary > salary_max:
            salary_max = salary

    return salary_max


def get_min_salary(path):
    list_dict = read(path)
    salary_min = 100000
    salary_list = []

    for salary in list_dict:
        if salary["min_salary"].isdigit():
            salary_list.append(int(salary["min_salary"]))

    for salary in salary_list:
        if salary < salary_min:
            salary_min = salary

    return salary_min


def matches_salary_range(job, salary):
    if not ("min_salary" in job and "max_salary" in job):
        raise ValueError(
            "job['min_salary'] or job['max_salary'] doesn't exists"
        )
    elif not (
        type(job["min_salary"]) is int or type(job["max_salary"]) is int
    ):
        raise ValueError(
            "job['min_salary'] or job['max_salary'] aren't valid integers"
        )
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError(
            "job['min_salary'] is greather than job['max_salary']"
        )
    elif not (type(salary) is int):
        raise ValueError("salary isn't a valid integer")
    else:
        return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
