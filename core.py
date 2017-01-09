class Handler():
    def __init__(self):
        self.services = {}  # format is {path: callable}

    def register(self, app):
        for path, func in self.services.iteritems():
            app.route(path)(func)
