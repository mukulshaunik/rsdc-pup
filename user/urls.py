from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$',					views.home,		name='Home'),
    url(r'^About/$',				views.about,		name='About'),
    url(r'^Member/$',				views.member,		name='Member'),
    





    url(r'^ResearchGrants/$',			views.research_list,	name='ResearchList'),
    url(r'^TravelGrants/$',			views.travel_list,	name='TravelList'),
    url(r'^ConferenceGrants/$',			views.conference_list,	name='ConferenceList'),
    


    url(r'^ConferenceGrant/(?P<title>.*)/$',	views.conference_grant,	name='ConferenceGrant'), 
    url(r'^ResearchGrant/(?P<title>.*)$',	views.research_grant,	name='ResearchGrant'), 
    url(r'^TravelGrant/(?P<title>.*)/$',	views.travel_grant,	name='TravelGrant'), 
    



    url(r'^Fellowships/$',			views.fellowship_list,	name='FellowshipList'),
    url(r'^Fellowship/(?P<title>.*)/$',		views.fellowship,	name='Fellowship'),
    url(r'^Scholarships/$',			views.scholarship_list,	name='ScholarshipList'),
    url(r'^Scholarship/(?P<title>.*)/$',	views.scholarship,	name='Scholarship'),
    



    url(r'^ProjectCircle/$',			views.project_circle,		name='ProjectCircle'),
    url(r'^ResearchCircle/$',			views.research_circle,		name='ResearchCircle'),
    url(r'^InternCircle/$',			views.intern_circle,		name='InternCircle'),  
    url(r'^ProjectCircleGuest/$',		views.project_circle_guest,	name='ProjectCircleGuest'),
    url(r'^ResearchCircleGuest/$',		views.research_circle_guest,	name='ResearchCircleGuest'),
    url(r'^InternCircleGuest/$',		views.intern_circle_guest,	name='InternCircleGuest'),
    

    url(r'^login/$',				views.login_request,	name='Login'),
    url(r'^register/$',				views.register,		name='Register'),
    url(r'^Logout/$',				views.logout_request,	name='Logout'),
    url(r'^SaveProject/$',			views.save_project,	name='SaveProject'),
    url(r'^SaveStudent/$',			views.save_student,	name='SaveStudent'),
    url(r'^Apply/(?P<pk>[0-9]+)/$',		views.apply_intern,	name='Apply'),
    url(r'^Accept/(?P<pk>[0-9]+)/$',				views.accept,		name='Accept'),
    url(r'^Delete/(?P<pk>[0-9]+)/$',				views.delete,		name='Delete'),
    url(r'^EditProject/$',			views.edit_project,	name='EditProject'),
    



    url(r'^AddProject/$',				views.add_project,		name='AddProject'),
    url(r'^EditProfile/$',				views.edit_profile,		name='EditProfile'),
    url(r'^Works/$',					views.works,			name='Works'),
    url(r'^WorkDetailProject/(?P<title>.*)/$',		views.work_detail_project,	name='WorkDetailProject'),
    url(r'^WorkDetailResearch/(?P<title>.*)/$',		views.work_detail_research,	name='WorkDetailResearch'),

]
