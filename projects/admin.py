from django.contrib import admin
from .models import Project, Category, SubCategory, Equipment, TaggedEquipment, PlantSystem, Size
# Register your models here.

class TaggedProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_filter = ('name', 'code')
    fields = ('name', 'code')

class TaggedCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_filter = ('name', 'code')
    fields = ('name', 'code')

class TaggedSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'category')
    list_filter = ('name', 'number', 'category')
    fields = ('name', 'number', 'category')
    
class TaggedSizeAdmin(admin.ModelAdmin):
    list_display = ('display_string', 'code_string')
    list_filter = ('display_string', 'code_string')
    fields = ('display_string', 'code_string')

class TaggedEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'project', 'equipment_category', 'equipment_subcategory')
    list_filter = ('project', 'equipment__category', 'equipment__subcategory',)
    fields = ('name', 'description', 'equipment', 'project', 'size', 'system')
    
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'category', 'subcategory')
    list_filter = ('category', 'subcategory')
    fields = ('description', 'category', 'subcategory')
    ordering = ['category__code', 'subcode']

admin.site.register(Project, TaggedProjectAdmin)
admin.site.register(Category, TaggedCategoryAdmin)
admin.site.register(SubCategory, TaggedSubCategoryAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(TaggedEquipment, TaggedEquipmentAdmin)
admin.site.register(PlantSystem)
admin.site.register(Size, TaggedSizeAdmin)