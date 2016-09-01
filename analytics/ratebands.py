import collections

class AgeRateBandDict(collections.MutableMapping,dict):
    def __getitem__(self,key):
        return dict.__getitem__(self,key)
    def __setitem__(self, key, value):
        value = int(value)
        if not 1 <= value <= 30:
            raise ValueError('{v} not in range [1,30]'.format(v=value))
        dict.__setitem__(self,key,value)
    def __delitem__(self, key):
        dict.__delitem__(self,key)
    def __iter__(self):
        return dict.__iter__(self)
    def __len__(self):
        return dict.__len__(self)
    def __contains__(self, x):
        return dict.__contains__(self,x)