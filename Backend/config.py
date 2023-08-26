
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
