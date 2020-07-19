from django.contrib import admin
from .models import Admin
from .models import Activity
from .models import Participate
from .models import Discuss
from .models import Users

# Register your models here.
admin.site.register(Admin)
admin.site.register(Activity)
admin.site.register(Participate)
admin.site.register(Discuss)
admin.site.register(Users)
