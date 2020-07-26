import json
import tornado.web
import tornado.ioloop



class basicRequestHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('hello')





if __name__ == '__main__':



    app = tornado.web.Application(
        [
            (r'/',basicRequestHandler),
            (r'/blog', basicRequestHandler),
            (r'/isEven', basicRequestHandler),
            (r'/tweet/([0-9]+)', basicRequestHandler),

        ]
    )

    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()