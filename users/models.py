# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 添加昵称属性
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    # 根据你的需求可以自己进一步拓展，例如增加用户头像、个性签名等等，添加多少属性字段没有任何限制。
    nickname = models.CharField(max_length=50, blank=True)

    # 头像，有默认头像

    # 同时，我们继承了 AbstractUser 的内部类属性 Meta ，不过目前什么也没做。
    # 在这里继承 Meta 的原因是在你的项目中可能需要设置一些 Meta 类的属性值，不要忘记继承 AbstractUser.Meta 中已有的属性。

    # 注意：一定要继承 AbstractUser，而不是继承 auth.User。尽管 auth.User 继承自 AbstractUser 且并没有对其进行任何额外拓展，
    # 但 AbstractUser 是一个抽象类，而 auth.User 不是。如果你继承了 auth.User 类，这会变成多表继承，
    # 在目前的情况下这种继承方式是不被推荐的。

    # 此外，AbstractUser 类又继承自 AbstractBaseUser，前者在后者的基础上拓展了一套用户权限（Permission）系统。
    # 因此如非特殊需要，尽量不要从 AbstractBaseUser 拓展，否则你需要做更多的额外工作。
    class Meta(AbstractUser.Meta):
        pass

# 为了让 Django 用户认证系统使用我们自定义的用户模型，必须在 settings.py 里通过 AUTH_USER_MODEL 指定自定义用户模型所在的位置，即需要如下设置：

# settings.py
# 其它设置...
# AUTH_USER_MODEL = 'users.User'
# 即告诉 Django，使用 users 应用下的 User 用户模型。

# 设置好自定义用户模型后，生成数据库迁移文件，并且迁移数据库以生成各个应用必要的数据库表。即运行如下两条命令：
# python manage.py makemigrations
# python manage.py migrate
