__version__ = "1.0.0"


class SocialPlatform:
    def __init__(self, caption_limit=None, tag_limit=None):
        self.caption_limit = caption_limit
        self.tag_limit = tag_limit


all_platforms = {
    "FACEBOOK": SocialPlatform(caption_limit=2200),
    "INSTAGRAM": SocialPlatform(caption_limit=2200, tag_limit=30),
    "PINTEREST": SocialPlatform(caption_limit=2200, tag_limit=20),
    "TUMBLR": SocialPlatform(caption_limit=2200, tag_limit=20),
    "TWITTER": SocialPlatform(caption_limit=280),
}

for name, platform in all_platforms.items():
    locals()[name] = platform
