bind = "0.0.0.0:5000"
worker_class = "socketio.sgunicorn.GeventSocketIOWorker"
loglevel = "debug"
accesslog = "-"
errorlog = "-"
enable_stdio_inheritance = True
