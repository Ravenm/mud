import multiprocessing

bind = "0.0.0.0:5000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "socketio.sgunicorn.GeventSocketIOWorker"
