"""Fore more info look README.md"""


def make_change(amount: str) -> dict:
    """Function"""

    sum_ = 0.0
    sum_ = float(amount.split()[0]) * 100
    if sum_ % 5 > 0:
        sum_ += 5 - sum_ % 5 if sum_ % 10 > 5 else sum_ % 5 - 5
    answer = {1: 0, 2: 0, 50: 0, 25: 0, 10: 0, 5: 0}
    while sum_ > 0:
        if sum_ - 200 >= 0:
            sum_ -= 200
            answer[2] += 1
        elif sum_ - 100 >= 0:
            sum_ -= 100
            answer[1] += 1
        elif sum_ - 50 >= 0:
            sum_ -= 50
            answer[50] += 1
        elif sum_ - 25 >= 0:
            sum_ -= 25
            answer[25] += 1
        elif sum_ - 10 >= 0:
            sum_ -= 10
            answer[10] += 1
        elif sum_ - 5 >= 0:
            sum_ -= 5
            answer[5] += 1

    return answer


if __name__ == '__main__':
    print(make_change(input()))
