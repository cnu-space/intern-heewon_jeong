def accuracy(trial, **lengths):

    import math

    from est_pi import buffon_needle_pi

    result = buffon_needle_pi(
        trial, **lengths
    )  # length: { l: _ , t: _ } / 디폴트:  l=100, t=100
    l, t, π = result

    pi_true = math.pi
    pi_approx = result[2]
    delta = pi_true - pi_approx
    rel_error = abs(delta / pi_true) * 100  # 백분율로 나타낸 상대 오차

    # n_sig = 유효숫자의 개수 / 10**(2 - n_sig) <= rel_error
    n_sig = math.floor(
        (2 - math.log10(rel_error))
    )  # math.floor - n_sig는 결과값보다 작은 정수

    return trial, pi_approx, n_sig
