import asyncio
import logging
import aiomysql
from logging import log


@asyncio.coroutine
def create_pool(loop, **kw):  # 创建连接池
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get['charset', 'utf-8'],
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )


@asyncio.coroutine
def select(sql, args, size=None):
    log(sql,args)
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?', '%s', args or ()))


# import mysql.connector
#
#
# conn = mysql.connector.connect(user='root', password='huangziwen123', database='test')
# cursor = conn.cursor()
# cursor.execute('insert into user (id,name) values (%s,%s)',[2,'黄'])
# conn.commit()
# cursor.close()