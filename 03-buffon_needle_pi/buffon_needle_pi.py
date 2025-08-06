import math
import random


def buffon_needle_pi(trial):
    count = 0
    l = random.randint(1, 100)  # 바늘의 길이
    t = random.randint(1, 100)  # 두 평행선 사이 간격
    for n in range(trial):
        θ = random.uniform(0, math.pi)
        x = random.uniform(0, t / 2)
        if x <= (l / 2) * math.sin(θ):
            count += 1
    if trial != 0:
        P = count / trial
    if l <= t:
        π = (2 * l) / (P * t)
    else:
        π = (2 * (-math.sqrt(l**2 - t**2) + l - t * math.asin(t / l))) / (t * (P - 1))

    return f"l: {l}, t: {t}, pi: {π:.2f}"


result = buffon_needle_pi(10000)
print(result)
