# shell sort implemeting in python
import pdb


def shell_sort(bef_list):
    n = len(bef_list)
    # 初始步長
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            # 每个步長進行插入排序
            temp = bef_list[i]
            j = i
            # 插入排序
            while j >= 0 and j - gap >= 0 and bef_list[j - gap] > temp:
                bef_list[j] = bef_list[j - gap]
                j -= gap
            bef_list[j] = temp
        # 得到新的步長
        gap = gap // 2
    print(bef_list)
    return bef_list


if __name__ == "__main__":
    bef_list = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
    shell_sort(bef_list)
