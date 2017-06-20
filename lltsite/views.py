import json, operator
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from collections import Counter
from django.db.models import Q

from oaiharvests.models import Community, Collection, Record, MetadataElement

from .mixins import RecordSearchMixin


class HomeView(TemplateView):
    template_name = 'home.html'
    queryset = None

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['volumes'] = [(vol, vol.list_records()) for vol in Collection.objects.all().order_by('-name')]
        return context


class CommunityView(DetailView):
    model = Community
    template_name = 'community_view.html'

    def get_context_data(self, **kwargs):
        context = super(CommunityView, self).get_context_data(**kwargs)
        context['collections'] = self.get_object().list_collections()
        return context


class CollectionListView(ListView):
    model = Collection
    template_name = 'collection_list.html'

    def get_context_data(self, **kwargs):
        context = super(CollectionListView, self).get_context_data(**kwargs)
        return context


class CollectionView(DetailView):
    model = Collection
    template_name = 'collection_view.html'
    queryset = None

    def get_context_data(self, **kwargs):
        context = super(CollectionView, self).get_context_data(**kwargs)
        context['toc'] = dict(self.get_object().list_toc())
        context['size'] = len(context['toc'])
        return context


class ItemView(DetailView):
    model = Record
    template_name = 'item_view.html'

    def get_context_data(self, **kwargs):
        context = super(ItemView, self).get_context_data(**kwargs)
        context['item_data'] = self.get_object().as_display_dict()
        return context


class ItemViewFull(DetailView):
    model = Record
    template_name = 'item_view_full.html'

    def get_context_data(self, **kwargs):
        context = super(ItemViewFull, self).get_context_data(**kwargs)
        context['item_data'] = self.get_object().as_dict()
        return context


class LanguageView( ListView):
    model = Record
    template_name = 'collection_view.html'

    def get_context_data(self, **kwargs):
        query = self.kwargs['query']        
        self.queryset = Record.objects.filter(data__element_type='language').filter(
            data__element_data__icontains=query)
        
        context = super(LanguageView, self).get_context_data(**kwargs)
        context['items'] = self.queryset
        context['size'] = len(self.queryset)   
        context['object'] = query + ' language'
        return context


class ContributorView(ListView):
    model = Record
    template_name = 'collection_view.html'

    def get_context_data(self, **kwargs):
        query = self.kwargs['query']
        self.queryset = []
        if len(query.split('-')) != 1:
            firstQuery = query.split('-')[0]
            lastQuery = query.split('-')[1]
            q = MetadataElement.objects.filter(element_type='contributor').filter(Q(element_data__icontains=firstQuery) & Q(element_data__icontains=lastQuery))
            
        else:
            q = MetadataElement.objects.filter(element_type='contributor').filter(element_data__icontains=query)

        for i in q:
            self.queryset.append(i.record)

        context = super(ContributorView, self).get_context_data(**kwargs)
        context['items'] = self.queryset
        context['size'] = len(self.queryset)
        context['object'] = query
        return context


class SearchView(ListView):
    template_name = 'search.html'

    def post(self, request, *args, **kwargs):
        # arrays to hold values
        self.items = []

        # Grab POST values from the search query
        self.query = self.request.POST.get('query')
        self.key = self.request.POST.get('key')

        self.queryset = MetadataElement.objects.filter(
            element_type=self.query).filter(element_data__icontains=self.key)

        for element in MetadataElement.objects.filter(element_type=self.query).filter(element_data__icontains=self.key):
            self.items.append(element.record)

        return super(SearchView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['items'] = self.items
        context['len'] = len(self.items)
        context['query'] = self.query
        context['key'] = self.key
        # pdb.set_trace()
        return context


class SearchPage(RecordSearchMixin, ListView):
    model = Record
    template_name = 'searchtest.html'
