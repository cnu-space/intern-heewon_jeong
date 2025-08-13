# accuracy 함수 테스트 예시

import math

from accuracy import accuracy

N = 1000000

pi_exact = math.pi
trial, pi_approx, correct_digits = accuracy(N)

print(f"{trial = } \n{pi_exact  = } \n{pi_approx = } \n{correct_digits = }")
