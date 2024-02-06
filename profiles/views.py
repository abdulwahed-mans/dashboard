from django.urls import reverse_lazy
from django.views import generic
from .models import Profile  # تأكد من أن هذا المسار يتوافق مع مكان تواجد نموذج Profile في تطبيقك
from .forms import ProfileForm  # تأكد من أن لديك نموذج ProfileForm محدد في ملف forms.py داخل التطبيق

class ProfileListView(generic.ListView):
    model = Profile
    # لا حاجة لتعريف form_class في ListView إذ لا يتم استخدام نماذج الإدخال في عرض القائمة

class ProfileCreateView(generic.CreateView):
    model = Profile
    form_class = ProfileForm
    # success_url اختياري هنا، Django سيستخدم get_absolute_url من نموذج Profile إذا تم تعريفه

class ProfileDetailView(generic.DetailView):
    model = Profile
    # لا حاجة لتعريف form_class في DetailView حيث يتم فقط عرض التفاصيل

class ProfileUpdateView(generic.UpdateView):
    model = Profile
    form_class = ProfileForm
    # pk_url_kwarg هو "pk" بشكل افتراضي، لذا لا حاجة لتعريفه ما لم يكن مختلفًا

class ProfileDeleteView(generic.DeleteView):
    model = Profile
    success_url = reverse_lazy("profiles:profile_list")  # تأكد من أن 'profiles:profile_list' يتطابق مع اسم URL الصحيح في ملف urls.py الخاص بتطبيقك
