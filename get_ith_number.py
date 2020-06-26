#获得数字第i位的函数,从低位到高位
def get_i(num,i)
	return num//(10**(i-1))%10
