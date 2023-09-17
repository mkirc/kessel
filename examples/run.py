import argparse
import gunicorn.app.base
from app import app

class HttpServer(gunicorn.app.base.BaseApplication):
   def __init__(self, app, options=None):
       self.options = options or {}
       self.application = app
       super().__init__()

   def load_config(self):
       for key, value in self.options.items():
           if key in self.cfg.settings and value is not None:
               self.cfg.set(key.lower(), value)

   def load(self):
       return self.application


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--num-workers', type=int, default=1)
    parser.add_argument('--port', type=str, default='8080')
    args = parser.parse_args()
    options = {
        'bind': '%s:%s' % ('0.0.0.0', args.port),
        # 'worker_class' : 'gthread',
        'logger_class' : 'kessel.logger.GunicornLogger',
        'workers': args.num_workers,
        'accesslog' : '-',
        'print_config': True,
    }
    HttpServer(app, options).run()


