from mongokat import Collection, Document

class UserDocument(Document):
        def my_sum(self):
                return self["a"] + self["b"]

class UserCollection(Collection):
        document_class = UserDocument
        def find_by_name(self, name):
                return self.find_one({"name": name})
