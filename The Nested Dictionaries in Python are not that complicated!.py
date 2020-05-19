#!/usr/bin/env python
# coding: utf-8

# # Task at hand :-
#     
# We have two dictionaries. Let’s call them dict1 and dict2. The idea is to check whether a certain key called ‘column’ exists in the first dictionary (dict1).
# 
# If yes, then fetch the corresponding value/s (as there can be multiple occurrences), and then search the same fetched values as keys in the second dictionary and fetch their corresponding values from the second dictionary.
# 
# If no, then fetch the key value pairing of the key ‘ensembl_sample_id’ from dict1. If the key is found then, print the key value pairing, else print 'ensembl_sample_id : " ".
# 
# The results in either case have to be transformed into a new third dictionary and printed. We will call it dict3.
# 
# So, let’s look at how these two dictionaries (dict1 & dict2) look 
# 
# dict1 = {‘ensembl_sample_id’: {‘mandatory’: True}, ‘ensembl_name’: {‘column’: ‘Name’}, ‘hgnc_id’: {‘column’: ‘description’}}
# 
# dict2 = “ID=gene:SNSG00000223972;Name=SSX11L1;biotype=transcribe;description=DEAD/H-box helicase 11 like 1 [Source:HGNC Symbol%3BAcc:HGNC:37102];sample_id=SNSG00000223972;logic_name=javana_hemo_saiens;version=6”
# 
# Well, if you look at it, we really need to make dict2 look like a dictionary. So, what do we do about that? We will get the lambda at splitting.
# 
# Use :— 
# 
# dict(map(lambda x: x.split(‘=’), dict2.split(‘;’)))
# 
# And that will make dict2 look like (which is what we really need) :-
# 
# dict2 = {‘ID’: ‘gene:SNSG00000223972’,
# ‘Name’: ‘SSX11L1’,
# ‘biotype’: ‘transcribe’,
# ‘description’: ‘DEAD/H-box helicase 11 like 1 [Source:HGNC Symbol%3BAcc:HGNC:37102]’,
# ‘sample_id’: ‘SNSG00000223972’,
# ‘logic_name’: ‘javana_hemo_saiens’,
# ‘version’: ‘6’}
# 
# And, now let’s get to work. I am sure the following script is quite comprehensive and self-explanatory :-

# In[2]:


get_ipython().system('pip install nested-lookup')

from nested_lookup import nested_lookup

dict1 = {'ensembl_sample_id': {'mandatory': True}, 'ensembl_name': {'columnn': 'Name'}, 'hgnc_id': {'columnn': 'description'}}

dict2 = {'ID': 'gene:SNSG00000223972',
 'Name': 'SSX11L1',
 'biotype': 'transcribe',
 'description': 'DEAD/H-box helicase 11 like 1 [Source:HGNC Symbol%3BAcc:HGNC:37102]',
 'sample_id': 'SNSG00000223972',
 'logic_name': 'javana_hemo_saiens',
 'version': '6'}

dict3 = {}

lookup_dict2 = nested_lookup('column', dict1)
print("Let's look at the value/s corresponding to key 'column' in dict1:",nested_lookup('column', dict1))
fetch_key = 'ensembl_sample_id'
fetch = nested_lookup(fetch_key, dict1)
print("Let's look at the value corresponding to key 'ensembl_sample_id' in dict1:", nested_lookup('ensembl_sample_id', dict1))

if len(lookup_dict2) != 0:
    
    for i in lookup_dict2:
        dict3.update({i : dict2[i]} )
        
elif len(fetch) != 0:
    
    for j in fetch:
        dict3.update({'ensembl_sample_id' : j})
        
elif len(fetch) == 0:
    
        dict3.update({'ensembl_sample_id' : ' '})
    
    
        
print("New updated dictionary dict3:", dict3)


# # The following lines of code are just to understand that how can one split a string basis a delimiter and generate a dictionary out of it.

# In[3]:


s1 = "Name1=Value1;Name2=Value2;Name3=Value3"

dict(map(lambda x: x.split('='), s1.split(';')))


# In[5]:


mutli_attr_dictionary = "ID=gene:SNSG00000223972;Name=SSX11L1;biotype=transcribe;description=DEAD/H-box helicase 11 like 1 [Source:HGNC Symbol%3BAcc:HGNC:37102];sample_id=SNSG00000223972;logic_name=javana_hemo_saiens;version=6"

dict(map(lambda x: x.split('='), mutli_attr_dictionary.split(';')))


# In[ ]:


from nested_lookup import get_all_keys
keys = get_all_keys(dict2)
print(keys)

