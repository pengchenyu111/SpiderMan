from MovieSpider.MovieSpider.db_handler import connection, cursor

if __name__ == '__main__':
    sql = 'select douban_id from movie_detail'
    cursor.execute(sql)
    douban_id_tuple_list = cursor.fetchall()
    l = list(map(lambda x: x[0], douban_id_tuple_list))
    print(list(l))
    s = [
        {
            "episodes_info": "",
            "rate": "7.2",
            "cover_x": 491,
            "title": "弓蕉园的秘密",
            "url": "https://movie.douban.com/subject/35427435/",
            "cover": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2639379745.webp",
            "id": "35427435",
            "cover_y": 686,
        },
        {
            "episodes_info": "",
            "rate": "6.0",
            "cover_x": 1300,
            "title": "徐福",
            "url": "https://movie.douban.com/subject/26949852/",
            "cover": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2625736779.webp",
            "id": "26949852",
            "cover_y": 1856,
        }]

    s1 = list(map(lambda x: int(x['id']), s))
    print(s1)

    print(set(s1) - set(l))
    print(list(set(s1) - set(l)))