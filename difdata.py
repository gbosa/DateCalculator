
print("""==========================================
  Calculate # of days between two dates
==========================================
""")

data1 = input("Date: ") #data1[-4:]=ano data1[2:4]=mes dia=data1[:2]
data2 = input("Other date: ")
j=0; mes = [31,28,31,30,31,30,31,31,30,31,30,31]

#organiza data
def gt(a,b):
	if int(a[-4:])<int(b[-4:]):
		return [a,b]
	elif int(a[-4:])>int(b[-4:]):
		return [b,a]
	else:
		if int(a[2:4])<int(b[2:4]):
			return [a,b]
		elif int(a[2:4])>int(b[2:4]):
			return [b,a]
		else:
			if int(a[1:2])<int(b[1:2]):
				return [a,b]
			elif int(a[1:2])>int(b[1:2]):
				return [b,a]
			else:
				return 0

#func ano bissexto
def bi6o(year):
	a=True
	if year % 4:
		a = False
	return a

def MonthToDay(day,month):
	n=0
	for i in range(0,int(month)-1):
		n += mes[i]
	n = n + int(day)
	return n

a=gt(data2,data1)
lower_date=a[0]; bigger_date=a[1] # type: ignore

if int(lower_date[2:4])<=2 and int(bigger_date[2:4])<2:
	for i in range(int(lower_date[-4:]),int(bigger_date[-4:])):
		if bi6o(i):
			j+=1
elif int(lower_date[2:4])>2 and int(bigger_date[2:4])<2:
	for i in range(int(lower_date[-4:])+1,int(bigger_date[-4:])):
		if bi6o(i):
			j+=1
elif int(lower_date[2:4])<=2 and int(bigger_date[2:4])>2:
	for i in range(int(lower_date[-4:]),int(bigger_date[-4:])+1):
		if bi6o(i):
			j+=1
elif int(lower_date[2:4])>2 and int(bigger_date[2:4])>2:
	for i in range(int(lower_date[-4:])+1,int(bigger_date[-4:])+1):
		if bi6o(i):
			j+=1

qtDia1 = MonthToDay(lower_date[:2],lower_date[2:4])
qtDia2 = MonthToDay(bigger_date[:2],bigger_date[2:4])

tot = (qtDia2 - qtDia1) + j + 365*(int(bigger_date[-4:])-int(lower_date[-4:]))

print(f'''
The difference between
{data1[:2]}/{data1[2:4]}/{data1[-4:]} and {data2[:2]}/{data2[2:4]}/{data2[-4:]} is:
    {tot} days.
    '''
    )