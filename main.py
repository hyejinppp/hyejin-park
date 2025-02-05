# main.py

import calculator  # calculator 패키지를 임포트

# 기본 계산기 사용
calc = calculator.Calculator()
print(calc.add(10, 5))  # 15
print(calc.subtract(10, 5))  # 5

# 공학용 계산기 사용
eng_calc = calculator.EngineeringCalculator()
print(eng_calc.square_root(9))  # 3.0
print(eng_calc.power(2, 3))  # 8.0
print(eng_calc.log(10))  # 자연로그 값

# 유틸리티 함수 사용
result = calculator.round_result(3.14159, 3)
print(result)  # 3.142

angle_in_degrees = 90
angle_in_radians = calculator.convert_to_radians(angle_in_degrees)
print(angle_in_radians)  # 1.5708 (라디안 값)
