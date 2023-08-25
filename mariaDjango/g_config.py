# import multiprocessing as mp
# bind = "127.0.0.1:8000"#等等試看看這個會不會讓nginx透過這個位址丟代理資料過來
bind = "0.0.0.0:8000"# 直接以gunicorn 執行deploy的動作,但這個變成在http裡要連port號一起打
# workers = mp.cpu_count() * 1 + 1
workers = 4
loglevel = 'debug'
# access_log_format = "{'request_date':%(t)s, 'remote_ip':%(h)s,'request_id':%({X-Request-Id}i)s,'response_code':%(s)s,'request_method':%(m)s,'request_path':%(U)s,'request_querystring': %(q)s}"
# accesslog = '/home/seric/DjangoProject/mariaDjango/mariaDjango/gunicorn/log/access.log'
# access_log_format = "{'remote_ip':'%(h)s', %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s %(l)s %(D)s}"
# errorlog = '/home/seric/DjangoProject/mariaDjango/mariaDjango/gunicorn/log/error.log'
