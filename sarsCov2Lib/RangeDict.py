import collections


class RangeDict(collections.MutableMapping):

    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        return self.store[key]
        #return self.store[self.transform_key(key)]

    def __setitem__(self, key, value):
        for i in range(key[0], key[1]+1):
            self.store[i] = [key, value]

    def __delitem__(self, key):
        # del self.store[self.transform_key(key)]
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

#    def transform_key(self, key):
#        for k in self.store.keys():
#            if k[0] <= key <= k[1]:
#                return k
#        return key
