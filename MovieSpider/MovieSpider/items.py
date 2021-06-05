# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# 电影详情信息
class MovieDetail(scrapy.Item):
    douban_id = scrapy.Field()  # 豆瓣id
    title = scrapy.Field()  # 电影名
    brief_instruction = scrapy.Field()  # 电影简介
    directors = scrapy.Field()  # 导演，列表
    screenwriters = scrapy.Field()  # 编剧，列表
    casts = scrapy.Field()  # 演员，列表
    types = scrapy.Field()  # 类型，列表
    production_country_area = scrapy.Field()  # 制片国家/地区
    language = scrapy.Field()  # 语言
    publish_date = scrapy.Field()  # 上映日期，列表
    runtime = scrapy.Field()  # 片长
    rating_score = scrapy.Field()  # 评分分数，10分制
    rating_star = scrapy.Field()  # 评分星级，5星制
    rating_num = scrapy.Field()  # 评分人数
    rating_5_star_weight = scrapy.Field()  # 评5星占比
    rating_4_star_weight = scrapy.Field()  # 评4星占比
    rating_3_star_weight = scrapy.Field()  # 评3星占比
    rating_2_star_weight = scrapy.Field()  # 评2星占比
    rating_1_star_weight = scrapy.Field()  # 评1星占比
    better_than = scrapy.Field()  # 好于其他类型影片占比，列表
    douban_url = scrapy.Field()  # 豆瓣电影链接
    cover_url = scrapy.Field()  # 电影海报链接
    imdb_url = scrapy.Field()  # IMDb链接
