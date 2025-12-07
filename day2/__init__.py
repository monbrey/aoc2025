from utils.io import read_input_for


def read_input(strip: bool = True) -> str:
    """Return the contents of this module's `input.txt`."""
    return read_input_for(__file__, strip=strip)


def a():
    """Part a for day2."""
    data = read_input()
    if not data:
        return "input.txt not found or empty"
    
    total = 0
    for start, end in [r.split('-') for r in data.split(',')]:
        for num in range(int(start), int(end) + 1):
            s = str(num)
            if len(s) % 2 != 0: # uneven numbers cant be repeats
                continue
            mid = len(s) // 2
            if s[:mid] == s[mid:]:
                total += num

    return total


def b():
    """Part b for day2."""
    data = read_input()
    if not data:
        return "input.txt not found or empty"

    total = 0
    for start, end in [r.split('-') for r in data.split(',')]:
        for num in range(int(start), int(end) + 1):
            s = str(num)
            mid = len(s) // 2
            for part_length in range(1,mid+1):
                parts = (s[i:i+part_length] for i in range(0, len(s), part_length))
                if len(set(parts)) == 1:
                    total += num
                    break


    return total