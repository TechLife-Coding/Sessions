"""برنامه‌ای بنویسید که 10 بار ارتفاع پرش ورزشکار را دریافت کند.

اگر رکورد جدید بود، پیام «بیشترین پرش ثبت شد» نمایش داده شود.
اگر قبلاً ثبت شده بود، پیام مناسب چاپ شود."""
l1=[]
gym_guy=l1.append(float(input('enter Km / Jump: ')))

gym_guy=l1[0]

for newrec in gym_guy:
    if gym_guy > newrec:
        gym_guy=newrec

print(f'new rec is added / you jump {gym_guy} higher now')
