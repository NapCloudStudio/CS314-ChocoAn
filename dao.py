import sqlite3

# data access object - singleton class containing all database queries
# from dao import DAO
class DAO:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DAO, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self._con = sqlite3.connect("ChocAn.db")

    def create_tables(self):
        cur = self._con.cursor()
        cur.execute(f"create table {_Address.table_name}({_Address.id} integer primary key, {_Address.street}, {_Address.city}, {_Address.state}, {_Address.zip})")
        cur.execute(f"create table {_Manager.table_name}({_Manager.id} integer primary key, {_Manager.name}, {_Manager.pw_hash})")
        cur.execute(f"create table {_Provider.table_name}({_Provider.id} integer primary key, {_Provider.name}, {_Provider.address_id}, {_Provider.email}, {_Provider.status}, {_Provider.pw_hash})")
        cur.execute(f"create table {_Member.table_name}({_Member.id} integer primary key, {_Member.name}, {_Member.address_id}, {_Member.email}, {_Member.status})")
        cur.execute(f"create table {_Service.table_name}({_Service.id} integer primary key, {_Service.name}, {_Service.fee})")

    def get_manager_password_hash(self, id: int) -> str:
        #TODO
        return None

    def get_provider_password_hash(self, id: int) -> str:
        #TODO
        return None

# database schema

class _Address:
    table_name = "Address"
    id = "id"
    street = "street"
    city = "city"
    state = "state"
    zip = "zip"

class _Manager:
    table_name = "Manager"
    id = "id"
    name = "name"
    pw_hash = "pw_hash"

class _Provider:
    table_name = "Provider"
    id = "id"
    name = "name"
    address_id = "address_id"
    email = "email"
    status = "status"
    pw_hash = "pw_hash"

class _Member:
    table_name = "Member"
    id = "id"
    name = "name"
    address_id = "address_id"
    email = "email"
    status = "status"

class _Service:
    table_name = "Service"
    id = "id"
    name = "name"
    fee = "fee"
