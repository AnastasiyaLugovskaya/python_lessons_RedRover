import random

from faker import Faker


class BaseGenerator:
    faker = Faker("En")

    @staticmethod
    def get_id(uid=None):
        if uid is None:
            return random.randint(10000, 99999)
        return uid

    def get_name(self, name=None):
        if name is None:
            return self.faker.name()
        return name

    def create_category(self, category_value=None, uid=None, name=None):
        if category_value is None:
            category_value ={
                "id": self.get_id(uid),
                "name": self.get_name(name)
            }
            return category_value
        return category_value

    def get_photo_urls(self, photo_urls=None, url_count=1):
        lst = []
        if photo_urls is None:
            for i in range(url_count):
                photo = self.faker.image_url()
                lst.append(photo)
            return lst
        return photo_urls

    def get_tags(self, tags=None, tags_count=1, uid=None, name=None):
        lst = []
        if tags is None:
            for i in range(tags_count):
                tag = {
                    "id": self.get_id(uid),
                    "name": self.get_name(name)
                }
                lst.append(tag)
            return lst
        return tags

    @staticmethod
    def get_status(status=None):
        if status is None:
            return "available"
        return status
