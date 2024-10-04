# target의 위치
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:  # 등호
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid

    return -1


# 중복값중 맨 왼쪽을 찾는 버전
def find_first(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            result = mid  # 값이 같을 경우 일단 결과를 저장
            right = mid - 1  # 더 왼쪽에 같은 값이 있는지 계속 탐색

    return result


# 중복값중 맨 오른쪽을 찾는 버전
def find_last(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            result = mid  # 값이 같을 경우 일단 결과를 저장
            left = mid + 1  # 더 오른쪽에 같은 값이 있는지 계속 탐색

    return result


# target 이상인 첫번째 값의 위치
def lower_bound(arr, target):
    left = 0
    right = len(arr)

    while left < right:  # 부등호
        mid = (left + right) // 2
        if arr[mid] < target:  # 부등호
            left = mid + 1
        else:
            right = mid

    return left


# target 초과인 첫번째 값의 위치
def upper_bound(arr, target):
    left = 0
    right = len(arr)

    while left < right:  # 부등호
        mid = (left + right) // 2
        if arr[mid] <= target:  # 등호
            left = mid + 1
        else:
            right = mid

    return left


def test_binary_search_functions():
    arr = [1, 2, 4, 4, 5, 7, 9, 10]  # 정렬된 배열

    print("binary_search 테스트")
    print(binary_search(arr, 4))  # 예상 출력: 2 또는 3 (4가 있는 첫 번째 인덱스)
    print(binary_search(arr, 6))  # 예상 출력: -1 (배열에 없음)
    print(binary_search(arr, 1))  # 예상 출력: 0 (1은 첫 번째 위치)
    print(binary_search(arr, 10))  # 예상 출력: 7 (10은 마지막 위치)

    print("\nlower_bound 테스트")
    print(lower_bound(arr, 4))  # 예상 출력: 2 (4 이상인 첫 번째 값의 위치)
    print(lower_bound(arr, 6))  # 예상 출력: 5 (6 이상의 첫 번째 값의 위치)
    print(lower_bound(arr, 0))  # 예상 출력: 0 (0 이상인 첫 번째 값의 위치)
    print(
        lower_bound(arr, 11)
    )  # 예상 출력: 8 (11 이상인 값이 없으므로 배열의 끝 인덱스)

    print("\nupper_bound 테스트")
    print(upper_bound(arr, 4))  # 예상 출력: 4 (4보다 큰 첫 번째 값의 위치)
    print(upper_bound(arr, 6))  # 예상 출력: 5 (6보다 큰 첫 번째 값의 위치)
    print(upper_bound(arr, 0))  # 예상 출력: 0 (0보다 큰 첫 번째 값의 위치)
    print(
        upper_bound(arr, 10)
    )  # 예상 출력: 8 (10보다 큰 값이 없으므로 배열의 끝 인덱스)


test_binary_search_functions()

"""
- 주의: 정렬된 배열에만 사용 가능
"""
