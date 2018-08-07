import json


class CvSet():
    def __init__(self, title, cv_list):
        self.title = title
        self.cv_list = cv_list

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4,  ensure_ascii=False)
