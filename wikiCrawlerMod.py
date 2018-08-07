from htmlBodyGetter import HtmlBodyGetter
import urllib
import re


def crawler(title, box_type):
    parsed_title = urllib.parse.quote_plus(title)
    url = 'http://ja.wikipedia.org/w/api.php' + \
          '?format=xml' + \
          '&action=query' + \
          '&prop=revisions' + \
          '&titles=' + parsed_title + \
          '&rvprop=content'
    r = HtmlBodyGetter.get_html_body(url)
    info_box = box_type(r)


def main():
    # from common.htmlFilter import HtmlFilter
    # line = "|タイトル= はたらく細胞"
    # a = HtmlFilter.any_or_filter([
    #     HtmlFilter.bracket_filter,
    #     HtmlFilter.single_equal_filter,
    #     HtmlFilter.equal_space_filter
    # ], line)
    # print(a)
    # exit(0)
    # title = "魔法少女まどか☆マギカ"
    # title = "はたらく細胞"
    # crawler(title, HtmlBodyGetter.get_infobox)

    title = "深夜アニメ一覧"
    crawler(title, HtmlBodyGetter.get_anime_list)


if __name__ == '__main__':
    main()
