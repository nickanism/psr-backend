from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.forms.models import model_to_dict

from .forms import UserChangeForm, UserCreationForm
from .models import User, Count


class UserCountInline(admin.StackedInline):
    model = Count
    readonly_fields = ('id','date_time')
    extra = 0

    def user_counts_detail(self, x):
        visits = [{"date": a.date_time.date().strftime("%Y-%M-%d"), "time": a.date_time.time().strftime("%H:%M:%S") } for a in x.counts.all()]
        return visits

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'level', 'is_admin', 'is_active', 'user_counts')
    def user_counts(self, x):
        return x.counts.count()
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('level',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active',)}),
    )

    inlines = (UserCountInline,)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'level', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)