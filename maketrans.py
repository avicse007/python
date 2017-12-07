leet = str.maketrans('abegiloprstz', '463611092572')
print("Leet : ",leet)
my_string = 'Now some of the char are gona replace by the trans value';
print(my_string.translate(leet));