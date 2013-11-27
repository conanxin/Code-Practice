i=1
while (i<=50):
	while 1:
		name=raw_input("Enter the name")
		if len(name)==0:
			continue
		else:
			break

	while 1:
		reg_no=raw_input("Enter the registration number")
		if len(reg_no)==0:
			continue
		else:
			break

	j=1
	tot_score=0
	while j<=4:
		print 'Enter score in subject', j
		score=raw_input()
		if len(score)==0 or int(score)>100:
			continue
		else:
			j=j+1
			tot_score=tot_score+int(score)

	percent=tot_score/4
	if percent>=80:
		grade='A'
	elif percent>=60:
		grade='B'
	elif percent>=40:
		grade='C'
	else:
		grade='Fail'
	for clear in range(35):	
		print
	print '-'*60
	print "Name          :", name
	print
	print "Registration no.  :", reg_no
	print 
	print "Grade          :", grade
	print '-'*60
	for y in range(10):
		print
	choice=raw_input("Do you want to enter details for\
		another student? ")
	choices=['y','Y','yes','Yes','YES']
	if choice in choices:
		i=i+1
		for clear in range(40):
			print
	else:
		break