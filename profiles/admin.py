from django.contrib import admin
from .models import Profile  # استيراد مباشر لنموذج Profile

# لا حاجة لتعريف ProfileAdminForm إذا كنت ستستخدم جميع الحقول وليس هناك تخصيصات خاصة للنموذج
# إذا كنت بحاجة إلى تخصيصات خاصة في النموذج، يمكنك إعادة إدخاله هنا

class ProfileAdmin(admin.ModelAdmin):
    # استخدام 'list_display' لتحديد الحقول التي تظهر في قائمة الإدارة
    list_display = ('postal_code', 'address', 'personal_identity_number', 'city', 'language_preference', 'phone_number', 'created', 'last_updated')
    
    # استخدام 'readonly_fields' للحقول التي لا يجب تعديلها من الإدارة
    readonly_fields = ('created', 'last_updated')  # عادةً ما يكون الوقت الذي تم فيه إنشاء السجل وآخر تحديث له فقط

    # إضافة 'search_fields' لتسهيل البحث عن ملفات التعريف
    search_fields = ('postal_code', 'address', 'personal_identity_number', 'city', 'phone_number')
    
    # إضافة 'list_filter' لتوفير فلاتر جانبية في الصفحة لتصفية السجلات بسهولة
    list_filter = ('city', 'language_preference', 'created')

    # تخصيص النموذج في صفحة التفاصيل
    fieldsets = (
        ('Basic Information', {'fields': ('user', 'personal_identity_number', 'language_preference', 'phone_number')}),
        ('Location Information', {'fields': ('postal_code', 'address', 'city')}),
        ('Media', {'fields': ('profile_picture',)}),
        ('Dates', {'fields': ('created', 'last_updated'), 'classes': ('collapse',)}),
    )

admin.site.register(Profile, ProfileAdmin)  # تسجيل Profile مع ProfileAdmin للتخصيص
