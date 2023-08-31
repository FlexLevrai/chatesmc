
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"
    OPENAI_KEY = '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'

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
