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
        cur.execute(f"""
            create table if not exists {_Address.table_name}(
                {_Address.id} integer primary key autoincrement,
                {_Address.street} not null,
                {_Address.city} not null,
                {_Address.state} not null,
                {_Address.zip} not null
            )
            """)
        cur.execute(f"""
            create table if not exists {_Manager.table_name}(
                {_Manager.id} integer primary key autoincrement,
                {_Manager.name} not null,
                {_Manager.pw_hash} not null
            )
            """)
        cur.execute(f"""
            create table if not exists {_Provider.table_name}(
                {_Provider.id} integer primary key autoincrement,
                {_Provider.name} not null,
                {_Provider.pw_hash} not null,
                {_Provider.address_id} integer not null,
                {_Provider.email} not null,
                {_Provider.status} not null,
                foreign key({_Provider.address_id}) references {_Address.table_name}({_Address.id})
            )
            """)
        cur.execute(f"""
            create table if not exists {_Member.table_name}(
                {_Member.id} integer primary key autoincrement,
                {_Member.name} not null,
                {_Member.address_id} integer not null,
                {_Member.status} not null,
                foreign key({_Member.address_id}) references {_Address.table_name}({_Address.id})
            )
            """)
        cur.execute(f"""
            create table if not exists {_Service.table_name}(
                {_Service.id} integer primary key autoincrement,
                {_Service.name} not null,
                {_Service.fee} not null
            )
            """)

########## create database records

    def create_address(self, street: str, city: str, state: str, zip: str) -> int:
        data = {
            "street": street,
            "city": city,
            "state": state,
            "zip": zip
        }
        print(data)
        cur = self._con.cursor()
        cur.execute(f"""insert into {_Address.table_name}(
            {_Address.street}, {_Address.city}, {_Address.state}, {_Address.zip}
            ) values(:street, :city, :state, :zip)""", data)
        self._con.commit()
        print(cur.lastrowid)
        return cur.lastrowid

    def create_manager(self, name: str, pw_hash: str) -> int:
        data = {
            "name": name,
            "hash": pw_hash
        }
        cur = self._con.cursor()
        cur.execute(f"""insert into {_Manager.table_name}(
            {_Manager.name}, {_Manager.pw_hash}
            ) values(:name, :hash)""", data)
        self._con.commit()
        return cur.lastrowid

    def create_provider(self, name: str, pw_hash: str, address_id: int, email: str, status: str) -> int:
        data = {
            "name": name,
            "hash": pw_hash,
            "addr": address_id,
            "email": email,
            "status": status
        }
        cur = self._con.cursor()
        cur.execute(f"""insert into {_Provider.table_name}(
            {_Provider.name}, {_Provider.pw_hash}, {_Provider.address_id}, {_Provider.email}, {_Provider.status}
            ) values(:name, :hash, :addr, :email, :status)""", data)
        self._con.commit()
        return cur.lastrowid

    def create_member(self, name: str, address_id: int, status: str) -> int:
        data = {
            "name": name,
            "addr": address_id,
            "status": status
        }
        print(data)
        cur = self._con.cursor()
        cur.execute(f"""insert into {_Member.table_name}(
            {_Member.name}, {_Member.address_id}, {_Member.status}
            ) values(:name, :addr, :status)""", data)
        self._con.commit()
        print(cur.lastrowid)
        return cur.lastrowid

    def create_service(self, name: str, fee: str) -> int:
        data = {
            "name": name,
            "fee": fee
        }
        cur = self._con.cursor()
        cur.execute(f"""insert into {_Service.table_name}(
            {_Service.name}, {_Service.fee}
            ) values(:name, :fee)""", data)
        self._con.commit()
        return cur.lastrowid

########## retrieve database records

    def get_manager_password_hash(self, id: int) -> str:
        #TODO
        return None

    def get_provider_password_hash(self, id: int) -> str:
        #TODO
        return None

########## database schema

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
    pw_hash = "pw_hash"
    address_id = "address_id"
    email = "email"
    status = "status"

class _Member:
    table_name = "Member"
    id = "id"
    name = "name"
    address_id = "address_id"
    status = "status"

class _Service:
    table_name = "Service"
    id = "id"
    name = "name"
    fee = "fee"
