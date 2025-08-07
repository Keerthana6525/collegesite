from django.contrib import admin
from .models import NewsEvent, Announcement, CarouselImage
from django import forms

# Register other models normally
admin.site.register(Announcement)
admin.site.register(CarouselImage)

# Custom admin form for date formatting (optional, if you want to format input)
class NewsEventForm(forms.ModelForm):
    class Meta:
        model = NewsEvent
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
        }

# Register NewsEvent with custom display
@admin.register(NewsEvent)
class NewsEventAdmin(admin.ModelAdmin):
    form = NewsEventForm  # Use the custom form
    list_display = ('formatted_date',)  # Show formatted date in list
    fields = ('description', 'date')    # Fields visible in form

    # Method to format the date
    def formatted_date(self, obj):
        return obj.date.strftime('%a, %d %b %Y')  # E.g., 'Wed, 02 Aug 2025'
    formatted_date.short_description = 'Date'
