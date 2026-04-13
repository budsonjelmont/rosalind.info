from lgis import lis, lds

def test_lis_0():
    res_lis = lis([9, 1, 10, 9, 7, 4], 6)
    expect_lis = [1, 4]
    assert res_lis == expect_lis

def test_lds_0():
    res_lds = lds([9, 1, 10, 9, 7, 4], 6)
    expect_lds = [10, 9, 7, 4]
    assert res_lds == expect_lds

def test_lis_1():
    res_lis = lis([3, 0, 2, 4, 8], 5)
    expect_lis = [0, 2, 4, 8]
    assert res_lis == expect_lis

def test_lds_1():
    res_lds = lds([3, 0, 2, 4, 8], 5)
    expect_lds = [3, 2]
    assert res_lds == expect_lds

def test_lis_2():
    res_lis = lis([1, 9, 2, 3], 4)
    expect_lis = [1, 2, 3]
    assert res_lis == expect_lis

def test_lds_2():
    res_lds = lds([1, 9, 2, 3], 4)
    expect_lds = [9, 3]
    assert res_lds == expect_lds

def test_lis_3():
    res_lis = lis([1, 9, 1, 2, 3], 5)
    expect_lis = [1, 2, 3]
    assert res_lis == expect_lis

def test_lds_3():
    res_lds = lds([1, 9, 1, 2, 3], 5)
    expect_lds = [9, 3]
    assert res_lds == expect_lds

def test_lis_4():
    res_lis = lis([2, 8, 9, 5, 6, 7, 1], 7)
    expect_lis = [2, 5, 6, 7]
    assert res_lis == expect_lis

def test_lds_4():
    res_lds = lds([2, 8, 9, 5, 6, 7, 1], 7)
    expect_lds = [9, 7, 1]
    assert res_lds == expect_lds

def test_lis_5():
    res_lis = lis([3, 5, 7, 3, 5, 7], 6)
    expect_lis = [3, 5, 7]
    assert res_lis == expect_lis

def test_lds_5():
    res_lds = lds([3, 5, 7, 3, 5, 7], 6)
    expect_lds = [7, 5]
    assert res_lds == expect_lds

def test_lis_6():
    res_lis = lis([3, 5, 0, 1, 2 , -1, 8], 7)
    expect_lis = [0, 1, 2, 8]
    assert res_lis == expect_lis

def test_lds_6():
    res_lds = lds([3, 5, 0, 1, 2 , -1, 8], 7)
    expect_lds = [5, 2, -1]
    assert res_lds == expect_lds

if __name__ == "__main__":
    test_lds_4()