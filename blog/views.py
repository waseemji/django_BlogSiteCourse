from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from datetime import date


from django.views.generic import ListView
from django.views import View
from django.urls import reverse 
from .models import Post
from .forms import CommentForm

aall_posts = [
    {
        "slug":"hike-in-the",
        "image":"some_image.jpg",
        "author":"Waseemji",
        "date":date(2022,10,18),
        "title":"Something",
        "excerpt":"lor ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deseem",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deserunt tempora aspernatur, odit minima accusantium quae beatae veritatis quos illo veniam deleniti optio illum, quaerat tenetur? 
        
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deserunt tempora aspernatur, odit minima accusantium quae beatae veritatis quos illo veniam deleniti optio illum, quaerat tenetur?"""
    },
    {
        "slug":"ride-in-the-woods",
        "image":"some_image.jpg",
        "author":"Waseemji",
        "date":date(2022,10,13),
        "title":"Something",
        "excerpt":"lor ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deseem",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deserunt tempora aspernatur, odit minima accusantium quae beatae veritatis quos illo veniam deleniti optio illum, quaerat tenetur? 
        
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deserunt tempora aspernatur, odit minima accusantium quae beatae veritatis quos illo veniam deleniti optio illum, quaerat tenetur?"""
    },
    {
        "slug":"joy-in-the-woods",
        "image":"some_image.jpg",
        "author":"Waseemji",
        "date":date(2022,10,2),
        "title":"Something",
        "excerpt":"lor ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deseem",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deserunt tempora aspernatur, odit minima accusantium quae beatae veritatis quos illo veniam deleniti optio illum, quaerat tenetur? 
        
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deserunt tempora aspernatur, odit minima accusantium quae beatae veritatis quos illo veniam deleniti optio illum, quaerat tenetur?"""
    },
    {
        "slug":"ntho-in-the-woods",
        "image":"some_image.jpg",
        "author":"Waseemji",
        "date":date(2022,10,12),
        "title":"Something",
        "excerpt":"lor ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deseem",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deserunt tempora aspernatur, odit minima accusantium quae beatae veritatis quos illo veniam deleniti optio illum, quaerat tenetur? 
        
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deserunt tempora aspernatur, odit minima accusantium quae beatae veritatis quos illo veniam deleniti optio illum, quaerat tenetur?"""
    },{
        "slug":"hike-in-the-woods",
        "image":"some_image.jpg",
        "author":"Waseemji",
        "date":date(2022,10,12),
        "title":"Something",
        "excerpt":"lor ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deseem",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deserunt tempora aspernatur, odit minima accusantium quae beatae veritatis quos illo veniam deleniti optio illum, quaerat tenetur? 
        
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deserunt tempora aspernatur, odit minima accusantium quae beatae veritatis quos illo veniam deleniti optio illum, quaerat tenetur?"""
    },{
        "slug":"hike-in-the-woods",
        "image":"some_image.jpg",
        "author":"Waseemji",
        "date":date(2022,10,12),
        "title":"Something",
        "excerpt":"lor ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deseem",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deserunt tempora aspernatur, odit minima accusantium quae beatae veritatis quos illo veniam deleniti optio illum, quaerat tenetur? 
        
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deserunt tempora aspernatur, odit minima accusantium quae beatae veritatis quos illo veniam deleniti optio illum, quaerat tenetur?"""
    },
    {
        "slug":"hike-in-the-woods",
        "image":"some_image.jpg",
        "author":"Waseemji",
        "date":date(2022,10,12),
        "title":"Something",
        "excerpt":"lor ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deseem",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deserunt tempora aspernatur, odit minima accusantium quae beatae veritatis quos illo veniam deleniti optio illum, quaerat tenetur? 
        
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus labore tempore repudiandae dolore deserunt tempora aspernatur, odit minima accusantium quae beatae veritatis quos illo veniam deleniti optio illum, quaerat tenetur?"""
    }
]

# def get_date(post):
#     return post['date']

# views with db

class HomePageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        base_query = super().get_queryset()
        latest_posts = base_query[:3]
        return latest_posts
    

# all_posts = Post.objects.all()
# def home_page(request):
#     latest_post = all_posts.order_by('-date')[:3]
#     return render(request,"blog/index.html",{
#         "posts":latest_post
#     })


# Create your views here.
# def home_page(request):
#     sorted_posts = sorted(all_posts,key=get_date)
#     latest_post = sorted_posts[-3:]
#     return render(request,"blog/index.html",{
#         "posts":latest_post
#         })

# def post_page(request):
#     return render(request,"blog/all-posts.html",{
#         "all_posts":all_posts
#     })

class AllPostView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["all_posts"] = all_posts

class SinglePostView(View):

    def has_stored_posts(self,request,posta_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = posta_id in stored_posts
        else:
            is_saved_for_later = False
        return is_saved_for_later
    
    def get(self,request,slug):
        posta = Post.objects.get(slug=slug)
        # comments = Comment.objects.filter(post = posta.pk)
        
        context = {
            "post":posta,
            "tags": posta.tag.all(),
            "comment_form" : CommentForm(),
            "comments":posta.comments.all().order_by("-id"),
            "has_stored_posts" : self.has_stored_posts(request,posta.id)
        }
        return render(request,"blog/post-detail.html",context)

    def post(self,request,slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("single-post-page",args=[slug]))

        context = {
            "post":post,
            "tags": post.tag.all(),
            "comment_form" : comment_form,
            "comments":post.comments.all().order_by("-id"),
            "has_stored_posts" : self.has_stored_posts(request,posta.id)
        }

        return render(request,"blog/post-detail.html",context)
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tags'] = self.object.tag.all()
    #     context["comment_form"] = CommentForm()
    #     return context
    

# def single_post(request,slug):
#     # identified_post = next(post for post in all_posts if post.slug == slug)
#     # identified_post = Post.objects.get(slug=slug)
#     identified_post = get_object_or_404(Post,slug=slug)
#     return render(request,"blog/post-detail.html",{
#         "post":identified_post,
#         "tags":identified_post.tag.all()
#     })



class ReadLaterView(View):
    def get(self,request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in = stored_posts)
            context["posts"]= posts
            context["has_posts"] = True

        return render(request,"blog/stored-posts.html", context)

    def post(self,request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []
        
        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        
        request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/")

