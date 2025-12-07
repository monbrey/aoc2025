from utils.io import read_input_for


def read_input(strip: bool = True) -> str:
    return read_input_for(__file__, strip=strip)


def a():
    data = read_input()
    if not data:
        return "input.txt not found or empty"
    
    point = 50
    password = 0
    for line in data.splitlines():
        if line[0] == "L":
            point = point - int(line[1:])
            while point < 0:
                point += 100
        elif line[0] == "R":
            point += int(line[1:])
            while point >= 100:
                point -= 100
        if point == 0:
            password += 1

    return password


def b():
    data = read_input()
    if not data:
        return "input.txt not found or empty"
    
    point = 50
    password = 0
    for line in data.splitlines():
        rotation = int(line[1:])
        # immediately count any full rotations and grab the rest
        password += rotation // 100
        rotation = rotation % 100

        next_point = point - rotation if line[0] == "L" else point + rotation
        if (next_point <= 0 and point > 0) or (next_point >= 100 and point < 100):
            # we've crossed or landed on zero
            password += 1

        point = next_point + 100 if next_point < 0 else next_point - 100 if next_point >= 100 else next_point
        
    return password