from django.contrib import admin
from .models import Project, Category, SubCategory, Equipment, TaggedEquipment, SpecifiedEquipment, PlantSystem, Size
# Register your models here.

def duplicate_query_sets(modeladmin, request, queryset):
    for p in queryset:
        p.pk = None
        p.save()
duplicate_query_sets.short_description = "Duplicate the items"

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_filter = ('name', 'code')
    fields = ('name', 'code')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_filter = ('name', 'code')
    fields = ('name', 'code')

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'category')
    list_filter = ('name', 'code', 'category')
    fields = ('name', 'code', 'category')
    
class SizeAdmin(admin.ModelAdmin):
    list_display = ('display_string', 'code_string')
    list_filter = ('display_string', 'code_string')
    fields = ('display_string', 'code_string')

class TaggedEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'project', 'equipment_category', 'equipment_subcategory')
    list_filter = ('project', 'specified_equipment__equipment__category', 'specified_equipment__equipment__subcategory',)
    fields = ('name', 'description', 'specified_equipment', 'project', 'system')
    actions = [duplicate_query_sets]
    
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'category', 'subcategory')
    list_filter = ('category', 'subcategory')
    fields = ('description', 'category', 'subcategory', 'vendor', 'model', 'material')
    ordering = ['category__code', 'subcode']
    # actions = [duplicate_query_sets]

class SpecifiedEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'size', 'equipment_category', 'equipment_subcategory')
    list_filter = ('equipment__category', 'equipment__subcategory', 'size')
    fields = ('equipment', 'size')

# class SpecifiedEquipment(admin.ModelAdmin):


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(TaggedEquipment, TaggedEquipmentAdmin)
admin.site.register(PlantSystem)
admin.site.register(Size, SizeAdmin)
admin.site.register(SpecifiedEquipment, SpecifiedEquipmentAdmin)