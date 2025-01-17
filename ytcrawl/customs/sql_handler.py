from copy import copy

class SQLHandler:
    command = None
    command_set = False
    values = None
    list_where_clauses = []
    list_order_clauses = []
    # get_where_from_list()
    dict_where_conj = {'and': ' AND ', 'or': ' OR '}
    dict_order = {'asc': 'ASC', 'desc': 'DESC'}
    # __check_type()
    dict_types = {str: 'str', int: 'int', list: 'list', tuple: 'tuple'}

    def __init__(self, verbose):
        self.verbose = verbose

    def __output(self, message):
        if self.verbose:
            print(*message)
        return self

    def set_command_set(self):
        self.command_set = True
        self.__output(('\tCommand set:', self.command))
        return self

    def select(self, table, columns='*'):
        if type(columns) in (list, tuple):
            columns = tuple(map(lambda column: '`' + column + '`', columns))
            columns = ', '.join(columns)
        self.command = "SELECT %s FROM `%s`" % (columns, table)
        self.set_command_set()
        return self

    def update(self, table, columns=None, values=None, dict_columns_values=None):
        if dict_columns_values != None:
            columns = list(dict_columns_values.keys())
            values = tuple(dict_columns_values.values())

        self.values = values

        key_val_pairs = ', '.join(tuple(map(lambda col: col + '=%s', columns)))

        self.command = "UPDATE `%s` SET %s" % (table, key_val_pairs)
        self.set_command_set()
        return self

    def insert(self, table, columns=None, values=None, dict_columns_values=None):
        if dict_columns_values != None:
            columns = list(dict_columns_values.keys())
            values = tuple(dict_columns_values.values())

        self.values = values

        # self.values = self.__preprocess_list_values(values)
        self.command = "INSERT INTO `%s` (%s) VALUES (" % (table, ', '.join(columns))\
            + ', '.join(['%s'] * len(columns))\
            + ")"
        self.set_command_set()
        return self

    def delete(self, table):
        self.command = "DELETE FROM `%s`" % table
        self.values = True
        self.set_command_set()
        return self

    def __preprocess_list_values(self, values):
        for i, val in enumerate(values):
            if type(val) == str:
                values[i] = "'%s'" % val
            elif type(val) == int:
                values[i] = str(val)
            elif val == None:
                values[i] = "NULL"
            else:
                raise TypeError(
                    'Type of value cannot be processed:', val, type(val))
        self.__output(('Preprocessed values:', values))
        return values

    def reset(self):
        self.init_command()
        self.init_list_where_clauses()
        self.init_list_order_clauses()

    def init_command(self):
        self.command = None
        self.command_set = False
        self.values = None
        return self

    def init_list_where_clauses(self, index=None):
        if index != None:
            pop = self.list_where_clauses.pop(index)
            self.__output(('\tlist_where_clauses[%d] popped:' % index, pop))
        else:
            self.list_where_clauses = []
        return self

    def init_list_order_clauses(self, index=None):
        if index != None:
            pop = self.list_order_clauses.pop(index)
            self.__output(('\tlist_order_clauses[%d] popped:' % index, pop))
        else:
            self.list_order_clauses = []
        return self

    def get_sql_vals(self, mode_where='and', reset=True):
        if not self.command_set:
            raise ValueError('Command not set.')

        # Start sql
        self.last_sql = self.command

        # WHERE
        if self.list_where_clauses:
            self.last_sql = "%s WHERE %s" % (
                self.command, self.get_where_from_list(self.list_where_clauses, mode_where))

        # ORDER BY
        if self.list_order_clauses:
            self.last_sql = "%s ORDER BY %s" % (
                self.last_sql, self.get_order_by_from_list(self.list_order_clauses))

        # End sql
        self.last_sql += ';'

        self.last_values = self.values
        self.__output(('\tsql:', self.last_sql))
        if reset:
            self.reset()
        return (self.last_sql, self.last_values)

    def where(self, column, value, mode='='):
        # Param 'mode' could be: '=', 'match'
        if mode == '=':
            if value == None:
                clause = "`%s` IS NULL" % column
            else:
                clause = "`%s`=%d" % (column, value) \
                    if type(value) != str else "`%s`='%s'" % (column, value)

        elif mode == '<>':
            if value == None:
                clause = "`%s` IS NOT NULL" % column
            else:
                clause = "`%s`<>%d" % (column, value) \
                    if type(value) != str else "`%s`<>'%s'" % (column, value)

        elif mode == '>':
            clause = "`%s`>%d" % (column, value) \
                if type(value) != str else "`%s`>'%s'" % (column, value)

        elif mode == '<':
            clause = "`%s`<%d" % (column, value) \
                if type(value) != str else "`%s`<'%s'" % (column, value)

        elif mode == 'like':
            clause = "`%s` LIKE %d" % (column, value) \
                if type(value) != str else "`%s` LIKE '%s'" % (column, value)

        elif mode == 'fulltext_list':
            value = str(value)
            # self.__check_type(value, 'str')
            list_clauses = []
            list_clauses.append(
                "match(%s) against ('\"%s,\"' in boolean mode)" % (column, value))
            list_clauses.append(
                "match(%s) against ('\" %s\"' in boolean mode)" % (column, value))
            list_clauses.append(
                "`%s`='%s'" % (column, value))
            clause = self.get_where_from_list(list_clauses, 'or')

        elif mode == 'fulltext':
            clause = "match(%s) against (\"%s\" in boolean mode)" % (
                column, value)

        elif mode in ('in', 'not in'):
            _list_vals_wrapped = list()
            for val in value:
                _list_vals_wrapped.append(str(val)) if type(
                    val) != str else _list_vals_wrapped.append('\'' + val + '\'')
            clause = "%s %s (%s)" % (column, mode.upper(), ', '.join(_list_vals_wrapped))

        else:
            raise ValueError()

        if clause not in self.list_where_clauses:
            self.list_where_clauses.append(clause)
        self.__output(('\tCurrent list_where_clauses:', self.list_where_clauses))
        return self

    def order_by(self, columns=["idx"], orders=["asc"], dict_columns_orders=None):
        if dict_columns_orders != None:
            columns = tuple(dict_columns_orders.keys())
            # self.__output(('dict_columns_orders.values(): ', dict_columns_orders.values()))
            orders = tuple(
                map(lambda order: self.dict_order[order], dict_columns_orders.values()))
            # self.__output(('orders: ', orders))

        for col, order in zip(columns, orders):
            clause = '%s %s' % (col, order)
            if clause not in self.list_order_clauses:
                self.list_order_clauses.append(clause)
        self.__output(('\tCurrent list_order_clauses:', self.list_order_clauses))
        return self

    def __check_type(self, value, type_targets='str'):
        str_value_type = self.dict_types[type(value)]
        if type(type_targets) not in (list, tuple):
            if str_value_type != type_targets:
                raise TypeError(value, ': Type %s expected, %s given.:' % (
                    type_targets, str_value_type))
        else:
            if str_value_type not in type_targets:
                raise TypeError(value, ': Type %s expected, %s given.:' % (
                    ' or '.join(type_targets), str_value_type))
        return self

    def get_where_from_list(self, list_clauses, mode='and'):
        if len(list_clauses):
            conj = self.dict_where_conj[mode]
            where = '(' + conj.join(list_clauses) + ')'
        else:
            where = '1'
        # self.__output(('\tWhere:', where))
        return where

    def get_order_by_from_list(self, list_clauses):
        # if len(list_clauses):
        # order_by = 'ORDER BY ' + ' '.join(list_clauses)
        # else:
        # order_by = ''
        return ' '.join(list_clauses)
