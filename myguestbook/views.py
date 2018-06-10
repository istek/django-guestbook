from myguestbook.models import Guestbook
from django.views import generic
from .forms import MessageForm


# Create your views here.


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Guestbook.objects.order_by('-create_time')


class NewView(generic.CreateView):
    model = Guestbook
    template_name = 'guestbook_form.html'
    fields = ['name', 'email', 'avatar', 'weburl', 'content']
