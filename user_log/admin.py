from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(College)
admin.site.register(MainEvent)
# admin.site.register(SubEvents)
admin.site.register(Games)

class SubEventsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Save the model
        super().save_model(request, obj, form, change)

        # Check if the participants field has been modified
        if form.cleaned_data.get('participants'):
            # Iterate through the participants and update their participated_event
            for user in form.cleaned_data['participants']:
                if str(obj.id) not in user.participated_event:
                    user.participated_event += str(obj.id) + ","
                    user.save()

class RanksAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Save the model
        super().save_model(request, obj, form, change)
        # user = form.cleaned_data.get('user')
        if form.cleaned_data.get('rank'):
            all_ranks = Ranks.objects.filter(user=obj.user,rank=obj.rank)
            if all_ranks:
                obj.save()
            else:
                obj.delete()
            

admin.site.register(SubEvents, SubEventsAdmin)
admin.site.register(Ranks,RanksAdmin)