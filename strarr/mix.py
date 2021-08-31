def prod(nums):
    total = 1
    res = []
    for i, n in enumerate(nums):
      total *= n
    print total

    for i, n in enumerate(nums):
      res.append(total/n)
    
    return res

if __name__ == '__main__':
    print prod([1,2,3,4])
    # print prod([1,5, 3, 2, 8])