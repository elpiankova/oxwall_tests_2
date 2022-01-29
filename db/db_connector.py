import json

import allure
import pymysql.cursors

from value_objects.user import User


def _hash(password):
    d = {
        "pass": "592490bd0faa5a417a1aa7cf7aca26e8551a1b2d3238c618a9d17d1bfc4bbbef",
        "test": "a2b84e6c176c01e1aacd3312469e5ac732978f6534af33290882f5aa32be572c",
        "secret": "74210d690a28b4372ca86ff249c472975d860a537d19f0f551cd2c7d908222ea"
    }
    return d[password]


class DB:
    def __init__(self, host, user, password, db):
        # Connect to the database
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.connection.autocommit(True)

    def close(self):
        self.connection.close()

    def create_user(self, user):
        with self.connection.cursor() as cursor:
            sql = """INSERT INTO `ow_base_user` (`username`, `email`, `password`, `emailVerify`, `joinIp`, `accountType`) 
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (user.username, user.email, _hash(user.password), 1, "2130706433",
                                 "290365aadde35a97f11207ca7e4279cc"))
        with self.connection.cursor() as cursor:
            sql1 = f"SELECT `id` FROM ow_base_user WHERE ow_base_user.username = '{user.username}'"
            cursor.execute(sql1)
            user_id = cursor.fetchone()['id']
            sql = f"""INSERT `ow_base_question_data` (`userId`, `textValue`, `questionName`)
                      VALUES ("{user_id}", "{user.real_name}", "realname")"""
            cursor.execute(sql)
            sql = f"""INSERT `ow_base_question_data`(`userId`, `intValue`, `questionName`)
                      VALUES("{user_id}", "{user.gender}", "sex")"""
            cursor.execute(sql)
            user_birthdate = user.birthdate if user.birthdate else "1982-02-10 00:00:00"
            sql = f"""INSERT `ow_base_question_data`(`userId`, `dateValue`, `questionName`)
                      VALUES("{user_id}", "{user_birthdate}", "birthdate")"""
            cursor.execute(sql)

    def delete_user(self, user):
        with self.connection.cursor() as cursor:
            sql1 = f"SELECT * FROM ow_base_user WHERE ow_base_user.username = '{user.username}'"
            cursor.execute(sql1)
            user_id = cursor.fetchone()['id']
            sql = f"""DELETE FROM `ow_base_question_data`
                       WHERE `ow_base_question_data`.`userId` = {user_id};"""
            cursor.execute(sql)
        with self.connection.cursor() as cursor:
            sql = f'''DELETE FROM `ow_base_user`
                      WHERE `ow_base_user`.`username` = "{user.username}"'''
            cursor.execute(sql)

    def get_users(self):
        """ Get all users """
        with self.connection.cursor() as cursor:
            sql = f"SELECT `id`, `username`, `email` FROM `ow_base_user`"
            cursor.execute(sql)
            result = cursor.fetchall()
        return [User(**u) for u in result]

    @allure.step("THEN a new post appears in DB with input text")
    def get_last_text_post(self):
        """ Get post with maximum id that is last added """
        with self.connection.cursor() as cursor:
            sql = """SELECT * FROM `ow_newsfeed_action`
                     WHERE `id`= (SELECT MAX(`id`) FROM `ow_newsfeed_action` WHERE `entityType`="user-status")
                     AND `entityType`="user-status"
                  """
            cursor.execute(sql)
            response = cursor.fetchone()
            data = json.loads(response["data"])["status"]
        return data
