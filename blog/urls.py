from django.urls import path
from . import views

# urlpatterns = [
#     path("",views.home_page,name="home-page"),
#     path("posts/",views.post_page,name="post-page"),
#     path("posts/<slug:slug>",views.single_post,name="single-post-page") #/posts/my-first-page
# ]

urlpatterns = [
    path("",views.HomePageView.as_view(),name="home-page"),
    path("posts/",views.AllPostView.as_view(), name="post-page") ,
    path("posts/<slug:slug>",views.SinglePostView.as_view(),name="single-post-page"),
    path("read-later",views.ReadLaterView.as_view(), name="read-later")
]
