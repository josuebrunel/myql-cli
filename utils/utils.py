from xml.etree import cElementTree as ctree
from myql.contrib.table import Table, Binder, BinderKey, BinderPage

class BinderMeta(type):
    
    BINDER_KEY = ['name', 'itemPath', 'produces', 'pollingFrequencySeconds', 'urls', 'keys', 'pages']

    def __new__(cls, name, bases, dct):
        if name != 'BinderModel':
            binder_attr = {key: value for (key, value) in dct.items() if key in cls.BINDER_KEY}
            binder_attr['inputs'] = [ value for value in dct.values() if isinstance(value, BinderKey)]
            dct = { key : value for (key, value) in dct.items() if key in ('__module__', '__metaclass__')}
            dct['binder'] = Binder(**binder_attr)
            print dct
            # Add KeyException Management
        return super(BinderMeta,cls).__new__(cls, name, (Binder,), dct)

    def toxml(cls,):
        return ctree.tostring(cls.binder.etree)

class BinderModel(Binder):
    __metaclass__ = BinderMeta


# TABLE
class TableMeta(type):

    TABLE_KEYS = ['name', 'author', 'apiKeyURL', 'documentationURL', 'sampleQuery']

    def __new__(cls, name, bases, dct):
        if name != 'TableModel':
            table_attr = {key: value for (key, value) in dct.items() if key in cls.TABLE_KEYS }
            table_attr['bindings'] = [ value.binder for value in dct.values() if hasattr(value, 'binder') and isinstance(value, BinderMeta) ]
            dct = { key : value for (key, value) in dct.items() if key in ('__module__', '__metaclass__')}
            dct['table'] = Table(**table_attr)
            print dct

        return super(TableMeta, cls).__new__(cls, name, (Table,), dct)

    def toxml(cls,):
        return ctree.tostring(cls.table.etree)

class TableModel(Table):
    __metaclass__ = TableMeta

