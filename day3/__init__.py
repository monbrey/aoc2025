from utils.io import read_input_for


def read_input(strip: bool = True) -> str:
    """Return the contents of this module's `input.txt`."""
    return read_input_for(__file__, strip=strip)


def a():
    """Part a for day3."""
    data = read_input()
    if not data:
        return "input.txt not found or empty"
    
    joltage = 0
    
    for line in data.splitlines():
        # find the highest number that isn't in the last place
        high = max([int(x) for x in line[0:-1]])
        high_index = line.find(str(high))
        next = max([int(x) for x in line[high_index+1:]])
        joltage += high*10 + next

    return joltage


def b():
    """Part b for day3."""
    data = read_input()
    if not data:
        return "input.txt not found or empty"
    
    joltage = 0
    
    for line in data.splitlines():
        lj = ''
        start, end = 0, -11
        while end <= 0:
            high = max([int(x) for x in (line[start:end] if end < 0 else line[start:])])
            high_index = line.find(str(high), start, end if end < 0 else None)
            lj += str(high)
            start = high_index + 1
            end += 1

        joltage += int(lj)

    return joltage
