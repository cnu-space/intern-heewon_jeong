def accuracy(trial):

    import math

    from buffon_needle_pi import buffon_needle_pi

    result = buffon_needle_pi(trial)
    l, t, π = result

    pi = f"{math.pi :.6f}"
    my_pi = f"{π :.6f}"
    digits = 0

    for i in range(len(my_pi)):

        if my_pi[i] != ".":

            if my_pi[i] == pi[i]:
                digits += 1
            else:
                break

    return float(my_pi), digits


for n in [2**i for i in range(7, 20 + 1)]:
    pi, digits = accuracy(n)
    print("n = {:10d}: pi = {}, digits = {}".format(n, pi, digits))
