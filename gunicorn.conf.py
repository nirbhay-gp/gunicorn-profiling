import multiprocessing
import gunicorn_profiler
print(multiprocessing.cpu_count())

# Setting for DEBUG environment
reload = True

worker_class = 'gthread'
threads = 8

bind = "127.0.0.1:8000"
# workers = multiprocessing.cpu_count() * 2 + 1
workers = 3
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(a)s %(M)s'

# def pre_request(worker, req): 
#     print('profiler_activated')
#     gunicorn_profiler.pre_request(worker, req)

# def post_request(worker, req, environ, resp): 
#     gunicorn_profiler.post_request(worker, req)    
    