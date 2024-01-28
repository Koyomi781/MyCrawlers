from selenium import webdriver
from selenium.webdriver.common.by import By
import pymysql
import time

def get_data():
    time.sleep(2)
    # 获取每个元素 就是tbody 里面的所有tr标签
    items = driver.find_elements(By.CSS_SELECTOR, 'tbody > tr')
    # 定义返回的datas列表
    datas = []

    # 遍历每个元素tr
    for item in items:
        # 在tr里定位标题所在的td 在td.name > a
        title = item.find_element(By.CSS_SELECTOR, 'td.name > a').text
        # 下面是获取作者
        authors = ''
        # 因为每个作者不在一起，分别在td标签下的a标签里， 所以遍历td.author标签下所有的a标签然后加到一起
        try:
            for author in item.find_elements(By.CSS_SELECTOR, 'td.author > a'):
                a = author.text + ' '
                authors += a
        except Exception as e:
            authors = ''
        # 以下同标题的获取
        name = driver.find_element(By.CSS_SELECTOR, 'td.source > a').text
        date = driver.find_element(By.CSS_SELECTOR, ' td.date').text
        # 这是一条数据
        data = (title, authors, name, date)
        # 将这一条数据加到datas里面
        datas.append(data)

    # 完成这一页的爬取，点击下一页
    driver.find_element(By.CSS_SELECTOR, '#PageNext').click()

    return datas


def save_to_mysql(datas):
    # 创建连接数据库
    con = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='mydb', port=3306)

    # 创建游标对象
    cur = con.cursor()

    # 编写sql语句
    sql = """
        insert into t_student(name,age,score) values(%s,%s,%s)
    """

    # 执行sql
    try:
        cur.executemany(sql, datas)
        # 提交事务
        con.commit()
        print('插入成功')
    except Exception as e:
        print(e)
        con.rollback()
        print('插入失败')
    finally:
        con.close()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    theme = '人工智能'
    driver.get('https://kns.cnki.net/KNS8/AdvSearch?dbcode=CJFQ')
    # 输入关键词
    driver.find_element(By.CSS_SELECTOR, '#gradetxt > dd:nth-child(2) > div.input-box > input[type=text]').send_keys(theme)
    # 点击检索
    driver.find_element(By.CSS_SELECTOR, 'div.search-buttons > input').click()

    page = 5
    # 执行获取数据函数
    for i in range(page):
        datas = get_data()
        print(datas)
        # 执行保存数据库函数,将一页的数据保存到数据库
        save_to_mysql(datas)

    # 执行完成关闭浏览器
    driver.close()












