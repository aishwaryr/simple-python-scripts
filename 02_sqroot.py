x = int(input("Enter the num: "))
if x < 0:
	x = abs(x)
	negFlag = 1
else:
	negFlag = 0

ans = 0
#flag = 0
while ans*ans < x:
	ans += 1
	#flag += 1
	#print (flag)
if ans*ans != x:
	print(str(x)+" is not a perfect square.")
else:
	if negFlag == 1:
		print(str(ans)+ "i is the square root of " + str(x*-1) + ".")
		
	elif negFlag == 0:
			print(str(ans)+ " and "+ str(-1*ans) + " are the square roots of " + str(x) + ".")

	

