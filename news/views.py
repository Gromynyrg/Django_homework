from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from .models import Articles, Category
from .forms import ArticlesForm


# Create your views here.

def create(request):
    error = ''
    form = ArticlesForm()
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена неверно'
    data = {'form': form, 'error': error}
    return render(request, 'news/create.html', data)


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/news_delete.html'
    success_url = '/news/'


class CategoryAllNewsView(ListView):
    model = Articles
    context_object_name = 'news'
    template_name = 'news/news_home.html'

    def get_queryset(self):
        category = Category.objects.get(pk=self.kwargs['pk'])
        queryset = Articles.objects.all().filter(category=category.id)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['current_category'] = category
        context['news_count'] = len(Articles.objects.all().filter(category=category.id))
        return context


def news_home(request):
    news = Articles.objects.order_by('-date')
    news_count = news.count()
    return render(request, 'news/news_home.html', {'news': news, 'news_count': news_count})
