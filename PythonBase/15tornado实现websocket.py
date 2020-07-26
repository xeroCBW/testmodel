from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler
import tornado.ioloop
import datetime
import tornado.websocket



class ChatHandler(tornado.websocket.WebSocketHandler):

    users =  set()

    def open(self, *args: str, **kwargs: str):

        # 进来的时候添加自己
        self.users.add(self)

        for x in self.users:
            x.write_message('[%s] - [%s]进入聊天室' %(self.request.remote_ip,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


    def on_message(self, message):

        for x in self.users:
            x.write_message('[%s] - [%s]说:%s' %(self.request.remote_ip,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),message))


    def close(self, code: int = None, reason: str = None):
        self.users.remove(self)
        for x in self.users:
            x.write_message('[%s] - [%s]离开聊天室' %(self.request.remote_ip,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


    def check_origin(self, origin: str):
        return  True

class IndexHandler(RequestHandler):

    def get(self):
        self.render('websocket.html')

if __name__ == '__main__':

    app = tornado.web.Application(

        [
            (r'/', IndexHandler),
            (r'/chat', ChatHandler),

        ],
        debug = True
    )

    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()

