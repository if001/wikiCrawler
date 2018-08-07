import json


class AnimeSet():
    def __init__(self, title, year, season="", stage=""):
        self.title = title
        self.year = year
        self.season = season  # 夏アニメ、冬アニメとか
        self.stage = stage  # 1期,2期とか

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4,  ensure_ascii=False)
