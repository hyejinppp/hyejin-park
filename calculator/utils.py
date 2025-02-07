# utils.py

import math

def round_result(value, precision=2):
    """결과값을 지정된 정밀도로 반올림"""
    return round(value, precision)

def convert_to_radians(angle, unit='degree'):
    """각도를 라디안으로 변환"""
    if unit == 'degree':
        return math.radians(angle)
    elif unit == 'radian':
        return angle  # 이미 라디안이면 그대로 반환
    else:
        return "Invalid unit"
