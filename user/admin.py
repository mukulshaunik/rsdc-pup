from django.contrib import admin
from .models import ResearchGrant
from .models import TravelGrant
from .models import ConferenceGrant
from .models import Fellowship
from .models import Scholarship
from .models import Message
from .models import Student
from .models import Project
from .models import Notice
admin.site.register(ResearchGrant)
admin.site.register(TravelGrant)
admin.site.register(ConferenceGrant)
admin.site.register(Fellowship)
admin.site.register(Scholarship)
admin.site.register(Message)
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(Notice)
# Register your models here.
