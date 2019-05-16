from django.contrib import admin
from .models import game
from .models import result
from .models import before
from .models import player

admin.site.register(game)
admin.site.register(result)
admin.site.register(before)
admin.site.register(player)