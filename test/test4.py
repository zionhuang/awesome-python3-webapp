# # 使用元类写ORM
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):  # cls是当前准备创建的类的对象User,Model,Objecj; name是这个类的名字 User;
        #                                    bases是类继承的父类集合 dict; attrs 是类的方法集合
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v, Field):
                print('Found mappings: %s ===> %s' % (k,v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 现在猜想__mappings__是metaclass给的
        attrs['__table__'] = name  # 和__mappings__一样，都是metaclass给的
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        field = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            field.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(field), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, column_type='bigint')


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, column_type='varchar(100)')


class User(Model):
    id = IntegerField('id')
    name = StringField('name')
    email = StringField('email')
    password = StringField('password')


if __name__== '__main__':
    U = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
    U.save()

# class Field(object):
#
#     def __init__(self, name, column_type):
#         self.name = name
#         self.column_type = column_type
#
#     def __str__(self):
#         return '<%s:%s>' % (self.__class__.__name__, self.name)
#
# class StringField(Field):
#
#     def __init__(self, name):
#         super(StringField, self).__init__(name, 'varchar(100)')
#
# class IntegerField(Field):
#
#     def __init__(self, name):
#         super(IntegerField, self).__init__(name, 'bigint')
#
# class ModelMetaclass(type):
#
#     def __new__(cls, name, bases, attrs):
#         if name=='Model':
#             return type.__new__(cls, name, bases, attrs)
#         print('Found model: %s' % name)
#         mappings = dict()
#         for k, v in attrs.items():
#             if isinstance(v, Field):
#                 print('Found mapping: %s ==> %s' % (k, v))
#                 mappings[k] = v
#         for k in mappings.keys():
#             attrs.pop(k)
#         attrs['__mappings__'] = mappings # 保存属性和列的映射关系
#         attrs['__table__'] = name # 假设表名和类名一致
#         return type.__new__(cls, name, bases, attrs)
#
# class Model(dict, metaclass=ModelMetaclass):
#
#     def __init__(self, **kw):
#         super(Model, self).__init__(**kw)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Model' object has no attribute '%s'" % key)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
#     def save(self):
#         fields = []
#         params = []
#         args = []
#         for k, v in self.__mappings__.items():
#             fields.append(v.name)
#             params.append('?')
#             args.append(getattr(self, k, None))
#         sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
#         print('SQL: %s' % sql)
#         print('ARGS: %s' % str(args))
#
# # testing code:
#
# class User(Model):
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')
#
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# u.save()