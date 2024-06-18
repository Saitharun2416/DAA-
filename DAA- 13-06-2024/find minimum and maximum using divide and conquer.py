def m(a):
    def dandc(a,low,high):
        if low == high:
            return a[low], a[low]
        if high == low +1:
            if a[low] < a[high]:
                return a[low], a[high]
            else:
                return a[high], a[low]

        mid=(low+high) // 2

        left_min, left_max = dandc(a,low,mid)
        right_min, right_max = dandc(a, mid+1, high)

        overall_min = min(left_min, right_min)
        overall_max = max(left_max, right_max)

        return overall_min, overal_max
    
    return dandc(a, 0, len(a)-1)

a=[3,1,4,1,5,9,7,8,5,5]
min_value, max_value = m(a)
print(f"the minimum value is : {min_value}")
print(f"the maximum value is : {max_value}")
