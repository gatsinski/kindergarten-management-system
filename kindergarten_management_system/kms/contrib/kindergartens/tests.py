from django.test import TestCase
from .models import Kindergarten, KindergartenType, City


CityData = {
    'name': 'City name'
}

KindergartenTypeData = {
    'name': 'Kindergarten type name'
}


KindergartenData = {
    'name': 'Test Kindergarten Name',
    'address': 'Test Kindergarten Address'
}


class ModelTests(TestCase):
    def setUp(self):
        self.city = City.objects.create(**CityData)
        self.kindergarten_type = KindergartenType.objects.\
            create(**KindergartenTypeData)
        self.kindergarten = Kindergarten.objects.\
            create(**KindergartenData,
                   city=self.city,
                   type=self.kindergarten_type)

    def test_city_creation(self):
        self.assertTrue(City.objects.filter(**CityData).exists())
        self.assertEqual(self.city, City.objects.get(**CityData))

    def test_kindergarten_type_creation(self):
        filter = KindergartenType.objects.filter(**KindergartenTypeData)
        self.assertTrue(filter.exists())
        object = KindergartenType.objects.get(**KindergartenTypeData)
        self.assertEqual(self.kindergarten_type, object)
