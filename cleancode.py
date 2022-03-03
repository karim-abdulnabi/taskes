"""n = 10
sum_all = 0

for i in range(1, n + 1):
    sum_all = sum_all + i

print(sum_all) """

#=====================clean code =========================

n = 10
sum_all = sum(range(1, n + 1))

print(sum_all)

#==============================================

"""names = ["Mike", "John", "Steve"]
names_iterator = iter(names)

for i in range(len(names)):
    print(next(names_iterator))"""
    
#====================clean code===========================
names = ["Mike", "John", "Steve"]

for name in names:
    print(name)    




opensourselanguage = ["javascript" , "python" , "java" , "php" , "c++" , "R" ,
                      "c#" , "swift" , "scala" , "Ruby"]

compiled_language = [ "C", "C++", "C#", "CLEO", "COBOL", ]

interpreted_language = ["JavaScript", "Perl", "Python", "BASIC"]
