import numpy as np

file1 = 'mars_base_main_parts-001.csv'
file2 = 'mars_base_main_parts-002.csv'
file3 = 'mars_base_main_parts-003.csv'

arr1 = np.genfromtxt(file1, delimiter=',', skip_header=1, usecols=1)
arr2 = np.genfromtxt(file2, delimiter=',', skip_header=1, usecols=1)
arr3 = np.genfromtxt(file3, delimiter=',', skip_header=1, usecols=1)

parts = np.concatenate((arr1, arr2, arr3))
parts_to_work_on = parts[parts < 50]

try:
    np.savetxt('parts_to_work_on.csv', parts_to_work_on.reshape(-1, 1), delimiter=',', fmt='%.2f')
except Exception as e:
    print('파일 저장 오류: ', e)

try:
    parts2 = np.loadtxt('parts_to_work_on.csv', delimiter=',')
    parts3 = parts2.T
    print(parts3)
except Exception as e:
    print('전치행렬 오류: ', e)

mean_parts = np.mean(parts)
print("전체 parts 배열의 평균값:", mean_parts)
