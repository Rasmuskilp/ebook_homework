import pyodbc
import requests
class MSDBConnection():
    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'ebook_db'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.docker_Northwind = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID='
            + self.username + ';PWD=' + self.password)
        self.cursor = self.docker_Northwind.cursor()
    def __sql_query(self,sql_query): # Makes it private
        return self.cursor.execute(sql_query)
    # cursor.execute("SELECT * FROM Passengers WHERE name LIKE 'Jessica'")
    def author_in(self):
        author_in = input('enter the author for the book')
        return author_in
    def title_in(self):
        title_in = input('enter the title for the book')
        return title_in
    def release_in(self):
        print('the format of the date that you need to input is YYYY-MM-DD')
        release_in = input('enter the release date for the book')
        return  release_in
    def insert_to(self):
        # val_title = self.title_in()
        # val_author = self.author_in()
        # val_release = self.release_in()
        query = f"INSERT INTO ebooks (title, author, release_date) VALUES ('{self.title_in()}','{self.author_in()}','{self.release_in()}')"
        query2 = 'SELECT * FROM ebooks'
        item = self.__sql_query(query)
        self.docker_Northwind.commit()
        item2 = self.__sql_query(query2)
        # record = item.fetchall()
        return item2.fetchall()
    def select_from(self):
        query = 'SELECT * FROM ebooks'
        item = self.__sql_query(query)
        print( item.fetchall())
    def geo_code_api_call(self):
        path_url = 'http://api.postcodes.io/postcodes/'
        arguments = 'WS29EX'
        post_codes = requests.get(path_url + arguments)
        dict_response = post_codes.json()
        return dict_response
    def get_post_code(self):
        post_code = self.geo_code_api_call()
        lat_code = self.geo_code_api_call()
        long_code =self.geo_code_api_call()
        return post_code['result']['postcode'], long_code['result']['longitude'], lat_code['result']['latitude']
    def get_long(self):
        long_code =self.geo_code_api_call()
        return long_code['result']['longitude']
    def get_lat(self):
        lat_code = self.geo_code_api_call()
        return lat_code['result']['latitude']
    def ins_long_lat(self):
        from_long= self.get_long()
        from_lat = self.get_lat()
        #query = f"ALTER TABLE ebooks add (longitude DECIMAL(11,8),latitude DECIMAL(11,8))"
        query3 = f" UPDATE ebooks SET longitude = {from_long}, latitude = {from_lat} WHERE title = '{self.title_in()}' "
        #item = self.__sql_query(query)
        item3 = self.__sql_query(query3)
        query2 = 'SELECT * FROM ebooks'
        item2 = self.__sql_query(query2)
        return item2.fetchall()
# print(MSDBConnection().ins_long_lat())
# print(MSDBConnection().get_post_code())
# posts = MSDBConnection()
# posts = MSDBConnection().geo_code_api_call()
#print(posts['result'].keys())
# def add_to(self):
    #     query = "INSERT INTO ebook (passenger) VALUES ('Jess')"
    #     item = self.__sql_query(query)
    #     query2 = "SELECT * FROM Flight_trip"
    #     item2 = self.__sql_query(query2)
    #     print(item2.fetchall())
    # build URL