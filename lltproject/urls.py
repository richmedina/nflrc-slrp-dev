from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from lltsite.views import (
    HomeView, 
    CommunityView, 
    CollectionListView, 
    CollectionView, 
    ItemView, 
    ItemViewFull,
    PageView,
    PageViewPrivate,
    KeywordBrowseView,
    LanguageView, 
    ContributorView, 
    SearchHaystackView,
)

from oaiharvests.views import (
    OaiRepositoryListView, 
    OaiRepositoryCreateView, 
    OaiRepositoryUpdateView, 
    OaiRepositoryDeleteView, 
    OaiRepositoryView,
    OaiCommunityView,
    OaiCommunityCreateView,
    OaiCommunityUpdateView,
    OaiCommunityDeleteView,
    OaiCommunityHarvestView,
    OaiCollectionView,
    OaiCollectionCreateView,
    OaiCollectionUpdateView,
    OaiCollectionDeleteView,
    OaiCollectionHarvestView
)

urlpatterns = [

   # ---------- SITE VIEWS ------------- #

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^community/(?P<pk>\w+)$',
     CommunityView.as_view(), name='community'),                       

    url(r'^collections/$', CollectionListView.as_view(),
     name='collection_list'),

    url(r'^collection/(?P<pk>\w+)$',
     CollectionView.as_view(), name='collection'),

    url(r'^item/(?P<pk>\w+)$',
     ItemView.as_view(), name='item'),

    url(r'^item-detail/(?P<pk>\w+)$',
     ItemViewFull.as_view(), name='item_full'),

    url(r'^page/(?P<pk>\w+)$',
     PageView.as_view(), name='page_view'),

    url(r'^keys/$',
     KeywordBrowseView.as_view(), name='keyword_browse_view'),

    url(r'^staff-page/(?P<pk>\w+)$',
     PageViewPrivate.as_view(), name='staff_page_view'),

    url(r'^language/(?P<query>\w+)$',
     LanguageView.as_view(), name='language'),

    # url(r'^depositor/(?P<query>\w+)$',
    #     ContributorView.as_view(), name='collection'),

    url(r'^contributor/(?P<query>[-\w]+)$',
     ContributorView.as_view(), name='contributor'),

    url(r'^search/$',
       SearchHaystackView.as_view(), name='haystack_search'),

    # url(r'^searchtest/$',
    #    SearchPage.as_view(), name='searchtest'),

    # url(r'^search/', include('haystack.urls')),



    # ---------- OAI HARVESTER VIEWS ------------- #
    # Institutional Repositories #
    url(r'^oaiharvester/$', OaiRepositoryListView.as_view(),
     name='oai_repository_list'),
    url(r'^oaiharvester/repository/add/$',
     OaiRepositoryCreateView.as_view(
     ), name='oai_repository_add'),
    url(r'^oaiharvester/repository/edit/(?P<pk>\w+)$',
     OaiRepositoryUpdateView.as_view(
     ), name='oai_repository_edit'),
    url(r'^oaiharvester/repository/delete/(?P<pk>\w+)$',
     OaiRepositoryDeleteView.as_view(
     ), name='oai_repository_delete'),
    url(r'^oaiharvester/repository/(?P<pk>\w+)$',
     OaiRepositoryView.as_view(), name='oai_repository'),

    # Community Collections #
    url(r'^oaiharvester/community/(?P<pk>\w+)$',
     OaiCommunityView.as_view(), name='oai_community'),
    url(r'^oaiharvester/community/add/(?P<pk>\w+)$',
     OaiCommunityCreateView.as_view(
     ), name='oai_community_add'),
    url(r'^oaiharvester/community/edit/(?P<pk>\w+)$',
     OaiCommunityUpdateView.as_view(
     ), name='oai_community_edit'),
    url(r'^oaiharvester/community/delete/(?P<pk>\w+)$',
     OaiCommunityDeleteView.as_view(
     ), name='oai_community_delete'),
    url(r'^oaiharvester/community/harvest/(?P<pk>\w+)$',
     OaiCommunityHarvestView.as_view(
     ), name='oai_harvest_community'),

    # Collections #
    url(r'^oaiharvester/collection/(?P<pk>\w+)$',
     OaiCollectionView.as_view(), name='oai_collection'),
    url(r'^oaiharvester/collection/add/(?P<community>\w+)$',
     OaiCollectionCreateView.as_view(
     ), name='oai_collection_add'),
    url(r'^oaiharvester/collection/edit/(?P<pk>\w+)$',
     OaiCollectionUpdateView.as_view(
     ), name='oai_collection_edit'),
    url(r'^oaiharvester/collection/delete/(?P<pk>\w+)$',
     OaiCollectionDeleteView.as_view(
     ), name='oai_collection_delete'),
    url(r'^oaiharvester/collection/harvest/(?P<pk>\w+)$',
     OaiCollectionHarvestView.as_view(
     ), name='oai_harvest_collection'),

    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls), name='index'),
]
