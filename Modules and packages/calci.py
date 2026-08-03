def add(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def mul(a: int, b: int) -> int:
    return a * b


def div(a: int, b: int) -> float:
    return a / b


PI = 3.142
DIST_FROM_MOON = 10000

if __name__ == "__main__":
    print("Start")
    result = add(10, 20)
    print(f"result = {result}")
    print("End")
    print(__name__)
