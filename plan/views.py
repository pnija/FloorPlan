from django.shortcuts import render

from django.views.generic import FormView
from .forms import PlanDataForm


class PlanDataView(FormView):
    template_name = 'plan_data.html'
    form_class = PlanDataForm