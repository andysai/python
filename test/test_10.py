start_floor_rooms = {301:[1,80], 302:[1,80], 303:[2,90]}
start_floor = '3'
end_floor = '4'
floor_last_number = ['01','02','03']
floor_rooms = {}
for i in range(len(start_floor_rooms)):
    a = start_floor_rooms[int(start_floor + floor_last_number[i])]
    b = end_floor + floor_last_number[i]
    print(a)
    floor_rooms[b] = a
print(floor_rooms)

for i in range(3+1,7+1):
    print(i)