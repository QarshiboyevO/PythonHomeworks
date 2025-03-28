import csv

with open("grades.csv",'w') as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Subject","Grade"])
    writer.writerow(['Alice',"Math",85])
    writer.writerow(["Bob","Science", 78])
    writer.writerow(["Carol","Math",92])
    writer.writerow(["Dave","History", 74])


grade=[]
with open("grades.csv",'r') as f:
    reader = csv.reader(f)
    for row in reader:
        student={"name":row[0],"subject":row[1],"grade":row[2]}
        grade.append(student)


mathtotal=0
sciencetotal=0
historicaltotal=0
mathscounter=0
sciencecounter=0
historicalcounter=0
for student in grade:
    if student["subject"]=="Math":
        mathtotal+=int(student["grade"])
        mathscounter+=1
    elif student["subject"]=="Science":
        sciencetotal+=int(student["grade"])
        sciencecounter+=1
    elif student["subject"]=="History":
        historicaltotal+=int(student["grade"])
        historicalcounter+=1
subject=[["Subject",'Grade'],["Maths",mathtotal/mathscounter],["Science",sciencetotal/sciencecounter],["History",historicaltotal/historicalcounter]]
print(mathtotal,sciencetotal,historicaltotal)
with open("average_grades.csv",'w') as f:
    writer = csv.writer(f)
    for row in subject:
        writer.writerow(row)

with open("average_grades.csv",'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)