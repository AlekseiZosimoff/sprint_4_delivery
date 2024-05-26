import sys


"""
25 май 2024, 21:24:27
114601820	
A
Python 3.12.1	
OK
-	
34ms
4.25Mb
"""
def platforms_counter(robots_masses: list, max_weight: int) -> int:
    left: int = 0
    right: int = len(robots_masses) - 1
    counter: int = 0

    while left <= right:
        if left == right:
            counter += 1
            break
        elif (left < right and
              robots_masses[left] + robots_masses[right] <= max_weight):
            counter += 1
            left += 1
            right -= 1
        elif (left < right and
              robots_masses[left] + robots_masses[right] > max_weight):
            counter += 1
            right -= 1
    return counter


def main():
    robots_masses = [int(i) for i in sys.stdin.readline().strip().split()]
    robots_masses = sorted(robots_masses)
    max_weight = int(sys.stdin.readline().strip())
    print(platforms_counter(robots_masses, max_weight))


if __name__ == '__main__':
    main()
