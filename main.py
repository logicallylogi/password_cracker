from typing import Dict
from time import time_ns


def password_check(password: str) -> dict[str, int | bool] | dict[str, str | bool] | dict[str, bool | None]:
    for i in range(1920, 2030):
        if password == i:
            return {'cracked': True, 'password': i}

    for o in ["passlist.txt", "2ndpasslist.txt", "piotrcki-wordlist.txt"]:
        with open(o, "r", encoding="utf-8") as f:
            list1 = f.readlines()
            for i in list1:
                if password == i:
                    return {'cracked': True, 'password': i}

    return {"cracked": False, "password": None}


def password_test(password: str) -> None:
    start_time = time_ns()
    pswd = password_check(password)['password']
    end_time = time_ns()

    print(f"Password: {pswd} \nTook: {(end_time - start_time) / 1000000} ms")

for i in ["Amber95", "death66", "lawyerSeries62"]:
    password_test(i)