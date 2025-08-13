def buffon_needle_pi(trial, l=100, t=100):

    import math
    import random

    count = 0

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

    return l, t, π
