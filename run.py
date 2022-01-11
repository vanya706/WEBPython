other_labs = __import__("other labs.app")


def create_app():
    return other_labs.app.create_app(config_name='dev')


if __name__ == '__main__':
    create_app().run()
