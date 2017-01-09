class Handler():
    def __init__(self):
        self.services = {}  # format is {path: callable}

    def register(self, app):
        for path, func in self.services.iteritems():
            if func.__code__.co_argcount == 1:
                app.route(path)(func)

    @staticmethod
    def package_response(response):
        return str(response)
