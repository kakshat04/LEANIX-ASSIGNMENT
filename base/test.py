# from Project.base.Read_from_json import ReadJson
#
# json_read = ReadJson()
# ages = json_read.get_access_key_age()
# # ages = [67, 13, 42]
#
# age_range = [1, 13, 25, 37, 49, 61]
#
# num = []
# for age in ages:
#     i = 0
#     j = 0
#     print(age, num, i, j)
#     while j < len(age_range) - 1:
#         j += 1
#         if age_range[i] <= age < age_range[j]:
#             num.append(age_range[i])
#             break
#         i += 1
#     if len(num) == 0:
#         num.append(age_range[-1])
#     print(num)
#
# for i in num:
#     print(age_range.index(i))

x = ['background-color: rgb(0, 65, 106);', 'background-color: rgb(143, 184, 210);']
z = ['background-color: rgb(0, 65, 106); color: rgb(255, 255, 255);',
     'background-color: rgb(143, 184, 210); color: rgb(255, 255, 255);']
for i in range(len(z)):
    if x[i] in z[i]:
        print("Yes")
    else:
        print("No")



