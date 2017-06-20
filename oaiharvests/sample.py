from oaiharvests.models import *
from oaiharvests.utils import OAIUtils as OAI
from oaiharvests.utils import batch_harvest_issues

base_url = 'http://scholarspace.manoa.hawaii.edu/dspace-oai/request'
community = 'com_10125_27123' # llt comm

repo = Repository.objects.all()[0]
com = Community.objects.all()[0]
batch_harvest_issues(com)

cols = Collection.objects.all()
oai = OAI()
issues = oai.list_oai_collections(com)
recs = oai.harvest_oai_collection_records_sickle(cols[0])
for i in recs:
    print i
