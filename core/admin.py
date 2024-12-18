from django.contrib import admin

class BaseAdmin(admin.ModelAdmin):
    exclude = ('created_by', 'updated_by')

    def save_model(self, request, obj, form, change):
        """
        Kaydetmeden önce `created_by` ve `updated_by` alanlarını otomatik doldur.
        """
        if obj._state.adding:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

