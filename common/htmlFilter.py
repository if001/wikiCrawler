import re

class HtmlFilter():
    @classmethod
    def __filter(cls, pattern, line):
        """
        filterに共通の処理があればここでかく
        """
        result = re.findall(pattern, line)
        return result

    @classmethod
    def bracket_filter(cls, line):
        return HtmlFilter.__filter('\[+(.*?.)\]+', line)

    @classmethod
    def double_bracket_filter(cls, line):
        return HtmlFilter.__filter('\[[+(.*?.)\]]+', line)

    @classmethod
    def paren_filter(cls, line):
        return HtmlFilter.__filter('\(+(.*?.)\)+', line)

    @classmethod
    def last_parent_filter(cls, line):
        result = HtmlFilter.paren_filter(line)
        if len(result) == 0:
            return []
        else:
            return [result[-1]]

    @classmethod
    def single_equal_or_bracket_filter(cls, line):
        result = HtmlFilter.bracket_filter(line)
        if len(result) == 0:
            return HtmlFilter.equal_filter(line)
        else:
            return result

    @classmethod
    def single_equal_filter(cls, line):
        return HtmlFilter.__filter('\= (.*)', line)

    @classmethod
    def equal_filter(cls, line):
        return HtmlFilter.__filter('\=== +(.*?.)\ ===+', line)

    @classmethod
    def colon_filter(cls, line):
        return HtmlFilter.__filter('\; +(.*?.)+', line)

    @classmethod
    def include_year_four_seasons(cls, line):
        result = False
        for year in range(2000, 2018 + 1):
            if ((str(year) + "春" in line) \
                or (str(year) + "夏" in line) \
                or (str(year) + "秋" in line) \
                or (str(year) + "冬" in line)):
                result = True
        return result

    @classmethod
    def remove_new_line(cls, line):
        while("\n" in line): line = line.replace("\n","")
        return line

    @classmethod
    def is_anime_title(cls, line):
        return line.startswith(":* ")
