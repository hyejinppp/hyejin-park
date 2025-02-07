# engineering.py

import math
from .basic import Calculator  # 상대 경로로 기본 계산기 클래스 임포트

class EngineeringCalculator(Calculator):
    """공학용 계산기 클래스"""
    
    def square_root(self, a):
        if a < 0:
            return "Cannot take square root of negative number"
        return math.sqrt(a)
    
    def power(self, a, b):
        return math.pow(a, b)
    
    def log(self, a):
        if a <= 0:
            return "Logarithm undefined for non-positive numbers"
        return math.log(a)
