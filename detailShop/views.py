from django.db.models import Q
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView, CreateView
from django_filters.views import FilterView
from django import forms

from detailShop import filters
from detailShop.form import OrderForm, OrderElementFormSet
from detailShop.models import Detail, Category, Order, OrderElement


class Index(TemplateView):
    template_name = 'index.html'
    model = Detail
    context_object_name = 'details'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Главная'
        context['content'] = "Магазин автозапчастей"
        context['details'] = Detail.objects.all()

        context['categories'] = Category.objects.all()
        selected_category = self.request.GET.get('category')

        if selected_category:
            context['details'] = Detail.objects.filter(category__id=selected_category)
        else:

            context['details'] = Detail.objects.all()

        return context


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    details = Detail.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'details': details})

def delivery(request):
    template_name = 'delivery_info.html'
    return render(request, template_name)

def about(request):
    template_name = 'about_info.html'
    return render(request, template_name)

def search(request):
    results = Detail.objects.none()  # Start with an empty QuerySet
    query = request.GET.get('search', '').strip()  # Get the search query and strip whitespace

    if query:
        results = Detail.objects.filter(Q(name__icontains=query))



    return render(request, 'search.html', {'query': query, 'results': results})


class DetailList(FilterView):
    model = Detail
    template_name = 'detail_list.html'
    context_object_name = 'detail'
    filterset_class = filters.DetailFilter

class DetailDetail(DetailView):
    model = Detail
    template_name = 'detail_detail.html'
    context_object_name = 'detail'

class OrderCreate(CreateView):
    model = Order
    template_name = 'create_order.html'
    success_url = reverse_lazy('order_list')

    def get_form_class(self):
        return OrderForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = OrderElementFormSet(self.request.POST)
        else:
            context['formset'] = OrderElementFormSet(queryset=OrderElement.objects.none())
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid():
            order = form.save()

            for order_element_form in formset:
                order_element = order_element_form.save(commit=False)
                order_element.order = order
                order_element.save()
            order.calculate_sum()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class OrderList(FilterView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'order'