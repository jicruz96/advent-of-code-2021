"""See `README.md` for details"""
from typing import List


def solution(elements: List[int], window_size: int):
    count = 0
    for i in range(len(elements) - window_size):
        if elements[i + window_size] > elements[i]:
            count += 1
    print(count)


if __name__ == "__main__":

    # Get input, transform to list of integers.
    with open("puzzle_input.txt", "r") as fp:
        sonar_sweep_data = [int(depth_reading) for depth_reading in fp.readlines()]

    # Problem 1: Increasing elements in sonar sweep data
    solution(sonar_sweep_data, 1)

    # Problem 2: Increasing elements in sonar sweep data in sliding window of 3
    solution(sonar_sweep_data, 3)
