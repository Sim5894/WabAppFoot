from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import CreateView, FormView
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm


from .forms import LoginForm, RegisterForm, GuestForm


def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email = form.cleaned_data.get("email")
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register/")
    return redirect("/register/")


class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'connexion/login.html'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email  = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        return super(LoginView, self).form_invalid(form)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'connexion/register.html'
    success_url = '/login/'


def home(request):
    return render(request, 'connexion/home.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
    else:
        u_form = UserUpdateForm(instance=request.user)

    if u_form.is_valid():
        u_form.save()
        messages.success(request, f'Ton compte a bien été modifié')
        return redirect('profile')

    context = {
        'u_form': u_form
    }
    return render(request, 'connexion/profile.html', context)

