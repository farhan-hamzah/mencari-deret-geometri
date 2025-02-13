
# deret geometri
start = int(input("Start :"))
end = int(input("End :"))
r = int(input("Rasio :"))
a = start
hasil = [a]
count = 1
while count < end:
    a *= r
    hasil.append(a)
    count += 1
print(hasil)