from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


class UserRegistrationView(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _("Ro'yxatdan o'tish")

    def get(self, request):
        return render(request, 'layouts/form.html', {
            'form': RegistrationForm()
        })

    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            messages.success(request, _("Siz muvaffaqiyatli ro'yxatdan o'tdingiz."))
            return redirect('main:home')

        return render(request, 'layouts/form.html', {
            'form': form
        })


class UserLoginView(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _("Tizimga kirish")

    def get(self, request):
        return render(request, 'layouts/form.html', {
            'form': LoginForm
        })

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)

                messages.success(request, _("Xush kelibsiz, {}!").format(user.username))
                return redirect('main:home')

        return render(request, 'layouts/form.html', {
            'form': form
        })


@login_required
def user_logout(request):
    messages.success(request, _("Xayr, {}!").format(request.user.username))
    logout(request)
    return redirect('main:home')
