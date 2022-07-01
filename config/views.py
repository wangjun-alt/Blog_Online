from django.views.generic import ListView
from myblog.views import CommonViewMixin
from .models import Link
from django.http import HttpResponse

# def links(request):
#     return HttpResponse('links')

class LinkListView(CommonViewMixin, ListView):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    temp1ate_name = 'config/links.html'
    context_object_name = 'link_list'