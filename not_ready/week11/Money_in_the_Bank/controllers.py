from models import Clients, LoginAttempts
from helpers import hash_password
from validation import get_validator, StrongPasswordException

from sqlalchemy import desc

import datetime
import time


class ClientAlreadyRegistered(Exception):
    pass


class UserBlockedException(Exception):
    pass


class UserNotInDataBase(Exception):
    pass


class MainController:

    def __init__(self, session):
        self.session = session

    def __commit(self):
        self.session.commit()

    def __commit_object(self, obj):
        self.session.add(obj)
        self.__commit()

    def __commit_objects(self, objects):
        self.session.add_all(objects)
        self.__commit()

    def get_id_by_username(self, username):
        result = self.session.query(Clients.id).\
                  filter(Clients.username == username).one()

        if result is None:
            return None

        return result[0]

    def register(self, user, password):
        validator = get_validator(user)

        if not validator.is_valid(password):
            raise StrongPasswordException("Your password is not strong enough")

        hashed_password, salt = hash_password(password)

        current_user = self.session.query(Clients.username).\
                        filter(Clients.username == user).first()

        if current_user is not None:
            raise ClientAlreadyRegistered('Client already registered')

        client = Clients(username=user, password=hashed_password, salt=salt)
        self.__commit_object(client)

    def block_if_necessary(self, user_id):
        query = self.session.query(LoginAttempts.attempt_status).\
                 filter(LoginAttempts.client_id == user_id).first()
        # query = """SELECT attempt_status
        #            FROM login_attempts
        #            WHERE client_id = ?
        #            ORDER BY id DESC
        #            LIMIT ?"""
        # cursor.execute(query, (user_id, BLOCK_AFTER_N_ATTEMPTS))
        # result = cursor.fetchall()

        print(query)
    #     if len(result) < BLOCK_AFTER_N_ATTEMPTS:
    #         return

    #     should_block = all([r['attempt_status'] == 'FAILED' for r in result])

    #     if not should_block:
    #         return

    #     create_login_attempt(user_id, status='BLOCKED')
    #     block_start = datetime.datetime.now()
    #     block_end = block_start + datetime.timedelta(seconds=BLOCKING_TIME)
    #     insert_sql = """INSERT INTO blocked_users(client_id,
    #                                               block_start,
    #                                               block_end)
    #                     VALUES(?, ?, ?)"""

    #     cursor.execute(insert_sql, (user_id, block_start, block_end))
    #     conn.commit()


    # def is_blocked(user_id):
    #     query = """SELECT block_end
    #                FROM blocked_users
    #                WHERE client_id = ?
    #                ORDER BY id DESC
    #                LIMIT 1"""
    #     cursor.execute(query, (user_id, ))

    #     r = cursor.fetchone()

    #     if r is None:
    #         return False

    #     now = datetime.datetime.now()
    #     return r['block_end'] > adapt_datetime(now)

    def create_login_attempt(self, user_id, status):
        now = datetime.datetime.now()
        insert_sql = self.session.add(LoginAttempts(client_id=user_id,
                     attempt_status=status,
                     timestamp=now))
        self.session.commit()

    def is_blocked(self, user_id):
        temp = self.block_if_necessary(user_id)
        # block_query = self.session.query(LoginAttempts.attempt_status).\
        #                filter(client_id=user_id, attempt_status==).\
        #                order_by(LoginAttempts.id.desc()).\
        #                first()

        # if block_query == ""
        #     raise UserBlockedException("Blokiran!")

    def is_user_in_db(self, user_id):
        query = self.session.query(Clients.id).\
                 filter(Clients.id == user_id)

        # print(query)

        if query is None:
            return True

        return False

    def login(self, user, password):
        user_id = self.get_id_by_username(user)

        if self.is_user_in_db(user_id):
            raise UserNotInDataBase("This user is not registration!")

        current_user = self._login(user_id, user, password)
        # print(current_user)

        if current_user:
            self.create_login_attempt(user_id, status="SUCCESS")
            return user
        if self.is_blocked(user_id):
            raise UserBlockedException("Blokiran!")

    #     # if user:
    #     #     create_login_attempt(user.get_id(), status="SUCCESS")
    #     #     return user

    #     # create_login_attempt(user_id, status="FAILED")
    #     # block_if_necessary(user_id)


    def _login(self, user_id, user, pwd):
        user_salt = self.session.query(Clients.salt).\
                filter(Clients.id == user_id,
                       Clients.username == userII
                first()

        print(user_salt)

        if user_salt is None:
            return False

        pwd_hash, _ = hash_password(pwd, salt=user_salt)

        select_query = self.session.query(Clients).\
                        filter(Clients.username == user, Clients.password == pwd_hash).\
                        all()
        # print(select_query)
        # oshte neshto
