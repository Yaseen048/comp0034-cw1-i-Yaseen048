"""Flask config class."""


class Config(object):
    SECRET_KEY = "xoY23504XqLK35MzQMd1Bw"


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    TESING = True
