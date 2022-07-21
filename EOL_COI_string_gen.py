input_string = input("Raw author list: ")
interim_string_1 = input_string.replace(" (proxy) (contact)","")
interim_string = interim_string_1.replace(";"," OR")
interim_string = "AND (" + interim_string + ")"
output_string = interim_string
chinese = "-Liu -Zhao -Li -Xia -Chen -Geng -Lu -Wang -Su -Zheng -Guo -Zhang"

authors = interim_string_1.split(";")
surname_list = []

for name in authors:
    surname = "x"
    surname = name.split(",")
    surname_list.append(surname[0])
    
    
surname = ""
for name in surname_list:
    name = name.replace(" ", "")
    surname = surname + "-" + name + " "
    
print("\n\nPubmed string: \n" + output_string)
print("\n\nSurnames: \n" + surname)
print("\n\nChinese: -Li -Xia -Chen -Geng -Lu -Wang -Su -Zheng -Guo -Zhang -Liu -Zhao")