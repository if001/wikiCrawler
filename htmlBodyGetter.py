import requests
import re
from common.htmlFilter import HtmlFilter
from model.animeSet import AnimeSet
from model.infoBox import InfoBox
from const.infoBoxConst import InfoBoxConst

class HtmlBodyGetter():
    @classmethod
    def get_html_body(cls, url):
        r = requests.get(url)
        body = HtmlBodyGetter.__page_not_found_handler(r.text)
        body = HtmlBodyGetter.__set_one_lines_list(body)
        return body

    @classmethod
    def __page_not_found_handler(cls, text):
        body = ""
        if "missing" in text :
            print(title + " page not find")
        else:
            body = text
        return body

    @classmethod
    def __set_one_lines_list(cls, text):
        lines = []
        tmp = ""
        st = ""
        for tmp in text:
            st = st + tmp
            if tmp == "\n" :
                lines.append(st)
                st=""
        return lines

    @classmethod
    def get_infobox(cls, lines):
        flag=0
        info_box_lines = []
        for line in lines:
            if line.startswith("{{Infobox animanga/Header"):
                flag = 1
            if line.startswith("{{Infobox animanga/TVAnime"):
                flag = 1
            if flag == 1:
                info_box_lines.append(line)
            if line.startswith("}}"):
                flag=0

        infoBox = InfoBox()
        for line in info_box_lines :
            if InfoBoxConst.title in line:
                infoBox.title = HtmlFilter.single_equal_filter(line)
            elif InfoBoxConst.genre in line:
                infoBox.genre = HtmlFilter.single_equal_or_bracket_filter(line)
            elif InfoBoxConst.director in line:
                infoBox.director = HtmlFilter.single_equal_or_bracket_filter(line)
            elif InfoBoxConst.scenario in line:
                infoBox.scenario = HtmlFilter.single_equal_or_bracket_filter(line)
            elif InfoBoxConst.character_design in line:
                infoBox.character_design = HtmlFilter.single_equal_or_bracket_filter(line)
            elif InfoBoxConst.production_company in line:
                infoBox.production_company = HtmlFilter.single_equal_or_bracket_filter(line)
            elif InfoBoxConst.broadcasts in line:
                infoBox.broadcasts = HtmlFilter.single_equal_or_bracket_filter(line)
            elif InfoBoxConst.publisher in line:
                infoBox.publisher = HtmlFilter.single_equal_or_bracket_filter(line)
            elif InfoBoxConst.original_work in line:
                infoBox.original_work = HtmlFilter.paren_filter(line) # ほかの作品みて検証
            elif InfoBoxConst.label in line:
                infoBox.label = HtmlFilter.paren_filter(line)
            elif InfoBoxConst.music in line:
                infoBox.music = HtmlFilter.single_equal_or_bracket_filter(line)
            elif InfoBoxConst.number_of_story in line:
                infoBox.number_of_story = HtmlFilter.single_equal_filter(line)
            else:
                pass
        infoBox.self_print()

    @classmethod
    def get_anime_list(cls, lines):
        anime_list = []
        year_cnter = 2017
        season = ""
        stage = ""
        year = ""
        for line in lines :
            if "=== " + str(year_cnter) + "年 ===" in line :
                year_cnter += 1
                year = HtmlFilter.equal_filter(line)
            elif HtmlFilter.include_year_four_seasons(line):
                season = HtmlFilter.colon_filter(line)
            elif HtmlFilter.is_anime_title(line):
                title = HtmlFilter.bracket_filter(line)
                stage = HtmlFilter.last_parent_filter(line)
                anime_list.append(AnimeSet(title, year, season, stage))
                print("year:",year)
                print("title:",title)
                print("season:",season)
                print("stage:",stage)
                print("---")
