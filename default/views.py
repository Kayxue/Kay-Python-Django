from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

## Create your views here.
## 投票主題列表
class PollList(ListView):
    model = Poll
class PollDetail(DetailView):
    model = Poll

    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['options'] = Option.objects.filter(poll_id=self.kwargs['pk'])
        return ctx