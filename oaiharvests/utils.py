# utils.py

""" 
OAIUtils : A set of utility functions that handle requests and format responses for OAI provider. 

http://www.openarchives.org/OAI/openarchivesprotocol.html
"""

from oaipmh.client import BaseClient, Client
from oaipmh.metadata import MetadataRegistry, oai_dc_reader

# Sickle implementation: https://sickle.readthedocs.io/en/latest/
import string, urllib
from collections import defaultdict

from sickle import Sickle
from sickle.utils import xml_to_dict, get_namespace
from sickle.models import Record, Header


def dim_xml_to_dict(tree):
    fields = defaultdict(list)
    for tag in tree.getchildren():
        f = tag.get('element')
        q = tag.get('qualifier')
        if q: f += '.' + q
        fields[f].append(tag.text)    
    return dict(fields)

def get_bitstream_url(collection, record):
    """ Harvests an href pointing to the bitstream url for the record in repository.
    E.g., https://scholarspace.manoa.hawaii.edu/bitstream/10125/25006/1/editor.pdf
    """
    try:

        sickle = Sickle(collection.community.repository.base_url)        
        sickle.class_mapping['GetRecord'] = LltRecordBitstream
        record = sickle.GetRecord(metadataPrefix='ore', identifier=record.header.identifier)
        return record.metadata['bitstream'][0].replace('+', '%20')
    except Exception as e:
        print e, 'Unable to construct bitstream url.'
        return None


class LltRecord(Record):
    """ XML Record handler override for dim metadata format. """    
    def __init__(self, record_element, strip_ns=True):
        super(LltRecord, self).__init__(record_element, strip_ns=strip_ns)
        self.header = Header(self.xml.find('.//' + self._oai_namespace + 'header'))

        tree = self.xml.find('.//' + self._oai_namespace + 'metadata').getchildren()[0]
        self.metadata = dim_xml_to_dict(tree)


class LltRecordBitstream(Record):
    """ XML Record handler override for ore metadata format. Used to retrieve bitstream url for a record."""    
    def __init__(self, record_element, strip_ns=True):
        super(LltRecordBitstream, self).__init__(record_element, strip_ns=strip_ns)
        self._oai_namespace = get_namespace(self.xml)
        
        tree = self.xml.find('.//' + self._oai_namespace + 'metadata').getchildren()[0]
        bitstream_urls = tree.findall('.//'+ '{http://www.w3.org/2005/Atom}'+'link')
        for i in bitstream_urls:
            if i.get('rel') == 'http://www.openarchives.org/ore/terms/aggregates':
                self.metadata = {'bitstream': [i.get('href')]}


class OAIUtils(object):
    repositories = []
    communities = []
    collections = []


    def list_oai_community_sets(self, repository):

        try:
            registry = MetadataRegistry()
            registry.registerReader('oai_dc', oai_dc_reader)
            client = Client(repository.base_url, registry)
            sets = client.listSets()
        except:
            return

        """ Filter records to build list of community sets """
        self.communities = []
        for i in sets:
            set_id = i[0]
            set_name = i[1]
            """ Build collection tuples (id, human readable name) """
            if set_id[:3] == 'com':
                set_data = []
                set_data.append(set_id)
                set_data.append(set_name)
                self.communities.append(set_data)

        self.communities = sorted(
            self.communities, key=lambda community: community[1])

    def list_oai_collections(self, community):
        """ Retrieve the header data for each subset within the set indicated by 
        community parameter.
        """
        try:
            sickle = Sickle(community.repository.base_url)
            records = sickle.ListIdentifiers(metadataPrefix='oai_dc', set=community.identifier)
            # registry = MetadataRegistry()
            # registry.registerReader('oai_dc', oai_dc_reader)
            # client = Client(community.repository.base_url, registry)
            # records = client.listIdentifiers(
            #     metadataPrefix='oai_dc', set=community.identifier)
        except:
            community_collections = set()
            return


        # Filter through records to build list of collections in the set
        # existing_cols = Collection.objects.all().values_list('pk')
        community_collections = {}
        for i in records:
            for j in i.setSpecs:
                if j[:3] == 'col':
                    community_collections[j] = None

    
        # Build collection tuples (identifier, name) 
        sickle = Sickle(community.repository.base_url)
        sets = sickle.ListSets()
        print community_collections
        for i in sets:
            try:
                # print i.setSpec
                coll = community_collections[i.setSpec]
                community_collections[i.setSpec] = i.setName
            except:
                pass

        self.collections = community_collections.items()

        # for i, j in community_collections.items():

            # print i
            # print community_collections
            
            # set_data = []
            # set_data.append(i)  # Store identifier
            # set_data.append('Collection: %s'%i)  # Store human readable name
            # # print set_data
            # self.collections.append(set_data)

    def harvest_oai_collection_records(self, collection):
        records = []
        try:
            registry = MetadataRegistry()
            registry.registerReader('oai_dc', oai_dc_reader)
            client = Client(collection.community.repository.base_url, registry)
            records = client.listRecords(
                metadataPrefix='oai_dc', set=collection.identifier)
        except:
            return

        return records

    def harvest_oai_collection_records_sickle(self, collection):
        sickle = Sickle(collection.community.repository.base_url)
        sickle.class_mapping['ListRecords'] = LltRecord

        records = sickle.ListRecords(metadataPrefix='dim', set=collection.identifier)
        return records

############################################
        # records = []
        # try:
        #     registry = MetadataRegistry()
        #     registry.registerReader('oai_dc', oai_dc_reader)
        #     client = Client(collection.community.repository.base_url, registry)
        #     records = client.listRecords(
        #         metadataPrefix='oai_dc', set=collection.identifier)
        # except:
        #     return

        # return records        







