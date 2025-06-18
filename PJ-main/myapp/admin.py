from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(disease)
admin.site.register(medicine)
admin.site.register(health_parameters)
admin.site.register(sub_health_parameters)
admin.site.register(ask_to_expert)
admin.site.register(order)
admin.site.register(user)
admin.site.register(contact_us)
admin.site.register(plan)
admin.site.register(user_membership)
admin.site.register(advertisement)
admin.site.register(admin_login)

