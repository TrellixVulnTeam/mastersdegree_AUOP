import mysql.connector
from preprocessor import Preprocessor


class DBHandler:
    def __init__(self, host='localhost', user='root', passwd='111111', database='ytcrawl0'):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database
        )
        self.mycursor = self.conn.cursor()
        self.preprocessor = Preprocessor()
    
    def close(self):
        self.conn.close()

    def insert(self, table_name, items, custom_fields={}):
        # Preprocess items
        items = self.preprocessor.preprocess(items)
        print('Preprocessed:', items)

        # Get columns, values
        columns, values = self.get_columns_values(items, custom_fields)

        # Wrap columns
        columns = self.preprocessor.wrap_columns(columns)

        print('\ncolumns:', columns, '#:', len(columns))
        print('\nvalues:', values, '#:', len(values))
        
        val = tuple(values)
        sql = 'INSERT INTO %s '%(table_name) + \
            '(' + ', '.join(columns) + ')' + ' VALUES ' + \
              '(' + ', '.join(['%s']*len(values)) + ');'
        
        self.mycursor.execute(sql, val)
        self.conn.commit()
    
    def get_columns_values(self, iterable, custom_fields):
        (columns, values) = self.get_columns_values_recursive(iterable)
        for column in custom_fields:
            columns += [column]
            values += [custom_fields[column]]
        return (columns, values)

    def get_columns_values_recursive(self, iterable):
        columns = list()
        values = list()
        if type(iterable) == dict:
            for key in iterable:
                if type(iterable[key]) in (dict, list):
                    recur = self.get_columns_values_recursive(iterable[key])
                    # print('\n\tAdding column:', recur[0])
                    # print('\n\tAdding value:', recur[1])
                    columns += recur[0]
                    values += recur[1]
                else:
                    # print('\n\tAdding column:', key)
                    # print('\n\tAdding value:', iterable[key])
                    columns += [key]
                    values += [iterable[key]]
        elif type(iterable) == list:
            for val in iterable:
                if type(val) in (dict, list):
                    recur = self.get_columns_values_recursive(val)
                    # print('\n\tAdding column:', recur[0])
                    # print('\n\tAdding value:', recur[1])
                    columns += recur[0]
                    values += recur[1]
                else:
                    print('List:', iterable, '\tValue:', val)
                    raise TypeError('Cannot get column from non-iterative value in list.')
        else:
            raise TypeError('Iterable expected.')
        return (columns, values)
        