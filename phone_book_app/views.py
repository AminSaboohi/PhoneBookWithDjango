from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, AddProvinceForm, AddCityForm
from .models import PhoneBookRow


# Create your views here.
def user_authenticated_decorator(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            result = view_func(request, *args, **kwargs)
        else:
            messages.success(
                request,
                message="You Must Be Logged In To Do That..."
            )
            result = redirect('home')
        return result

    return wrapper


def home(request):
    phone_book_rows = PhoneBookRow.objects.all()
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, message="You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(
                request,
                message="There Was An Error Logging In, Please Try Again..."
            )
            return redirect('home')
    else:
        return render(
            request,
            template_name='home.html',
            context={'phone_book_rows': phone_book_rows}
        )


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, message="You Have Been Logged Out...")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request,
                message="You Have Successfully Registered! Welcome!"
            )
            return redirect('home')
    else:
        form = SignUpForm()
        return render(
            request,
            template_name='register.html',
            context={'form': form}
        )

    return render(
        request,
        template_name='register.html',
        context={'form': form}
    )


@user_authenticated_decorator
def phone_book_record(request, pk):
    # Look Up Row Datas
    record = PhoneBookRow.objects.get(id=pk)
    return render(
        request,
        template_name='record.html',
        context={'phone_book_record': record}
    )


@user_authenticated_decorator
def delete_phone_book_record(request, pk):
    delete_it = PhoneBookRow.objects.get(id=pk)
    delete_it.delete()
    messages.success(
        request,
        message="Record Deleted Successfully..."
    )
    return redirect('home')


@user_authenticated_decorator
def add_phone_book_record(request):
    form = AddRecordForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, message="Phone Book Record Added...")
            return redirect('home')
    return render(
        request,
        template_name='add_record.html',
        context={'form': form}
    )


@user_authenticated_decorator
def add_city(request):
    form = AddCityForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, message="City Added...")
            return redirect('add_phone_book_record')
    return render(
        request,
        template_name='add_city.html',
        context={'form': form}
    )


@user_authenticated_decorator
def add_province(request):
    form = AddProvinceForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, message="Province Added...")
            return redirect('add_phone_book_record')
    return render(
        request,
        template_name='add_province.html',
        context={'form': form}
    )


@user_authenticated_decorator
def update_phone_book_record(request, pk):
    current_record = PhoneBookRow.objects.get(id=pk)
    form = AddRecordForm(request.POST or None, instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(
            request,
            message="Phone Book Record Has Been Updated!"
        )
        return redirect('home')
    return render(
        request,
        template_name='update_record.html',
        context={'form': form}
    )
