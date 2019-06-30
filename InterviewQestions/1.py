#题目描述：
# 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
# 也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
# 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是重复的数字2或者3。

#思路解析:
#注意题目条件，所有数字在0到n-1范围内，如果经过排序，那么数字i应该在下标i的位置
#从头扫描这个数组，当扫描到第i个元素时，判断其值(假设为m)是否等于i,如果相等，
#则扫描下一个，如果不等，则判断m是否与数组第m个元素相等，相等则说明有重复元素，
#如果不等，则将第i个元素与第m个元素位置互换，把m放到正确的位置，重复此过程，直
#到找到重复数字或者遍历结束，以{2,3,1,0,2,5,3}为例，过程如下
#第一次交换后{1,3,2,0,2,5,3}
#第二次交换后{3,1,2,0,2,5,3}
#第三次交换后{0,1,2,3,2,5,3}
#下标0~3，数字与下标相等，遍历值下标4，nums[4]==nums[nums[4]],
#说明找到重复数字，返回true，这种方法也是一个数组排序的好办法

class Solotion():
    def duplicate(self,nums):
        i = 0
        while(i < len(nums)):
            if (nums[i] != i):
                temp = nums[i]
                if (temp != nums[temp]):
                    nums[i] = nums[temp]
                    nums[temp] = temp
                else:
                    return True
            else:
                i += 1
        return False

res = Solotion()
nums=[5,4,3,2,1,0,5]
ans = res.duplicate(nums)
print(ans)