from flask import Flask, request, render_template
import csv
import matplotlib
#from jinja2 import Template
import matplotlib.pyplot as plt
matplotlib.use('AGG')

list = []
with open('data.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile)
	for row in spamreader:
		list.append(row)

#print(list)
d = {}
l = []
for i in range(1, len(list)):
	d[list[0][0].strip()] = list[i][0].strip()
	d[list[0][1].strip()] = list[i][1].strip()
	d[list[0][2].strip()] = int(list[i][2].strip())
	#print(d)
	l.append(d)
	d = {}

#l_st_id aggregating list of student ids
l_st_id = []
for d in l:
	l_st_id.append(d['Student id'])
#print(l_st_id, 'l_st_id')

#l_cour_id aggregating list of course ids
l_cour_id = []
for d in l:
	l_cour_id.append(d['Course id'])
#print(l_cour_id, 'l_cour_id')

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def funct():
    if request.method =='GET':
        return render_template('index.html')
    if request.method =='POST':
        ID = request.form.get('ID')
        #print(ID)
        ID = request.form.get('ID')
        #print(ID)
        id_value = request.form.get('id_value')
        #print(id_value)
        #temp = Template('/template/base.html')
        #output = temp.render(student_details=l)


        if ID == 'student_id' and id_value in l_st_id:
            return render_template('base.html',stu_details=l, y=id_value)
        
        elif ID == 'course_id' and id_value in l_cour_id:

            marksl_per_stu = []
            for d in l:
                if d['Course id'] == id_value:
                    marksl_per_stu.append(d['Marks'])

            #Calculating avg marks of a perticular student
            sum = 0
            for marks in marksl_per_stu:
                sum += marks
            avg = sum / len(marksl_per_stu)

            #Calculating max marks of a perticular student
            max = 0
            for marks in marksl_per_stu:
                if marks > max:
                    max = marks
            plt.clf()
            plt.hist(marksl_per_stu)
            plt.xlabel("Marks")
            plt.ylabel("Frequency")
            plt.savefig("static/graph.png")
            #plt.close()

            return render_template('base3.html',avg=avg, max=max, image='static/graph.png')
        
        else:
              return render_template('base2.html')
    
app.run(debug = True)