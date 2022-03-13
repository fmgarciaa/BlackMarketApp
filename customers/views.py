from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Customers

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class CustomerList(ListView):
    model=Customers

class CustomerCreate(SuccessMessageMixin, CreateView):
    model=Customers
    form=Customers
    fields=('full_name', 'phone_number', 'direction', 'district', 'reference')
    success_message="Customer created succesfully"

    def get_success_url(self):
        return reverse('customer:list')

class CustomerDetail(DetailView):
    model=Customers

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Customers.objects.all()
        context['filter'] = CustomerFilter(self.request.GET, queryset=Customers.objects.all())
        return context

class CustomerUpdate(SuccessMessageMixin, UpdateView):
    model=Customers
    form=Customers
    fields=('full_name', 'phone_number', 'direction', 'district', 'reference', 'is_regular_client')
    success_message='Update Customer successfully!'

    def get_success_url(self):
        return reverse('customer:list')

class CustomerDelete(SuccessMessageMixin, DeleteView):
    model=Customers
    form=Customers
    fields='__all__'

    def get_success_url(self):
        success_message='the client has been successfully deleted'
        messages.success(self.request, (success_message))
        return reverse('customer:list')



