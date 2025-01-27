# Musbat sonlarni filtrlaydigan funksiya
def is_positive(num):
    return num > 0

# Ro'yxat
numbers = [-10, -5, 0, 5, 10]

# filter() funksiyasidan foydalanib musbat sonlarni filtrlaymiz
positive_numbers = filter(is_positive, numbers) # type: ignore

# Natijani ro'yxatga aylantirib chop etamiz
print(list(positive_numbers))