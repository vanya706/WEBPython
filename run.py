other_labs = __import__("other labs.app")

if __name__ == '__main__':
    other_labs.app.create_app(config_name='dev').run()
