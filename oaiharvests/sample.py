from oaiharvests.models import *
from oaipmh.client import BaseClient, Client
from oaipmh.metadata import MetadataRegistry, oai_dc_reader

base_url = 'http://scholarspace.manoa.hawaii.edu/dspace-oai/request'
# community = 'col_10125_35870' # llt vol
community = 'com_10125_27123' # llt comm
# community = 'com_10125_6033'  # nflrc comm
md = 'qdc'

registry = MetadataRegistry()
registry.registerReader(md, oai_dc_reader)
client = Client(base_url, registry)
print dir(client)
records = client.listRecords(metadataPrefix=md, set=community)
sets = client.listSets(metadataPrefix=md, set=community)
reclist = list(records)
for i in reclist:
    print 'community record:', i, i.setSpec()


'oai:scholarspace.manoa.hawaii.edu:10125/24502'
# vols = Collection.objects.all()
# v = vols[0]
