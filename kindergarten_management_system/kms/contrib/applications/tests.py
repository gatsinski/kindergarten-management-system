from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from .forms import ApplicationForm, ParentForm, ChildForm
from kms.contrib.kindergartens import models


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

ParentFormData = {
    'username': 'parent',
    'first_name': 'Name',
    'middle_name': 'Middle',
    'last_name': 'Last',
    'email': 'parent_email@kindergarten.com',
    'address': 'Parent Address',
    'telephone': '1234512345'
}

ChildFormData = {
    'first_name': 'Name',
    'middle_name': 'Middle',
    'last_name': 'Last',
    'birthdate': '2010-01-01',
    'personal_id': '1234512345',
    'address': 'Child Address',
}


class ModelTests(TestCase):
    def setUp(self):
        self.city = models.City.objects.create(**CityData)
        self.kindergarten_type = models.KindergartenType.objects.\
            create(**KindergartenTypeData)
        self.kindergarten = models.Kindergarten.objects.\
            create(**KindergartenData,
                   city=self.city,
                   type=self.kindergarten_type)

    def test_application_form(self):
        application_form_data = {'kindergarten': 1,
                                 'attachment_set-0-name': 'Attachment 1',
                                 'attachment_set-MIN_NUM_FORMS': 1,
                                 'attachment_set-MAX_NUM_FORMS': 100,
                                 'attachment_set-INITIAL_FORMS': 0,
                                 'attachment_set-TOTAL_FORMS': 1}
        application_form_files = \
            {'attachment_set-0-file': SimpleUploadedFile("file.pdf",
                                                         b"Content")}
        application_form = ApplicationForm(application_form_data,
                                           application_form_files)
        self.assertTrue(application_form.is_valid())
        self.assertDictEqual(application_form.errors, {})

    def test_application_form_without_attachment(self):
        application_form_data = {'kindergarten': 1,
                                 'attachment_set-0-name': '',
                                 'attachment_set-MIN_NUM_FORMS': 1,
                                 'attachment_set-MAX_NUM_FORMS': 100,
                                 'attachment_set-INITIAL_FORMS': 0,
                                 'attachment_set-TOTAL_FORMS': 1}
        application_form = ApplicationForm(application_form_data)
        self.assertFalse(application_form.is_valid())

    def test_parent_form(self):
        parent_form = ParentForm(ParentFormData)
        self.assertTrue(parent_form.is_valid())
        self.assertDictEqual(parent_form.errors, {})

    def test_child_form(self):
        child_form = ChildForm(ChildFormData)
        self.assertTrue(child_form.is_valid())
        self.assertDictEqual(child_form.errors, {})
