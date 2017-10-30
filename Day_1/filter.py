#取偶数
l = [1,2,3,4,5]
print(list(filter(lambda x:x%2==0,l)))

#删除空格
string = ['A','','d','','s']
print(list(filter(lambda x:x and x.strip(),string)))



#回数筛选
def is_palindrome(n):
    for i in str(n):
        if str(n)[:] == str(n)[::-1]: return True
        else: return False
print(list(filter(is_palindrome,range(1,1000))))