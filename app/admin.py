from django.contrib import admin
from app.models import ModelTag, Model, MaterialTag, Material, Tailor, FabricTag, Fabric, Measurment, CustomUser



admin.site.register(DesignModel)
admin.site.register(ModelTag)
admin.site.register(CustomUser)
admin.site.register(Material)
admin.site.register(MaterialTag)
admin.site.register(Tailor)
admin.site.register(Fabric)
admin.site.register(Measurment)
admin.site.register(FabricTag)

