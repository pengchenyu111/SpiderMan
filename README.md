# SpiderMan
爬虫项目

## 使用许可

该仓库只用于自己的学习及开发记录，**如涉及侵犯个人或团体利益，请与我联系，我将主动撤销一切相关数据，谢谢**！

该仓库中所爬取的一些数据集仅限用于学习研究目的，我不能保证数据的正确性以及任何场景的适用性。对于使用这份数据的其他用户，必须严格遵循下列条件:

1. 未经许可，用户不得将此数据集用于任何商业或收入交易用途。
2. 未经单独许可，用户不得重新转发数据。
3. 用户在使用数据集时，必须声明数据来源。

在任何情况下，我均不对因使用这些数据而造成的任何损失承担责任（包括但不限于数据丢失或数据不准确）。

**如果您有任何其他问题或意见，请发送电子邮件至: iampengchenyu@163.com**



## MovieSpider

豆瓣电影爬虫

### 技术框架

开发语言：Python	学习地址：https://www.runoob.com/python3/python3-list.html

爬虫框架：Scrapy	官方文档：https://docs.scrapy.org/en/latest/

数据存储：MySQL

### 爬取内容

#### 电影详细表

- *douban_id ：豆瓣id*
- *title ：电影名*
- *brief_instruction：电影简介*
- *directors：导演，列表*
- *screenwriters ：编剧，列表*
- *casts：演员，列表*
- *types ：类型，列表*
- *production_country_area ：制片国家/地区*
- *language ：语言*
- *publish_date：上映日期，列表*
- *runtime ：片长*
- *rating_score：评分分数，10分制*
- *rating_star ：评分星级，5星制*
- *rating_num ：评分人数*
- *rating_5_star_weight ：评5星占比*
- *rating_4_star_weight：评4星占比*
- *rating_3_star_weight ：评3星占比*
- *rating_2_star_weight ：评2星占比*
- *rating_1_star_weight ：评1星占比*
- *better_than：好于其他类型影片占比，列表*
- *douban_url ：豆瓣电影链接*
- *cover_url ：电影海报链接*
- *imdb_url ：IMDb链接*

# 作者注

若需学习完整的爬虫技术栈，请移步：

https://github.com/pengchenyu111/SpiderLearning

若需学习部署自动化爬虫，请移步：

https://blog.csdn.net/qq_43284141/article/details/116270502