from pymongo import MongoClient
import bcrypt


class Posts:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.users
        self.Posts = self.db.posts

    def insert_post(self, data):
        inserted = self.Posts.insert({"username":data.username, "content" : data.content})
        return True