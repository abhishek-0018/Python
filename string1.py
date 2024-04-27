import string
s="Hello world"
print(s[0])
print(s[5])
print(s[-2])  # print characters from last
print(s[0:5])
print(s[:3])
print(s[4:])
print(s[:])
print(s[0:10:2])
print(s.upper())
print(s)
a = "topeka,kansas city,wichita,olathe"
city=a.split(",")  #   a.split() will split after space
for c in city:
    print(c)
f = "Buffalo;Rochester;Yonkers;Syracuse;Albany;Schenectady"

# Separate on semicolon.

# ... Split from the right, only split three.

cities = f.rsplit(";", 3)

# Loop and print.

for ci in cities:
    print(ci)
list = ["a", "b", "c"]

# Join with empty string literal.

result = "".join(list)

# Join with comma.

result2 = ",".join(list)

# Display results.

print(result)

print(result2)