from django.contrib import admin
from .models import Award,Education,Experience,Work,Contact,Service,Counter

# Register your models here.
admin.site.register(Award)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Work)
admin.site.register(Contact)
admin.site.register(Service)
admin.site.register(Counter)