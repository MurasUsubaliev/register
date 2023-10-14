from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django import forms
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

from .models import Region

User = get_user_model()

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

class CustomUserCreationForm(UserCreationForm):
    region = forms.ModelChoiceField(queryset=Region.objects.all())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('region',)


class CustomUserEditForm(UserChangeForm):
    region = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        empty_label=None,
        label="Region"
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'region')

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class EditProfile(View):
    template_name = 'edit_profile.html'

    def get(self, request):
        user_edit_form = CustomUserEditForm(instance=request.user)
        password_change_form = CustomPasswordChangeForm(user=request.user)

        return render(request, self.template_name, {'user_edit_form': user_edit_form, 'password_change_form': password_change_form})

    def post(self, request):
        user_edit_form = CustomUserEditForm(request.POST, instance=request.user)
        password_change_form = CustomPasswordChangeForm(user=request.user)

        if 'user_edit_submit' in request.POST:
            if user_edit_form.is_valid():
                user_edit_form.save()
                return redirect('edit_profile')
        elif 'password_change_submit' in request.POST:
            if password_change_form.is_valid():
                password_change_form.save()
                return redirect('edit_profile')

        return render(request, self.template_name, {'user_edit_form': user_edit_form, 'password_change_form': password_change_form})