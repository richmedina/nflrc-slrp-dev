from oaiharvests.models import *
from oaiharvests.utils import OAIUtils as OAI
from oaiharvests.utils import batch_harvest_issues

base_url = 'http://scholarspace.manoa.hawaii.edu/dspace-oai/request'
# community = 'col_10125_35870' # llt vol
community = 'com_10125_27123' # llt comm
# community = 'com_10125_6033'  # nflrc comm
md = 'qdc'

repo = Repository.objects.all()[0]
com = Community.objects.all()[0]
cols = Collection.objects.all()
batch_harvest_issues(com)

oai = OAI()
issues = oai.list_oai_collections(com)
print len(issues)
recs = oai.harvest_oai_collection_records_sickle(cols[0])
for i in recs:
    print i
# existing = Collection.objects.all().values_list('identifier')
# d = list(existing)