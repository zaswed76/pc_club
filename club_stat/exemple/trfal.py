lst = [(1, 0, 1), (1, 3, 2), (1, 3, 3), (2, 0, 1), (2, 0, 2),
       (2, 3, 3), (2, 3, 4), (3, 0, 1), (3, 0, 2)]


class Akm(list):
    def __init__(self):
        super().__init__()

    def __contains__(self, item):
        for line in self:
            if item[0] == line[0] and item[1] == line[1]:
                return True


def sort_seq(lst):
    akm = Akm()
    for line in lst:
        if not (line[0], line[1]) in akm:
            akm.append(line)
    return akm


def sort_seq2(lst):
    akm = Akm()
    akm = [x for x in lst if not x[0] in akm]
    return akm


if __name__ == '__main__':
    print(sort_seq(lst))
