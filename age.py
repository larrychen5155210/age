# else if 另外如果
# 年齡判別
age = input('請輸入你的年齡: ')
age = int(age)
if age < 13:
	print('國小')
elif age >= 13 and age < 18:
	print('國高中')
elif age >= 18 and age < 22:
	print('大學')
else:
	print('出社會')

