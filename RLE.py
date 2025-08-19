print('В данной программе при сжатии строки управляющий байт повторяющихся символов начинается с 0, а неповторяющихся - с 1  ')
def rle_encode(data):
  """Сжимает данные с помощью RLE."""
  encoded_data = []
  count = 1
  prev_byte = data[0]
  for i in range(1, len(data)):
    if data[i] == prev_byte:
      count += 1
    else:
      encoded_data.extend([count, prev_byte])
      prev_byte = data[i]
      count = 1
  encoded_data.extend([count, prev_byte])
  return encoded_data

def encod_con(a):
    """Систематизирует и выделяет управляющий байт """
    spis_index = []
    spis_con = []
    counter = 0
    for i in range(1, len(a), 2):
        if a[i - 1] == 1:
            counter += 1
            spis_index.append(i - 1)
        else:
            if counter != 0:
                spis_con.append(str(counter)+"!")
                counter = 0
            for y in spis_index:
                spis_con.append(a[y + 1])
            spis_con.extend([a[i - 1], a[i]])
            spis_index = []
        if i == len(a) - 1 and counter!=0:
            spis_con.append(str(counter)+'!')
            for y in spis_index:
                spis_con.append(a[y + 1])
    return spis_con


def encode_to_binary(encoded_data):
  """Преобразует список сжатых данных в двоичную строку."""
  binary_data = []
  for item in encoded_data:
      if  ((type(item)==str) and (item[-1] =="!") and (item[0]!="!")):
          item = int(item[:-1])
          item = bin(item)[2:]
          item = '1'+"0"*(7-len(item))+item
          binary_data.append(item)
      else:
        if str(item).isdigit():
              binary_data.append(bin(item)[2:])
        else:
              binary_data.append(bin(int.from_bytes(str(item).encode('windows-1251')))[2:])
        for i in range(len(binary_data)):
            binary_data[i] = '0' * (8 - len(binary_data[i])) + binary_data[i]
  return binary_data


# Тело программы
data  =[]
spis = input('Введите строку, которую хотите сжать: ')
for i in spis:
    if i.isdigit():
        data.append(int(i))
    else:
        data.append(i)
#print(data)

#Сжатие данных
encoded_data = rle_encode(data)
encoded_dat = encod_con(encoded_data)

print(f"Сжатые данные: {encoded_dat}")

#Вид в двоичной записи
binary_data = encode_to_binary(encoded_dat)
print(f"Двоичная запись сжатых данных: {binary_data}")

#Нахождение КС
rez = 0
for i in range(len(binary_data)):
    rez ^=int(binary_data[i],2)
print('Контрольная сумма:',bin(rez),hex(rez))