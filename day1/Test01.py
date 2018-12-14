oldGrade=float(input("请输入去年的成绩:"))
thisGrade=float(input("请输入今年的成绩:"))

average=(oldGrade+thisGrade)/2

info="""
-----------------去年成绩:{_oldGrade}------------
-----------------今年成绩:{_thisGrade}-------
-----------------平均成绩:{_average}----
""".format(_oldGrade=oldGrade,_thisGrade=thisGrade,_average=average)

print(info)