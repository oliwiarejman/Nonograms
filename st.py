import time
from main import nonogram_ga
from main2 import nonogram_ga2
# nonograms example

nonogram_1_1 = [
    [[1,1,1], [3], [5], [3], [1,1,1]],
    [[1,1,1], [3], [5], [3], [1,1,1]]
    ]
nonogram_1_2 = [
    [[2], [1, 1], [1, 1], [1, 1], [2]],
    [[1,1], [1, 1,1], [1, 1], [1,1], [1]]
]

nonogram_1_3 = [
    [[1], [2, 1], [5], [2, 1], [1]],
    [[1], [3], [5], [3], [1]]
]

nonogram_2_1 = [
    [[0], [2], [3], [1], [1, 2, 2], [1, 2, 2], [1, 2], [6], [4], [0]],
    [[6], [2, 2], [2, 2], [2], [3], [4], [2], [0], [2], [2]]
]

nonogram_2_2 = [
    [[1], [4, 2], [1, 2], [6, 1], [1, 2, 1], [5, 1, 1], [1, 2, 1, 1], [3, 1, 2], [1, 5], [2]],
    [[6], [1, 1, 1, 1], [2, 1, 2], [1, 1, 2, 1], [1, 1, 4], [1, 2, 1], [8], [1, 1], [1, 4], [2]]
]

nonogram_2_3 = [
    [[3,1],[5,2],[3,2,1],[4,1,1],[10],[1,7],[3,1,1,1],[3,1,1],[4,1],[2,2]],
    [[6],[4,3],[5,4],[2,3,2],[3,5],[5],[3],[2],[1,2,1],[10]]
]


nonogram_3_1 = [
    [[1,2,2], [2,2,4,2], [2,3,6], [2,2,1,2], [3,1], [1,3], [1,1,7],[7,2],[1,10], [5,1], [5,2], [5, 1], [3,9,1],[2,3,1],[5]],
    [[4,1,1],[3,1],[5],[1,1,1,3],[4,5],[4,8],[7],[1,2,1],[2,4,1],[3,4,1],[8,5],[1,5,3],[1,1,1,3],[4,3,1],[4,2,3]]
]

nonogram_3_2 = [
    [[2],[3],[1,1],[1,1,2,1],[2,2,1,1],[2,6,2],[1,2,2],[1,3,2],[3,2,5],[2,1,1],[1,1],[4,2,1],[2,2,2,2],[1,1,2,5],[2,5]],
    [[3],[4,2,1],[3,1,1],[3,1,2,1],[2,1,2],[4,2,2],[2,2,2],[1,3,1],[2,2,1],[4,3],[1,1,2,2],[1,1,1],[1,1,1],[5,2],[3,2,3]]
]

nonogram_3_3 = [
    [[2,2],[7],[7,2],[7,2],[3,5,1],[5,3,2],[6,1,2],[6,4],[6,1],[5,3],[3,5],[7],[7],[7],[2,2]],
    [[2,2],[7],[7],[7],[3,5,3],[5,3,5],[6,1,6],[6,6],[6,1,6],[5,1,5],[3,1,3],[2],[2],[4],[2]]
]

def res(ga):
    start_time1_1= time.time()
    res1_1 = ga(nonogram_1_1, f"{ga.__name__}_1_1")
    end_time1_1 = time.time()
    t1_1= end_time1_1- start_time1_1

    start_time1_2 = time.time()
    res1_2 =ga(nonogram_1_2, f"{ga.__name__}_1_2")
    end_time1_2 = time.time()
    t1_2 = end_time1_2 - start_time1_2

    start_time1_3 = time.time()
    res1_3 =ga(nonogram_1_3, f"{ga.__name__}_1_3")
    end_time1_3 = time.time()
    t1_3 = end_time1_3 - start_time1_2


    start_time2_1 = time.time()
    res2_1 =ga(nonogram_2_1, f"{ga.__name__}_2_1")
    end_time2_1 = time.time()
    t2_1 = end_time2_1 - start_time2_1

    start_time2_2 = time.time()
    res2_2 =ga(nonogram_2_2, f"{ga.__name__}_2_2")
    end_time2_2 = time.time()
    t2_2 = end_time2_2 - start_time2_2

    start_time2_3 = time.time()
    res2_3 =ga(nonogram_2_3, f"{ga.__name__}_2_3")
    end_time2_3 = time.time()
    t2_3 = end_time2_3 - start_time2_3


    start_time3_1 = time.time()
    res3_1 =ga(nonogram_3_1, f"{ga.__name__}_3_1")
    end_time3_1 = time.time()
    t3_1 = end_time3_1 - start_time3_1

    start_time3_2 = time.time()
    res3_2 =ga(nonogram_3_2, f"{ga.__name__}_3_2")
    end_time3_2 = time.time()
    t3_2 = end_time3_2 - start_time3_1

    start_time3_3 = time.time()
    res3_3 = ga(nonogram_3_3, f"{ga.__name__}_3_3")
    end_time3_3 = time.time()
    t3_3 = end_time3_3 - start_time3_3

    print("statistics:")
    print(f"algorytm {ga.__name__}")
    print("5x5")
    print(f"accuracy: {res1_1}, {res1_2}, {res1_3}; average {(res1_1+res1_2+res1_3)/3}")
    print(f"time: {t1_1}, {t1_2}, {t1_3}; average {(t1_1+t1_2+t1_3)/3}")
    print()
    print("10x10")
    print(f"accuracy: {res2_1}, {res2_2}, {res2_3}; average {(res2_1+res2_2+res2_3)/3}")
    print(f"time: {t2_1}, {t2_2}, {t2_3}; average {(t2_1+t2_2+t2_3)/3}")
    print()
    print("15x15")
    print(f"accuracy: {res3_1}, {res3_2}, {res3_3}; average {(res3_1+res3_2+res3_3)/3}")
    print(f"time: {t3_1}, {t3_2}, {t3_3}; average {(t3_1+t3_2+t3_3)/3}")


res(nonogram_ga)
res(nonogram_ga2)