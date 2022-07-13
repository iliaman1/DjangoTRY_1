from django.urls import path, include

from .views import WomenHome, ShowPost, about, AddPage, Contact, LoginUser, logout_user, RegisterUser, TopRaited, \
    ShowCategory, PostVote, CommentVote

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', Contact.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('top/', TopRaited.as_view(), name='toprait'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('post/<slug:post_slug>/', include([
        path('like/', PostVote.like, name='postlike'),
        path('dislike/', PostVote.dislike, name='postdislike'),
        path('comment_like/<int:comment_id>', CommentVote.like, name='commentlike'),
        path('comment_dislike/<int:comment_id>', CommentVote.dislike, name='commentdislike')
    ])),
    path('category/<slug:cat_slug>/', ShowCategory.as_view(), name='category')
]