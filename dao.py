from typing import Self
import os
import sqlite3
from data_classes import *
import util

# data access object - singleton class containing all database queries
# from dao import DAO
class DAO:
    _CHOCAN_DB_PATH = "ChocAn.db"

    def chocan() -> Self:
        is_creating = not os.path.exists(DAO._CHOCAN_DB_PATH)
        dao = DAO(DAO._CHOCAN_DB_PATH)
        if is_creating:
            dao.create_tables()
            dao.create_manager("admin", "admin") # FIXME
        return dao


    def __init__(self, path: str):
        if path is None:
            raise Exception("no path specified")
        self._con = sqlite3.connect(path)

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
        cur = self._con.cursor()
        cur.execute(f"""insert into {_Address.table_name}(
            {_Address.street}, {_Address.city}, {_Address.state}, {_Address.zip}
            ) values(:street, :city, :state, :zip)""", data)
        self._con.commit()
        return cur.lastrowid

    def create_manager(self, name: str, pw: str) -> int:
        data = {
            "name": name,
            "hash": util.sha256(pw)
        }
        cur = self._con.cursor()
        cur.execute(f"""insert into {_Manager.table_name}(
            {_Manager.name}, {_Manager.pw_hash}
            ) values(:name, :hash)""", data)
        self._con.commit()
        return cur.lastrowid

    def create_provider(self, name: str, pw: str, address_id: int, email: str, status: str) -> int:
        data = {
            "name": name,
            "hash": util.sha256(pw),
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
        cur = self._con.cursor()
        cur.execute(f"""insert into {_Member.table_name}(
            {_Member.name}, {_Member.address_id}, {_Member.status}
            ) values(:name, :addr, :status)""", data)
        self._con.commit()
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

    def _get_manager_field(self, id: int, field: str) -> str:
        data = { "id": id }
        cur = self._con.cursor()
        response = cur.execute(f"""select {field} from {_Manager.table_name}
            where {_Manager.id} = :id""", data)
        result = response.fetchone()
        return None if result is None else result[0]

    def get_manager_name(self, id: int) -> str:
        return self._get_manager_field(id, _Manager.name)

    def get_manager_password_hash(self, id: int) -> str:
        return self._get_manager_field(id, _Manager.pw_hash)


    def _get_provider_field(self, id: int, field: str) -> str:
        data = { "id": id }
        cur = self._con.cursor()
        response = cur.execute(f"""select {field} from {_Provider.table_name}
            where {_Provider.id} = :id""", data)
        result = response.fetchone()
        return None if result is None else result[0]

    def get_provider_name(self, id: int) -> str:
        return self._get_provider_field(id, _Provider.name)

    def get_provider_password_hash(self, id: int) -> str:
        return self._get_provider_field(id, _Provider.pw_hash)

    def get_provider_email(self, id: int) -> str:
        return self._get_provider_field(id, _Provider.email)

    def get_provider_status(self, id: int) -> str:
        return self._get_provider_field(id, _Provider.status)


    def _get_member_field(self, id: int, field: str) -> str:
        data = { "id": id }
        cur = self._con.cursor()
        response = cur.execute(f"""select {field} from {_Member.table_name}
            where {_Member.id} = :id""", data)
        result = response.fetchone()
        return None if result is None else result[0]

    def get_member_name(self, id: int) -> str:
        return self._get_member_field(id, _Member.name)

    def get_member_status(self, id: int) -> str:
        return self._get_member_field(id, _Member.status)

########## update database records

    def _update_single(self, sql: str, data: dict) -> bool:
        rowcount = self._con.execute(sql, data).rowcount
        #assert (rowcount <= 1), f"{rowcount} rows were modified, 1 expected"
        self._con.commit()
        return (rowcount == 1)

    def update_address(self, id: int, street: str = None, city: str = None, state: str = None, zip: str = None) -> bool:
        update = ""
        if street is not None:
            update += f"{_Address.street} = :street, "
        if city is not None:
            update += f"{_Address.city} = :city, "
        if state is not None:
            update += f"{_Address.state} = :state, "
        if zip is not None:
            update += f"{_Address.zip} = :zip"
        if update == "":
            return True
        sql = f"""update {_Address.table_name}
            set {update.rstrip(", ")}
            where {_Address.id} = :id"""
        return self._update_single(sql, {
            "id": id,
            "street": street,
            "city": city,
            "state": state,
            "zip": zip
        })


    def update_provider(self, id: int, name: str = None, pw_hash: str = None, email: str = None, status: str = None) -> bool:
        update = ""
        if name is not None:
            update += f"{_Provider.name} = :name, "
        if pw_hash is not None:
            update += f"{_Provider.pw_hash} = :hash, "
        if addr_id is not None:
            update += f"{_Provider.email} = :email, "
        if status is not None:
            update += f"{_Provider.status} = :status"
        if update == "":
            return True
        sql = f"""update {_Provider.table_name}
            set {update.rstrip(", ")}
            where {_Provider.id} = :id"""

        return self._update_single(sql, {
            "id": id,
            "name": name,
            "hash": pw_hash,
            "email": email,
            "status": status,
        })

    def update_member(self, id: int, name: str = None, status: str = None) -> bool:
        update = ""
        if name is not None:
            update += f"{_Provider.name} = :name, "
        if addr_id is not None:
            update += f"{_Provider.status} = :status"
        if update == "":
            return True
        sql = f"""update {_Provider.table_name}
            set {update.rstrip(", ")}
            where {_Provider.id} = :id"""

        return self._update_single(sql, {
            "id": id,
            "name": name,
            "status": status,
        })

    def delete_provider(self, id: int) -> bool:
        sql = f"""update {_Provider.table_name}
            set {_Provider.status} = "{Provider.STATUS_INACTIVE}"
            where {_Provider.id} = :id"""
        return self._update_single(sql, { "id": id })

    def delete_member(self, id: int) -> bool:
        sql = f"""update {_Member.table_name}
            set {_Member.status} = "{Member.STATUS_INACTIVE}"
            where {_Member.id} = :id"""
        return self._update_single(sql, { "id": id })

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
