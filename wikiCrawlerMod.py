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
    # title = "魔法少女まどか☆マギカ"
    # title = "はたらく細胞"
    # crawler(title, HtmlBodyGetter.get_infobox)

    title = "進撃の巨人 (アニメ)"
    title = "魔法少女まどか☆マギカ"
    title = "はたらく細胞"
    title = "ハイスコアガール"
    crawler(title, HtmlBodyGetter.get_cast)

    # title = "深夜アニメ一覧"
    # crawler(title, HtmlBodyGetter.get_anime_list)


if __name__ == '__main__':
    main()
