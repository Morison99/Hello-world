summing = input("Enter Your Inputs : ")

# روش خودم

summing = summing.split()
leng = len(summing)
summing2 = list()

for a in range(0, leng):

    try:
        summing2.append(float(summing[a]))
    except ValueError:
        summing2.append(0)

b = 0

if summing2.count(0) != leng:
    for a in summing2:
        b += a
    print(b)
else:
    print("there is no number")


print(30*("***"))

# ___________________________________________________________________
# ___________________________________________________________________

# روش دوم که همان روش حل شده در ویدیو است

inputs = summing


def is_numeric(x):
    try:
        float(x)
        return True
    except:
        return False


# برگرداندن داده هایی که قابل تبدیل به عدد هستند
numeric_string = list(filter(is_numeric, inputs))

if numeric_string:
    numbers = map(float, numeric_string)
    print("sum of numbers", sum(numbers))
else:  # تنها در صورتی اجرا میشود که لیست نومریک تهی باشد و هیچ داده عددی را تشخیص نداده باشد
    print("there is no number")
