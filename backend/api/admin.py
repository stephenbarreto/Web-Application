from django.apps import apps
from django.contrib import admin
from django.db.models import Model


app = apps.get_app_config('api')
models = app.get_models()

for model in models:
    admin.site.register(model)
