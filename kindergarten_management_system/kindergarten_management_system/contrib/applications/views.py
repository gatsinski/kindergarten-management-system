import os

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from formtools.wizard.views import SessionWizardView

from .forms import ApplicationForm, ChildForm, ParentForm


FORMS = [
    ('application', ApplicationForm),
    ('parent', ParentForm),
    ('child', ChildForm),
]


TEMPLATES = {
    'application': 'applications/application_form.html',
    'parent': 'applications/parent_form.html',
    'child': 'applications/child_form.html',
}


class ApplicationWizard(SessionWizardView):
    form_list = FORMS
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT,
                                                           'applications'))

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, form_dict, **kwargs):
        parent = form_dict['parent'].save()
        application_instance = form_dict['application'].instance

        child_form = form_dict['child']
        child_form.instance.kindergarten = application_instance.kindergarten
        child = child_form.save()

        child.parents = [parent]
        child.save()

        application_instance.child = child
        application_instance.parent = parent
        form_dict['application'].save()

        return render(self.request,
                      'applications/application_success.html',
                      {'form_data': [form.cleaned_data for form in form_list]})


def create_application(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,
                          'applications/application_success.html',
                          context)
    else:
        form = ApplicationForm()
    context = {'form': form}
    return render(request, 'applications/application_form.html', context)
