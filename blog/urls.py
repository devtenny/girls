from django.urls import path, include
from . import views

# 링크에서 작성하면 정순, 아래에서 지정한 name으로 찾아가는게 역순
urlpatterns = [
    # path('url', 사용할 함수 혹은 클래스, 이름)
    path('', views.post_list, name='post_list'),  # 나중에 template에서 view로 접근할 때 사용할 이름 지정
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
]