import sociallimits


def test_platform_init():
    kwargs = {
        'caption_limit': 1,
        'tag_limit': 1,
    }
    platform = sociallimits.SocialPlatform(**kwargs)
    for (name, value) in kwargs.items():
        assert getattr(platform, name) == value


def test_all_limits_locals():
    for (name, platform) in sociallimits.all_platforms.items():
        assert getattr(sociallimits, name) == platform
