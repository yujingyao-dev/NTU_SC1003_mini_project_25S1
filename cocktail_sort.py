def cocktail(nums):
    n = len(nums)
    start = 0
    end = n - 1
    for i in range(n-1):
        is_swaped = False
        if i % 2 == 0:
            for j in range(start, end):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    is_swaped = True
            end -= 1
        else:
            for j in range(end, start, -1):
                if nums[j-1] > nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
                    is_swaped = True
            start += 1
        if not is_swaped:
            break

if __name__ == "__main__":
    nums = [1,4,2,42,4,453,24,2]
    cocktail(nums)
    print(nums)
    