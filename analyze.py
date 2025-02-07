import numpy as np
from sklearn.datasets import load_wine

# 데이터셋 로드
wine_data = load_wine()
data = wine_data.data
features = wine_data.feature_names

# 데이터셋의 행(row)과 열(column) 개수 출력
rows, columns = data.shape
print(f"행(row): {rows}, 열(column): {columns}")

# 각 특성의 평균(mean)과 표준편차(std) 계산
means = np.mean(data, axis=0)
stds = np.std(data, axis=0)

# 특정 특성(예: alcohol)의 최대값, 최소값
alcohol_column_index = features.index('alcohol')  # 'alcohol' 특성의 인덱스 찾기
alcohol_values = data[:, alcohol_column_index]
alcohol_max = np.max(alcohol_values)
alcohol_min = np.min(alcohol_values)

# 결과를 output.txt 파일에 저장
with open('output.txt', 'w') as file:
    file.write(f"행(row): {rows}, 열(column): {columns}\n")
    file.write("\n각 특성의 평균 (mean)과 표준편차 (std):\n")
    for feature, mean, std in zip(features, means, stds):
        file.write(f"{feature} - 평균: {mean:.2f}, 표준편차: {std:.2f}\n")
    file.write(f"\n'alcohol' 특성의 최대값: {alcohol_max:.2f}, 최소값: {alcohol_min:.2f}\n")

print("분석 결과가 output.txt에 저장되었습니다.")

