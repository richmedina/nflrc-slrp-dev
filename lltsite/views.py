import json
from operator import itemgetter
from collections import Counter

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q

from braces.views import LoginRequiredMixin
from haystack.generic_views import SearchView

from oaiharvests.models import Community, Collection, Record, MetadataElement
from .models import StoryPage
from .mixins import RecordSearchMixin


class HomeView(TemplateView):
    template_name = 'home.html'
    queryset = None

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        journal = Community.objects.all()[0]
        context['keywords'] =  journal.aggregate_keywords()
        context['volumes'] = journal.list_collections_by_volume()
        context['latest'] = [(vol, vol.list_records()) for vol in Collection.objects.all().order_by('-name')][0]
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
        bitstream = context['item_data']['bitstream'][0]
        context['pdf_filename'] = bitstream[bitstream.rfind('/')+1:]
        return context


class ItemViewFull(DetailView):
    model = Record
    template_name = 'item_view_full.html'

    def get_context_data(self, **kwargs):
        context = super(ItemViewFull, self).get_context_data(**kwargs)
        context['item_data'] = self.get_object().as_dict()
        return context


class PageView(DetailView):
    model = StoryPage
    template_name = 'page_view.html'
    context_object_name = 'page'

    def get(self, request, *args, **kwargs):
        if self.get_object().private:
            return redirect('staff_page_view', item=self.get_object().id)
        return super(PageView, self).get(request, *args, **kwargs)


class PageViewPrivate(LoginRequiredMixin, DetailView):
    model = StoryPage
    template_name = 'page_view.html'
    context_object_name = 'page'


class SearchHaystackView(SearchView):
    def get_context_data(self, *args, **kwargs):
        context = super(SearchHaystackView, self).get_context_data(*args, **kwargs)

        keylist = ['Assessment/Testing','Behavior-tracking Technology','Blended/Hybrid Learning and Teaching','Code Switching','Collaborative Learning','Computer-Mediated Communication','Concordancing','Corpus','Culture','Data-driven Learning','Digital Literacies','Discourse Analysis','Distance/Open Learning and Teaching','Eye Tracking','Feedback','Game-based Learning and Teaching','Grammar','Human-Computer Interaction','Indigenous Languages','Instructional Context','Instructional Design','Language for Special Purposes','Language Learning Strategies','Language Maintenance','Language Teaching Methodology','Learner Attitudes','Learner Autonomy','Learner Identity','Less Commonly Taught Languages','Listening','Meta Analysis','Mobile Learning','MOOCs','Multiliteracies','Natural Language Processing','Open Educational Resources','Pragmatics','Pronunciation','Reading','Research Methods','Social Context','Sociocultural Theory','Social Networking','Speaking','Speech Recognition','Speech Synthesis','Task-based Learning and Teaching','Teacher Education','Telecollaboration','Ubiquitous Learning and Teaching','Virtual Environments','Vocabulary','Writing']

        cols_length = len(keylist) / 3
        keytable = []
        for i in range(0, len(keylist), cols_length):
            keytable.append(keylist[i:i+cols_length])

        authorlist = []
        for i in MetadataElement.objects.filter(element_type='contributor.author'):
            for j in json.loads(i.element_data):
                
                n = j.split(',')
                try:
                    authorlist.append((n[1].strip(), n[0].strip()))
                except:
                    pass
        authorlist = set(authorlist)
        authorlist = sorted(authorlist, key=lambda author: author[1])
        cols_length = len(authorlist) / 6
        authortable = []
        for i in range(0, len(authorlist), cols_length):
            authortable.append(authorlist[i:i+cols_length])

        context['authortable'] = authortable
        context['keytable'] = keytable
        return context



class KeywordBrowseView(TemplateView):
    template_name = 'page_keyword_browse.html'

    def get_context_data(self, **kwargs):
        context = super(KeywordBrowseView, self).get_context_data(**kwargs)
        
        keylist = ['Assessment/Testing','Behavior-tracking Technology','Blended/Hybrid Learning and Teaching','Code Switching','Collaborative Learning','Computer-Mediated Communication','Concordancing','Corpus','Culture','Data-driven Learning','Digital Literacies','Discourse Analysis','Distance/Open Learning and Teaching','Eye Tracking','Feedback','Game-based Learning and Teaching','Grammar','Human-Computer Interaction','Indigenous Languages','Instructional Context','Instructional Design','Language for Special Purposes','Language Learning Strategies','Language Maintenance','Language Teaching Methodology','Learner Attitudes','Learner Autonomy','Learner Identity','Less Commonly Taught Languages','Listening','Meta Analysis','Mobile Learning','MOOCs','Multiliteracies','Natural Language Processing','Open Educational Resources','Pragmatics','Pronunciation','Reading','Research Methods','Social Context','Sociocultural Theory','Social Networking','Speaking','Speech Recognition','Speech Synthesis','Task-based Learning and Teaching','Teacher Education','Telecollaboration','Ubiquitous Learning and Teaching','Virtual Environments','Vocabulary','Writing']

        cols_length = len(keylist) / 3
        keytable = []
        for i in range(0, len(keylist), cols_length):
            keytable.append(keylist[i:i+cols_length])

        context['keytable'] = keytable
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

