from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models import Max

# Create your models here.
class Project(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    code = models.PositiveIntegerField(validators=[MaxValueValidator(99)], unique=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    class Meta:
        verbose_name_plural = "sub categories"
    name = models.CharField(max_length=25)
    number = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    class Meta:
        verbose_name_plural = "equipment"
    # code = models.CharField(max_length=2)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,)
    subcode = models.PositiveIntegerField(validators=[MaxValueValidator(999)])
    code = models.CharField(max_length=7)

    def __str__(self):
        return  self.code + ' - ' + self.description

    def find_next_subcode(self):
        subcategory_numbers = sorted([subcategory.number for subcategory in SubCategory.objects.filter(category=self.category)])
        if subcategory_numbers.index(self.subcategory.number) < (len(subcategory_numbers)-1):
            next_subcategory_number = subcategory_numbers[(subcategory_numbers.index(self.subcategory.number)+1)]
        else:
            next_subcategory_number = 99999
        return self.subcategory.number + len(Equipment.objects.filter(category=self.category, subcode__range=(self.subcategory.number, next_subcategory_number-1)))
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.subcode = self.find_next_subcode()
        self.code = str(self.category.code).zfill(2) + '.' + str(self.subcode).zfill(3)
        super().save(*args, **kwargs)

class PlantSystem(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Size(models.Model):
    display_string = models.CharField(max_length=50)
    code_string = models.CharField(max_length=10)

    def __str__(self):
        return self.display_string

class TaggedEquipment(models.Model):
    class Meta:
        verbose_name_plural = "tagged equipment"

    name = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    subcode = models.PositiveIntegerField(validators=[MaxValueValidator(999)])
    code = models.CharField(max_length=40)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE,)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,)
    size = models.ForeignKey(Size, on_delete=models.CASCADE,)
    system = models.ForeignKey(PlantSystem, on_delete=models.CASCADE,)


    def save(self, *args, **kwargs):
        if not self.id:
            if len(TaggedEquipment.objects.filter(size=self.size, project=self.project, equipment=self.equipment)) == 0:
                self.subcode = 0
            else:
                self.subcode = TaggedEquipment.objects.filter(size=self.size, project=self.project, equipment=self.equipment).aggregate(Max('subcode'))['subcode__max'] + 1
        else:
            if self.code[:-3] == self.project.code + '.' + str(self.equipment.category.code).zfill(2) + '.' + str(self.equipment.subcode).zfill(3) + '.' + str(self.size.code_string).zfill(4) + '.':
                pass
            else:
                if len(TaggedEquipment.objects.filter(size=self.size, project=self.project, equipment=self.equipment)) == 0:
                    self.subcode = 0
                else:
                    self.subcode = TaggedEquipment.objects.filter(size=self.size, project=self.project, equipment=self.equipment).aggregate(Max('subcode'))['subcode__max'] + 1
        self.code = self.project.code + '.' + str(self.equipment.category.code).zfill(2) + '.' + str(self.equipment.subcode).zfill(3) + '.' + str(self.size.code_string).zfill(4) + '.' + str(self.subcode).zfill(3)
        super().save(*args, **kwargs)


    def equipment_category(self):
        return self.equipment.category
    
    def equipment_subcategory(self):
        return self.equipment.subcategory

    def __str__(self):
        return self.name + ' - ' + self.code

