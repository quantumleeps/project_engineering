from django.contrib import admin
from .models import Project, Category, SubCategory, Equipment, TaggedEquipment, PlantSystem, Size
# Register your models here.

class TaggedEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'project', 'equipment_category', 'equipment_subcategory')
    list_filter = ('project', 'equipment__category', 'equipment__subcategory',)
    fields = ('name', 'description', 'equipment', 'project', 'size', 'system')
    
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'category', 'subcategory')
    list_filter = ('category', 'subcategory')
    fields = ('description', 'category', 'subcategory')
    ordering = ['category__code', 'subcode']

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(TaggedEquipment, TaggedEquipmentAdmin)
admin.site.register(PlantSystem)
admin.site.register(Size)