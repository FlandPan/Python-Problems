def hash(num):
    return num*47%101

def create_list(filename):
    with open(filename, 'r') as file:
        size = int(file.readline())
        nums = []
        for i in range(0, size):
            nums.append(int(file.readline()))
        return nums
    
def create_hashed(nums):
    length = len(nums)
    hashed = ['']*length
    for i in range(length):
        index = hash(nums[i]) % length
        while hashed[index] != '':
            index = (index + 1) % length
        print (nums[i], index)
        hashed[index] = nums[i]
    return hashed

print (create_hashed(create_list('listOfNums.txt')))