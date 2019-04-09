from django.test import TestCase
from projects.models import Project, Category, \
    SubCategory, Equipment, PlantSystem, Size, TaggedEquipment, SpecifiedEquipment

class EquipmentTestCase(TestCase):
    def setUp(self):
        Category.objects.create(code=13, name='Valves')
        Category.objects.create(code=21, name='Pumps')
        valves = Category.objects.get(name='Valves')
        pumps = Category.objects.get(name='Pumps')
        SubCategory.objects.create(name='Needle', code=0, category=valves)
        SubCategory.objects.create(name='Plug', code=100, category=valves)
        SubCategory.objects.create(name='Centrifugal', code=0, category=pumps)
        SubCategory.objects.create(name='Positive Displacement', code=100, category=pumps)
        needle_valves = SubCategory.objects.get(name='Needle')
        plug_valves = SubCategory.objects.get(name='Plug')
        centrifugal_pumps = SubCategory.objects.get(name='Centrifugal')
        positive_displacement_pumps = SubCategory.objects.get(name='Positive Displacement')
        Equipment.objects.create(description='PVC Needle Valve', category=valves, subcategory=needle_valves)
        Equipment.objects.create(description='SS Needle Valve', category=valves, subcategory=needle_valves)
        Equipment.objects.create(description='PVC Plug Valve', category=valves, subcategory=plug_valves)
        Equipment.objects.create(description='SS Plug Valve', category=valves, subcategory=plug_valves)
        Equipment.objects.create(description='Horizontal ANSI Style Centrifugal Pump', category=pumps, subcategory=centrifugal_pumps)
        Equipment.objects.create(description='Vertical ANSI Style Centrifugal Pump', category=pumps, subcategory=centrifugal_pumps)
        Equipment.objects.create(description='QD-400 Style Positive Displacement Pump', category=pumps, subcategory=positive_displacement_pumps)
        Equipment.objects.create(description='Danfoss Style Positive Displacement Pump', category=pumps, subcategory=positive_displacement_pumps)
 
    def test_that_first_equipment_gets_proper_code(self):
        PVC_needle_valve = Equipment.objects.get(description='PVC Needle Valve')
        PVC_plug_valve = Equipment.objects.get(description='PVC Plug Valve')
        Horizontal_ansi_centrifugal = Equipment.objects.get(description='Horizontal ANSI Style Centrifugal Pump')
        qd400 = Equipment.objects.get(description='QD-400 Style Positive Displacement Pump')
        self.assertEqual(PVC_needle_valve.code, '13.000')
        self.assertEqual(PVC_plug_valve.code, '13.100')
        self.assertEqual(Horizontal_ansi_centrifugal.code, '21.000')
        self.assertEqual(qd400.code, '21.100')

    def test_that_second_equipment_in_same_category_and_subcategory_get_incremented_code(self):
        SS_needle_valve = Equipment.objects.get(description='SS Needle Valve')
        SS_plug_valve = Equipment.objects.get(description='SS Plug Valve')
        Vertical_ansi_centrifugal = Equipment.objects.get(description='Vertical ANSI Style Centrifugal Pump')
        Danfoss = Equipment.objects.get(description='Danfoss Style Positive Displacement Pump')
        self.assertEqual(SS_needle_valve.code, '13.001')
        self.assertEqual(SS_plug_valve.code, '13.101')
        self.assertEqual(Vertical_ansi_centrifugal.code, '21.001')
        self.assertEqual(Danfoss.code, '21.101')

    def test_that_saving_without_modifications_does_not_increment_subcode(self):
        SS_needle_valve = Equipment.objects.get(description='SS Needle Valve')
        temp_subcode = SS_needle_valve.subcode
        SS_needle_valve.save()
        self.assertEqual(SS_needle_valve.subcode, temp_subcode)

    # Failing test right now. Need to decide if you want to allow category and
    # subcategory changes for a piece of equipment
    # def test_that_subcode_restarts_if_new_category_chosen_for_equipment(self):
    #     valves = Category.objects.get(name='Valves')
    #     plug_valves = SubCategory.objects.get(name='Plug')
    #     test_valve = Equipment.objects.get(description='PVC Needle Valve')
    #     test_valve.description = 'Now a plug valve'
    #     test_valve.category = valves
    #     test_valve.subcategory = plug_valves
    #     test_valve.save()
    #     self.assertEqual(test_valve.code, '13.100')

class SpecifiedEquipmentTestCase(TestCase):
    def setUp(self):
        Project.objects.create(code='WIN', name='Windsor', description='New plant')
        Project.objects.create(code='BH2', name='Blue Hills 2', description='Old plant')
        windsor = Project.objects.get(code='WIN')
        blue_hills = Project.objects.get(code='BH2')
        Category.objects.create(code=13, name='Valves')
        Category.objects.create(code=21, name='Pumps')
        valves = Category.objects.get(name='Valves')
        pumps = Category.objects.get(name='Pumps')
        SubCategory.objects.create(name='Needle', code=0, category=valves)
        SubCategory.objects.create(name='Plug', code=100, category=valves)
        SubCategory.objects.create(name='Centrifugal', code=0, category=pumps)
        SubCategory.objects.create(name='Positive Displacement', code=100, category=pumps)
        needle_valves = SubCategory.objects.get(name='Needle')
        plug_valves = SubCategory.objects.get(name='Plug')
        centrifugal_pumps = SubCategory.objects.get(name='Centrifugal')
        positive_displacement_pumps = SubCategory.objects.get(name='Positive Displacement')
        Equipment.objects.create(description='PVC Needle Valve', category=valves, subcategory=needle_valves)
        Equipment.objects.create(description='SS Needle Valve', category=valves, subcategory=needle_valves)
        Equipment.objects.create(description='PVC Plug Valve', category=valves, subcategory=plug_valves)
        Equipment.objects.create(description='SS Plug Valve', category=valves, subcategory=plug_valves)
        Equipment.objects.create(description='Horizontal ANSI Style Centrifugal Pump', category=pumps, subcategory=centrifugal_pumps)
        Equipment.objects.create(description='Vertical ANSI Style Centrifugal Pump', category=pumps, subcategory=centrifugal_pumps)
        Equipment.objects.create(description='QD-400 Style Positive Displacement Pump', category=pumps, subcategory=positive_displacement_pumps)
        Equipment.objects.create(description='Danfoss Style Positive Displacement Pump', category=pumps, subcategory=positive_displacement_pumps)
        pvc_needle_valve = Equipment.objects.get(description='PVC Needle Valve')
        ss_needle_valve = Equipment.objects.get(description='SS Needle Valve')
        qd400 = Equipment.objects.get(description='QD-400 Style Positive Displacement Pump')
        danfoss_pump = Equipment.objects.get(description='Danfoss Style Positive Displacement Pump')
        PlantSystem.objects.create(name='first pass RO')
        ro1 = PlantSystem.objects.get(name='first pass RO')
        Size.objects.create(display_string='1" NPS', code_string="0100")
        Size.objects.create(display_string='2" NPS', code_string="0200")
        p1 = Size.objects.get(code_string="0100")
        p2 = Size.objects.get(code_string="0200")
        SpecifiedEquipment.objects.create(equipment=pvc_needle_valve, size=p1)
        SpecifiedEquipment.objects.create(equipment=pvc_needle_valve, size=p2)
        SpecifiedEquipment.objects.create(equipment=qd400, size=p1)
        SpecifiedEquipment.objects.create(equipment=danfoss_pump, size=p1)
        # p1_pvc_needle_valve = SpecifiedEquipment.objects.get(equipment=pvc_needle_valve, size=p1)
        # p2_pvc_needle_valve = SpecifiedEquipment.objects.get(equipment=pvc_needle_valve, size=p2)
        # p1_qd400 = SpecifiedEquipment.objects.get(equipment=qd400, size=p1)
        # p1_danfoss_pump = SpecifiedEquipment.objects.get(equipment=danfoss_pump, size=p1)
        # TaggedEquipment.objects.create(name='V1', description='Pump Suction Valve', specified_equipment=p1_pvc_needle_valve, project=windsor, system=ro1)
        # TaggedEquipment.objects.create(name='V2', description='Pump Suction Valve', specified_equipment=p1_pvc_needle_valve, project=blue_hills, system=ro1)
        # TaggedEquipment.objects.create(name='V3', description='Pump Suction Valve', specified_equipment=p2_pvc_needle_valve, project=windsor, system=ro1)
        # TaggedEquipment.objects.create(name='P1', description='HP Pump 1', specified_equipment=p1_qd400, project=windsor, system=ro1)
        # TaggedEquipment.objects.create(name='P2', description='HP Pump 2', specified_equipment=p1_danfoss_pump, project=windsor, system=ro1)

    def test_first_inserted_specified_equipment_has_proper_code(self):
        pvc_needle_valve = Equipment.objects.get(description='PVC Needle Valve')
        p1 = Size.objects.get(code_string="0100")
        v1 = SpecifiedEquipment.objects.get(equipment=pvc_needle_valve, size=p1)
        self.assertEqual(v1.code, '13.000.0100')

    def test_subcode_resets_upon_adding_object_with_different_size_but_same_everything_else(self):
        pvc_needle_valve = Equipment.objects.get(description='PVC Needle Valve')
        p2 = Size.objects.get(code_string="0200")
        v3 = SpecifiedEquipment.objects.get(equipment=pvc_needle_valve, size=p2)
        self.assertEqual(v3.code, '13.000.0200')

    def test_subcode_goes_to_proper_increment_when_changing_size_field_to_join_other_non_unique_instances(self):
        pvc_needle_valve = Equipment.objects.get(description='PVC Needle Valve')
        p1 = Size.objects.get(code_string="0100")
        p2 = Size.objects.get(code_string='0200')
        V1 = SpecifiedEquipment.objects.get(equipment=pvc_needle_valve, size=p1)
        V1.size = p2
        V1.save()
        self.assertEqual(V1.code, '13.000.0200')
        
    def test_that_saving_without_modifications_does_not_increment_subcode(self):
        pvc_needle_valve = Equipment.objects.get(description='PVC Needle Valve')
        p1 = Size.objects.get(code_string="0100")
        V1 = SpecifiedEquipment.objects.get(equipment=pvc_needle_valve, size=p1)
        temp_code = V1.code
        V1.save()
        self.assertEqual(V1.code, temp_code)


class TaggedEquipmentTestCase(TestCase):
    def setUp(self):
        Project.objects.create(code='WIN', name='Windsor', description='New plant')
        Project.objects.create(code='BH2', name='Blue Hills 2', description='Old plant')
        windsor = Project.objects.get(code='WIN')
        blue_hills = Project.objects.get(code='BH2')
        Category.objects.create(code=13, name='Valves')
        Category.objects.create(code=21, name='Pumps')
        valves = Category.objects.get(name='Valves')
        pumps = Category.objects.get(name='Pumps')
        SubCategory.objects.create(name='Needle', code=0, category=valves)
        SubCategory.objects.create(name='Plug', code=100, category=valves)
        SubCategory.objects.create(name='Centrifugal', code=0, category=pumps)
        SubCategory.objects.create(name='Positive Displacement', code=100, category=pumps)
        needle_valves = SubCategory.objects.get(name='Needle')
        plug_valves = SubCategory.objects.get(name='Plug')
        centrifugal_pumps = SubCategory.objects.get(name='Centrifugal')
        positive_displacement_pumps = SubCategory.objects.get(name='Positive Displacement')
        Equipment.objects.create(description='PVC Needle Valve', category=valves, subcategory=needle_valves)
        Equipment.objects.create(description='SS Needle Valve', category=valves, subcategory=needle_valves)
        Equipment.objects.create(description='PVC Plug Valve', category=valves, subcategory=plug_valves)
        Equipment.objects.create(description='SS Plug Valve', category=valves, subcategory=plug_valves)
        Equipment.objects.create(description='Horizontal ANSI Style Centrifugal Pump', category=pumps, subcategory=centrifugal_pumps)
        Equipment.objects.create(description='Vertical ANSI Style Centrifugal Pump', category=pumps, subcategory=centrifugal_pumps)
        Equipment.objects.create(description='QD-400 Style Positive Displacement Pump', category=pumps, subcategory=positive_displacement_pumps)
        Equipment.objects.create(description='Danfoss Style Positive Displacement Pump', category=pumps, subcategory=positive_displacement_pumps)
        pvc_needle_valve = Equipment.objects.get(description='PVC Needle Valve')
        ss_needle_valve = Equipment.objects.get(description='SS Needle Valve')
        qd400 = Equipment.objects.get(description='QD-400 Style Positive Displacement Pump')
        danfoss_pump = Equipment.objects.get(description='Danfoss Style Positive Displacement Pump')
        PlantSystem.objects.create(name='first pass RO')
        ro1 = PlantSystem.objects.get(name='first pass RO')
        Size.objects.create(display_string='1" NPS', code_string="0100")
        Size.objects.create(display_string='2" NPS', code_string="0200")
        p1 = Size.objects.get(code_string="0100")
        p2 = Size.objects.get(code_string="0200")
        SpecifiedEquipment.objects.create(equipment=pvc_needle_valve, size=p1)
        SpecifiedEquipment.objects.create(equipment=pvc_needle_valve, size=p2)
        SpecifiedEquipment.objects.create(equipment=qd400, size=p1)
        SpecifiedEquipment.objects.create(equipment=danfoss_pump, size=p1)
        p1_pvc_needle_valve = SpecifiedEquipment.objects.get(equipment=pvc_needle_valve, size=p1)
        p2_pvc_needle_valve = SpecifiedEquipment.objects.get(equipment=pvc_needle_valve, size=p2)
        p1_qd400 = SpecifiedEquipment.objects.get(equipment=qd400, size=p1)
        p1_danfoss_pump = SpecifiedEquipment.objects.get(equipment=danfoss_pump, size=p1)
        TaggedEquipment.objects.create(name='V1', description='Pump Suction Valve', specified_equipment=p1_pvc_needle_valve, project=windsor, system=ro1)
        TaggedEquipment.objects.create(name='V2', description='Pump Suction Valve', specified_equipment=p1_pvc_needle_valve, project=blue_hills, system=ro1)
        TaggedEquipment.objects.create(name='V3', description='Pump Suction Valve', specified_equipment=p2_pvc_needle_valve, project=windsor, system=ro1)
        TaggedEquipment.objects.create(name='P1', description='HP Pump 1', specified_equipment=p1_qd400, project=windsor, system=ro1)
        TaggedEquipment.objects.create(name='P2', description='HP Pump 2', specified_equipment=p1_danfoss_pump, project=windsor, system=ro1)

    def test_first_inserted_tagged_equipment_has_proper_code(self):
        v1 = TaggedEquipment.objects.get(name='V1')
        self.assertEqual(v1.code, 'WIN.13.000.0100.000')

    def test_subcode_resets_upon_adding_object_with_different_project_but_same_everything_else(self):
        v2 = TaggedEquipment.objects.get(name='V2')
        self.assertEqual(v2.code, 'BH2.13.000.0100.000')

    def test_subcode_resets_upon_adding_object_with_different_size_but_same_everything_else(self):
        v3 = TaggedEquipment.objects.get(name='V3')
        self.assertEqual(v3.code, 'WIN.13.000.0200.000')

    def test_subcode_resets_upon_adding_object_with_different_system_but_same_everything_else(self):
        P2 = TaggedEquipment.objects.get(name='P2')
        self.assertEqual(P2.code, 'WIN.21.101.0100.000')

    def test_subcode_goes_to_0_when_changing_field_to_make_instance_unique(self):
        blue_hills = Project.objects.get(code='BH2')
        P2 = TaggedEquipment.objects.get(name='P2')
        P2.project = blue_hills
        P2.save()
        self.assertEqual(P2.code, 'BH2.21.101.0100.000')

    def test_subcode_goes_to_proper_increment_when_changing_equipment_field_to_join_other_non_unique_instances(self):
        blue_hills = Project.objects.get(code='BH2')
        V1 = TaggedEquipment.objects.get(name='V1')
        V1.project = blue_hills
        V1.save()
        self.assertEqual(V1.code, 'BH2.13.000.0100.001')

    def test_subcode_goes_to_proper_increment_when_changing_size_field_to_join_other_non_unique_instances(self):
        p2 = Size.objects.get(code_string='0200')
        V1 = TaggedEquipment.objects.get(name='V1')
        V1.specified_equipment.size = p2
        V1.save()
        self.assertEqual(V1.code, 'WIN.13.000.0200.001')
        
    def test_that_saving_without_modifications_does_not_increment_subcode(self):
        V1 = TaggedEquipment.objects.get(name='V1')
        temp_code = V1.code
        V1.save()
        self.assertEqual(V1.code, temp_code)
    
# Create your tests here.

# Test to show that if you change category or size
# the code updates appropriately
# viewing and saving should not increment
# should always start at 0 if first in a project and size and equipment