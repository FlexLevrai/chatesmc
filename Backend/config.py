
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
