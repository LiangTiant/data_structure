
#实现利用二分法找到对应值最为接近的较小值的位置
def find_up(num,key):
    low=0
    high=len(num)-1
    if num[0]>key or num[-1]<key: return -1
    while low<high:
        mid=(low+high)//2+(low+high)%2#向上运动
        if num[mid]==key: return mid
        elif num[mid]<key: low=mid#low记录比key大的值
        else:high=mid-1#high记录比key大的值，low向下运动

    return (low+high)//2