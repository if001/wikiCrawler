class InfoBox():
    def __init__(self):
        self.title = ""
        self.genre = []
        self.director = []
        self.character_design = []
        self.production_company = []
        self.broadcasts = []
        self.publisher = [] #出版社
        self.original_work = [] # 原作
        self.label = [] # ？
        self.music = [] # 音楽
        self.number_of_story = 0 # 話数

    def self_print(self):
        print(self.title)
        print(self.genre)
        print(self.director)
        print(self.character_design)
        print(self.production_company)
        print(self.broadcasts)
        print(self.publisher)
        print(self.original_work)
        print(self.label)
        print(self.music)
        print(self.number_of_story)

