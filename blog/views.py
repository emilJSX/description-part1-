from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .form import *
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import *
from django.views.generic.edit import CreateView, FormView
from django.views.generic import ListView
from .models import Event
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-Date')
    serializer_class = BlogSerializer

def register(request):
    return render(request, 'blog/signup.html')

def login(request):
    return render(request, 'blog/login.html')

def BlogViews(request):
    posts = Blog.objects.all()
    return render(request, 'blog/index.html', { 'post': posts })

def Success(request):
    return render(request, 'blog/success.html')

def BlogDetail(request, slug):
    post = get_object_or_404(Blog, Slug = slug)
    comments = post.comments.filter(Active=True, Parent__isnull=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid:
            Parent_obj = None
            try:
                Parent_id = int(request.POST.get('Parent_id'))
            except:
                Parent_id = None
            if Parent_id:
                Parent_obj = Comment.objects.get(id=Parent_id)
                if Parent_obj:
                    reply_comment = comment_form.save(commit=False)
                    reply_comment.Parent = Parent_obj
            new_comment = comment_form.save(commit=False)
            new_comment.Post = post
            new_comment.save()
            return redirect('blog:detail', slug)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/blogdetail.html', {'blog':post, 'comments':comments, 'comment_form':comment_form})


def SignUp(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('blog:success')
    else:
        form = UserRegisterForm()
    return render(request, "registration/signup.html", {'form': form})



def Contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')

            template = get_template('blog/contact_form.txt')
            context = {
                'contact_name' : contact_name,
                'contact_email' : contact_email,
                'contact_content' : contact_content,
            }
            
            content = template.render(context)

            email = EmailMessage(
                "New contact form email",
                content,
                "Tewaves Project" + '',
                ['emka6451@gmail.com'],
                headers = { 'Reply To': contact_email }
            )

            email.send()

            return redirect('blog:success')
    return render(request, 'blog/contact.html', {'form':Contact_Form })

def join(request):
    return render(request, 'blog/join_events.html')

def logout(request):
    return render(request, 'blog/base.html')

def password_change_form(request):
    return render(request, 'registration/password_change_form.html')

def eventcreate(request):
    return render(request, 'blog/create.html')

def event_user_page(request):
    return render(request, 'blog/event_user_page.html')


class EventCreate(CreateView):
    model = Event
    form_class = EventForm
    # fields = ['name','description','start_time','img','category','appointment_time']
    template_name = 'blog/create.html'
    success_url = '/'

    def save(self, *args, **kwargs):

        print("AAA", args, kwargs)