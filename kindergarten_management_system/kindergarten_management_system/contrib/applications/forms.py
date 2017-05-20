from django import forms
from django.forms import inlineformset_factory, BaseInlineFormSet

from .models import Application, Attachment
from kindergarten_management_system.contrib.children.models import Child
from kindergarten_management_system.contrib.parents.models import Parent


AttachmentFormset = inlineformset_factory(Application,
                                          Attachment,
                                          extra=0,
                                          min_num=1,
                                          validate_min=True,
                                          fields=('name', 'file'))


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('kindergarten',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.formset = AttachmentFormset(self.data if self.is_bound else None,
                                         self.files if self.is_bound else None,
                                         instance=self.instance)

    def is_valid(self):
        return super().is_valid() and self.formset.is_valid()

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
            self.formset.save()
            instance.send_staff_email()
            instance.send_client_email()
        return instance


class ParentForm(forms.ModelForm):

    class Meta:
        model = Parent
        fields = ('username',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'email',
                  'address',
                  'telephone',)


class ChildForm(forms.ModelForm):

    class Meta:
        model = Child
        fields = ('first_name',
                  'middle_name',
                  'last_name',
                  'birthdate',
                  'personal_id',
                  'address')
