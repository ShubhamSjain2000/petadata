from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from workflow.models import WorkSpace


class WorkSpaceListView(ListView):

    model = WorkSpace
    template_name = 'list_workspace.html'

    def get_queryset(self):

        return self.model.objects.filter(participants=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):

       context = super().get_context_data()
       context['abc'] = 'DEF'
       return context
class WorkSpaceCreateView(CreateView):

    model = WorkSpace
    template_name = 'create_workspace.html'
    fields = ['name']
    success_url = '/workflow/ui/workspace'

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        workspace = form.save(commit=False)
        workspace.created_by = self.request.user
        workspace.save()
        workspace.participants.set([self.request.user])
        workspace.save()
        return super().form_valid(form)



