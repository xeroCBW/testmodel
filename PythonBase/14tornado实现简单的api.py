import json
import tornado.web
import tornado.ioloop



class basicRequestHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html')


class queryStringRequestHandler(tornado.web.RequestHandler):
    def get(self):
        n = int(self.get_argument('n'))
        res = 'odd' if n % 2 else 'even'
        self.write('this number %d is %s' %(n,res))




if __name__ == '__main__':



    app = tornado.web.Application(
        [
            (r'/',basicRequestHandler),
            (r'/blog', basicRequestHandler),
            (r'/isEven', queryStringRequestHandler),
            (r'/tweet/([0-9]+)', basicRequestHandler),

        ]
    )

    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()