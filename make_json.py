from data_from_web import extraction
from data_from_web import features_sublist
from data_from_web import get_all_links
hackathon_names_list=[]
college_names_list=[]
features_list=[]
extraction(hackathon_names_list,college_names_list,features_list)

mode=[]
teamSize=[]
numberOfRegistrations=[]
features_sublist(0,features_list,mode)
features_sublist(1,features_list,teamSize)
features_sublist(2,features_list,numberOfRegistrations)


list_of_links=get_all_links('MuiGrid-root.MuiGrid-container.jobFeature-title-bg.css-5dis7f')

