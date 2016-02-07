from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import ResearchGrant
from .models import TravelGrant
from .models import ConferenceGrant
from .models import Fellowship
from .models import Scholarship
from .models import Message
from .models import Student
from .models import Project
from .models import StudentRel
from .models import Request
from .models import LeaderProject
from .models import StudentProject
from .models import LeaderResearch
from .models import Notice


def home(request):
	user = request.user
	VC = get_object_or_404(Message, Post='Vice Chancelor')
	HOD = get_object_or_404(Message, Post='Head Of Department')
	Dean = get_object_or_404(Message, Post='Dean')
	notices = Notice.objects.order_by('-date')
	return render(request, 'website/Home.html',{'VC':VC,'HOD':HOD,'Dean':Dean,'user':user,'notices':notices})
def about(request):
	user = request.user
	return render(request, 'website/About.html',{'user':user})
def member(request):
	if request.user.is_authenticated():
		studentrel = get_object_or_404(StudentRel, auth=request.user)
		me = studentrel.mine
		projects = LeaderProject.objects.filter(student=me)
		researches = LeaderResearch.objects.filter(student=me)
		requests = Request.objects.all()
		both = []
		mylist = []
		for project in projects:
			both.extend([project.project])
		for research in researches:
			both.extend([research.project])
		for b in both:
			for request1 in requests:
				if(b==request1.project):
					mylist.extend([request1])
		return render(request, 'website/Workspace.html',{'mylist':mylist,'student':me})
	else:
		return render(request, 'website/Member.html',{})








def research_list(request):
	user = request.user
	grants = ResearchGrant.objects.all()
	return render(request, 'website/ResearchGrants.html',{'grants':grants,'user':user})
def travel_list(request):
	user = request.user
	grants = TravelGrant.objects.all()
	return render(request, 'website/TravelGrants.html',{'grants':grants,'user':user})
def conference_list(request):
	user = request.user
	grants = ConferenceGrant.objects.all()
	return render(request, 'website/ConferenceGrants.html',{'grants':grants,'user':user})




def research_grant(request,title):
	user = request.user
	grants = ResearchGrant.objects.all()
	grant = get_object_or_404(ResearchGrant, title=title)
	return render(request, 'website/ResearchGrant.html',{'grant':grant, 'grants':grants,'user':user})
def travel_grant(request,title):
	user = request.user
	grants = TravelGrant.objects.all()
	grant = get_object_or_404(TravelGrant, title=title)
	return render(request, 'website/TravelGrant.html',{'grant':grant, 'grants':grants,'user':user})
def conference_grant(request,title):
	user = request.user
	grants = ConferenceGrant.objects.all()
	grant = get_object_or_404(ConferenceGrant, title=title)
	return render(request, 'website/ConferenceGrant.html',{'grant':grant, 'grants':grants,'user':user})







def fellowship_list(request):
	user = request.user
	grants = Fellowship.objects.all()
	return render(request, 'website/Fellowships.html',{'grants':grants,'user':user})
def scholarship_list(request):
	user = request.user
	grants = Scholarship.objects.all()
	return render(request, 'website/Scholarships.html',{'grants':grants,'user':user})



def fellowship(request,title):
	user = request.user
	grants = Fellowship.objects.all()
	grant = get_object_or_404(Fellowship, title=title)
	return render(request, 'website/Fellowship.html',{'grant':grant, 'grants':grants,'user':user})
def scholarship(request,title):
	user = request.user
	grants = Scholarship.objects.all()
	grant = get_object_or_404(Scholarship, title=title)
	return render(request, 'website/Scholarship.html',{'grant':grant, 'grants':grants,'user':user})


def project_circle(request):
	user = request.user
	LP = LeaderProject.objects.all()
	users = []
	leaders = []
	projects = []
	for lp in LP:
		projects.extend([lp.project])
		leaders.extend([lp.student])
		users.extend([get_object_or_404(StudentRel, mine=lp.student).auth])
	rows = zip(projects,users,leaders)
	length = len(projects)
	return render(request, 'website/ProjectCircle.html',{'user':user,'rows':rows,'projects':projects,'length':length})
def project_circle_guest(request):
	user = request.user
	return render(request, 'website/ProjectCircleGuest.html',{'user':user})
def intern_circle(request):
	user = request.user
	studentrel = get_object_or_404(StudentRel,auth=user)
	LP = LeaderProject.objects.all()
	users1 = []
	leaders1 = []
	projects1 = []
	for lp in LP:
		if(lp.student != studentrel.mine):
			projects1.extend([lp.project])
			leaders1.extend([lp.student])
			users1.extend([get_object_or_404(StudentRel, mine=lp.student).auth])
	row1 = zip(projects1,users1,leaders1)
	lengthproject = len(projects1)
	LP = LeaderResearch.objects.all()
	users2 = []
	leaders2 = []
	projects2 = []
	for lp in LP:
		if(lp.student != studentrel.mine):
			projects2.extend([lp.project])
			leaders2.extend([lp.student])
			users2.extend([get_object_or_404(StudentRel, mine=lp.student).auth])
	row2 = zip(projects2,users2,leaders2)
	lengthresearch = len(projects2)
	return render(request, 'website/InternCircle.html',{'user':user,'row1':row1,'row2':row2,'projects':projects1,'lengthproject':lengthproject,'researches':projects2,'lengthresearch':lengthresearch})
def intern_circle_guest(request):
	user = request.user
	return render(request, 'website/InternCircleGuest.html',{'user':user})
def research_circle(request):
	user = request.user
	LP = LeaderResearch.objects.all()
	users = []
	leaders = []
	projects = []
	for lp in LP:
		projects.extend([lp.project])
		leaders.extend([lp.student])
		users.extend([get_object_or_404(StudentRel, mine=lp.student).auth])
	rows = zip(projects,users,leaders)
	return render(request, 'website/ResearchCircle.html',{'user':user,'rows':rows})
def research_circle_guest(request):
	user = request.user
	return render(request, 'website/ResearchCircleGuest.html',{'user':user})
	
def register(request):
	username=password=''	
	if request.POST:
		name = request.POST.get('usernamesignup')
		password = request.POST.get('passwordsignup')
		email 	 = request.POST.get('emailsignup')
		count = User.objects.filter(username = name)
		if(len(count)>0):
			state = 'Username already exists'
			return render(request, 'website/Member.html',{'username':username,'state':state})
		else:
			user = User.objects.create_user(name,email,password)
			user.save()
			student = Student()
			student.save()
			studentrel = StudentRel(auth=user,mine=student)
			studentrel.save()
			state = ''
			return render(request, 'website/Member.html',{'username':username,'state':state})
		
def login_request(request):
	state = "Log In"
	username = password = ''
    
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			user = request.user
			VC = get_object_or_404(Message, Post='Vice Chancelor')
			HOD = get_object_or_404(Message, Post='Head Of Department')
			Dean = get_object_or_404(Message, Post='Dean')
			return render(request, 'website/Home.html',{'user':user, 'VC':VC, 'HOD':HOD, 'Dean':Dean})
		else:
			state = "Your account is not active, please contact the site admin."
	else:
		state = "Your username and/or password were incorrect."
	return render(request,'website/Member.html',{'state':state, 'username': username})


def logout_request(request):
	logout(request)
	VC = get_object_or_404(Message, Post='Vice Chancelor')
	HOD = get_object_or_404(Message, Post='Head Of Department')
	Dean = get_object_or_404(Message, Post='Dean')
	return render(request, 'website/Home.html',{'VC':VC,'HOD':HOD,'Dean':Dean})

def save_project(request):
	studentrel = get_object_or_404(StudentRel, auth=request.user)
	student = studentrel.mine
	if request.POST:
		start_date = request.POST.get('start_date')
		topic = request.POST.get('topic')
		details = request.POST.get('details')
		no_of_interns_required = request.POST.get('no_of_interns_required')
		role_qualification = request.POST.get('role_qualification')
		project_type = request.POST.get('type')
		test = Project.objects.filter(topic=topic)
		if(len(test)<1):
			project = Project(start_date=start_date, end_date='31/12/2020',topic=topic, details=details, no_of_interns_required=no_of_interns_required, role_qualification=role_qualification)
			project.save()
			if project_type == 'Research':
				projectrel = LeaderResearch(student=student,project=project)
				projectrel.save()
			else:
				projectrel = LeaderProject(student=student,project=project)
				projectrel.save()
			return render(request, 'website/Workspace.html',{'student':student})
		else:
			message = "Project/Research with same name already exists"
			return render(request, 'website/AddProject.html',{'message':message,'start_date':start_date,'topic':topic,'details':details,'no_of_interns_required':no_of_interns_required,'role_qualification':role_qualification,'project_type':project_type})

def save_student(request):
	if request.POST:
		studentrel = get_object_or_404(StudentRel, auth=request.user)
		student = studentrel.mine
		student.name = request.POST.get('name')
		student.age = request.POST.get('age')
		student.institute = request.POST.get('institute')
		student.address = request.POST.get('address')
		student.qualification = request.POST.get('qualification')
		student.works = request.POST.get('works')
		student.tag_line = request.POST.get('tag_line')
		student.achievement1 = request.POST.get('achievement1')
		student.achievement2 = request.POST.get('achievement2')
		student.achievement3 = request.POST.get('achievement3')
		student.save()
	return render(request, 'website/Workspace.html',{'student':student})


def add_project(request):
	message = "Add you project details"
	return render(request, 'website/AddProject.html',{'message':message})


def edit_profile(request):
	studentrel = get_object_or_404(StudentRel, auth=request.user)
	student = studentrel.mine
	return render(request, 'website/EditProfile.html',{'student':student})


def works(request):
	studentrel = get_object_or_404(StudentRel, auth=request.user)
	student = studentrel.mine
	projectrels = LeaderProject.objects.filter(student=student)
	projects=[]
	for projectrel in projectrels:
		projects.extend([projectrel.project])
	researchrels = LeaderResearch.objects.filter(student=student)
	researches=[]
	for researchrel in researchrels:
		researches.extend([researchrel.project])
	return render(request, 'website/Works.html',{'projects':projects,'researches':researches})


def work_detail_research(request,title):
	work = get_object_or_404(Project, pk=title)
	members = StudentProject.objects.filter(project=work)
	delimiter = ', '
	students = []
	for project in members:
		students.extend([project.student.name])
	s = delimiter.join(students)
	return render(request, 'website/WorkDetail.html',{'work':work,'s':s})


def work_detail_project(request,title):
	work = get_object_or_404(Project, pk=title)
	members = StudentProject.objects.filter(project=work)
	students = []
	for project in members:
		students.extend([project.student.name])
	s = ', '.join(students)
	return render(request, 'website/WorkDetail.html',{'work':work,'s':s})


def apply_intern(request,pk):
	studentrel = get_object_or_404(StudentRel,auth=request.user)
	count = Request.objects.filter(student = studentrel.mine)
	project = Project.objects.get(pk=pk)
	if(len(StudentProject.objects.filter(project=project)) >= project.no_of_interns_required):
		state = 'Maximmum intern limit for this project/research is reached'
	elif(len(count)>0):
		state = 'You have already applied for one Project/Research'
	else:	
		requests = Request(project=project,student=studentrel.mine)
		requests.save()
		state = 'Request Sent'
	user = request.user
	LP = LeaderProject.objects.all()
	users1 = []
	leaders1 = []
	projects1 = []
	for lp in LP:
		if(lp.student != studentrel.mine):
			projects1.extend([lp.project])
			leaders1.extend([lp.student])
			users1.extend([get_object_or_404(StudentRel, mine=lp.student).auth])
	row1 = zip(projects1,users1,leaders1)
	LP = LeaderResearch.objects.all()
	users2 = []
	leaders2 = []
	projects2 = []
	for lp in LP:
		if(lp.student != studentrel.mine):
			projects2.extend([lp.project])
			leaders2.extend([lp.student])
			users2.extend([get_object_or_404(StudentRel, mine=lp.student).auth])
	row2 = zip(projects2,users2,leaders2)
	zero = 0
	return render(request, 'website/InternCircle.html',{'zero':zero,'count':len(count),'state':state,'project':project,'user':user,'row1':row1,'row2':row2})
	

def accept(request,pk):
	myrequest = get_object_or_404(Request,pk=pk)
	studentrel = get_object_or_404(StudentRel,auth=request.user)
	studentproject = StudentProject(student=studentrel.mine,project=myrequest.project)
	studentproject.save()
	myrequest.delete()
	return member(request)



def delete(request,pk):
	myrequest = Request.objects.filter(pk=pk)
	myrequest.delete()
	return member(request)
	'''
	request1 = []
	projects = []
	students = []
	for a in requests:
		leaderproject = LeaderProject.objects.filter(project=a.project).student
		if leaderproject==user :
			request1.extend([a])
	for a in requests:
		leaderproject = LeaderResearch.objects.filter(project=a.project).student
		if leaderproject==user :
			request1.extend([a])
	for a in request1:
		projects.extend([a.project])
		students.extend([a.student])
	rows = zip(projects,students,request1)
	return render(request, 'website/Workspace.html',{'rows':rows})'''


def edit_project(request):
	if request.POST:
		pk = request.POST.get('pk')
		project = get_object_or_404(Project,id=pk)
		project.start_date = request.POST.get('start_date')
		project.topic = request.POST.get('topic')
		project.details = request.POST.get('details')
		project.end_date = request.POST.get('end_date')
		project.save()
		studentrel = get_object_or_404(StudentRel, auth=request.user)
		student = studentrel.mine
		
		return render(request, 'website/Workspace.html',{'student':student})
# Create your views here.
