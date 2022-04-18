import pathlib


class Config(object):
    """Flask config class."""
    SECRET_KEY = "xoY23504XqLK35MzQMd1Bw"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    database_file = pathlib.Path(__file__).parent.parent.joinpath("data", 'example.sqlite')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(database_file)


class TestingConfig(Config):
    pass
