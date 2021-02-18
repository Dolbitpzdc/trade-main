from django.contrib import admin
from accounts import models


# class CommentInline(admin.TabularInline):
#     pass


class ComplaintAdmin(admin.ModelAdmin):
    pass


class PaymentDetailsAdmin(admin.ModelAdmin):
    pass


class MessageToUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Complaint, ComplaintAdmin)
admin.site.register(models.Payment_detail, PaymentDetailsAdmin)
admin.site.register(models.Message_to_user, MessageToUserAdmin)
