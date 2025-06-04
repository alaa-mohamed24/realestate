from django.contrib import admin
from django import forms
from .models import Property, PropertyImage

class PropertyAdminForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

class PropertyAdmin(admin.ModelAdmin):
    form = PropertyAdminForm
    list_display = ('title', 'price', 'category', 'is_available')
    inlines = [PropertyImageInline]

    class Media:
        js = ('properties/property_admin.js',)

admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyImage)
