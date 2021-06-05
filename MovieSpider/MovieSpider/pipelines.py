# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from MovieSpider.items import MovieDetail

class MoviespiderPipeline:

    # 开启爬虫前，开启MySQL数据库连接
    def open_spider(self, spider):
        self.connection = pymysql.connect(
            host=spider.settings['MYSQL_HOST'],
            user=spider.settings['MYSQL_USERNAME'],
            password=spider.settings['MYSQL_PASSWORD'],
            db=spider.settings['MYSQL_DB'],
            charset=spider.settings['MYSQL_DB_CHARSET']
        )
        self.cursor = self.connection.cursor()

    # 爬虫关闭后及时关闭数据库连接
    def close_spider(self, spider):
        self.connection.close()

    # 存储数据
    def process_item(self, item, spider):
        if isinstance(item, MovieDetail):
            self.save_movie_detail(item)
        return item

    # 保存电影详细信息进入数据库
    def save_movie_detail(self, item):
        keys = item.keys()
        values = tuple(item.values())
        fields = ','.join(keys)
        temp = ','.join(['%s'] * len(keys))
        sql = 'INSERT INTO movie_detail (%s) VALUES (%s)' % (fields, temp)
        self.cursor.execute(sql, tuple(i for i in values))
        return self.connection.commit()
