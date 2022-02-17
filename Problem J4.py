# The first line will contain an integer X with X ≥ 0. The next X lines will each consist of
# two different names, separated by a single space. These two students must be in the same
# group.
# The next line will contain an integer Y with Y ≥ 0. The next Y lines will each consist of
# two different names, separated by a single space. These two students must not be in the
# same group.
# Among these X + Y lines representing constraints, each possible pair of students appears at
# most once.
# The next line will contain an integer G with G ≥ 1. The last G lines will each consist of
# three different names, separated by single spaces. These three students have been placed in
# the same group.
# Each name will consist of between 1 and 10 uppercase letters. No two students will have
# the same name and each name appearing in a constraint will appear in exactly one of the G
# groups.

sameGroupNum = int(input())

sameGroupList1 = []
sameGroupList2 = []
diffGroupList1 = []
diffGroupList2 = []



violations = 0

for x in range(0,sameGroupNum):
    name1,name2 = [i for i in input().split()]
    sameGroupList1.append(name1)
    sameGroupList2.append(name2)

diffGroupNum = int(input())

for x in range(0,diffGroupNum):
    name1,name2 = [i for i in input().split()]
    diffGroupList1.append(name1)
    diffGroupList2.append(name2)

groupNum = int(input())

for x in range(0,groupNum):
    group = []
    name1,name2,name3 = [i for i in input().split()]
    group.append(name1)
    group.append(name2)
    group.append(name3)

    for element in group:
        
        for x in range(0,sameGroupNum):
            inList = False
            if element == sameGroupList1[x]:
                inList = True
                for i in group:
                    if i == sameGroupList2[x]:
                        sameGroupList1[x] = ""
                        sameGroupList2[x] = ""

            if element == sameGroupList2[x]:
                inList = True
                for i in group:
                    if i == sameGroupList1[x]:
                        sameGroupList1[x] = ""
                        sameGroupList2[x] = ""
            if inList == True:
                if sameGroupList2[x] != "":
                    violations += 1
                    sameGroupList1[x] = ""
                    sameGroupList2[x] = ""


        for x in range(0,diffGroupNum):
            if element == diffGroupList1[x]:
                for i in group:
                    if i == diffGroupList2[x]:
                        violations += 1
                        diffGroupList1[x] = ""
                        diffGroupList2[x] = ""
                    

            if element == diffGroupList2[x]:
                for i in group:
                    if i == diffGroupList1[x]:
                        violations += 1
                        diffGroupList1[x] = ""
                        diffGroupList2[x] = ""

print(violations)

