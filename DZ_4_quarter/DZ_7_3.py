import random


def median_search(lst, left, right):
    lst = lst.copy()
    ind = len(lst) // 2

    if left >= right:
        return lst[ind]

    pillar = lst[ind]
    l = left
    r = right

    while l <= r:
        while lst[l] < pillar:
            l += 1
        while lst[r] > pillar:
            r -= 1
        if l <= r:
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1
    if ind < l:
        lst[ind] = median_search(lst, left, r)
    elif r < ind:
        lst[ind] = median_search(lst, l, right)
    return lst[ind]


def merge_sort(arr):
    def merge(fst, snd):
        res = []
        l, r = 0, 0

        while l < len(fst) and r < len(snd):
            if fst[l] < snd[r]:
                res.append(fst[l])
                l += 1
            else:
                res.append(snd[r])
                r += 1
        res.extend(fst[l:] if l < len(fst) else snd[r:])
        return res

    def div_half(lst):

        if len(lst) == 1:
            return lst
        elif len(lst) == 2:
            return lst if lst[0] <= lst[1] else lst[::-1]
        else:
            return merge(div_half(lst[:len(lst) // 2]), div_half(lst[len(lst) // 2:]))

    return div_half(arr)


m = random.randint(0, 50)

array = [random.randint(0, 50) for _ in range(2 * m + 1)]
median = median_search(array, 0, len(array) - 1)
print(f'Сгенерирован массив чисел из {2 * m + 1}  элементов: \n {array}\n')

print(f'Медиана: {median} \n'
      f'по левую и правую стороны от медианы находится по {len(array) // 2} элементов\n'
      f'\nОтсортированный массив:\n {merge_sort(array)} '
      )
