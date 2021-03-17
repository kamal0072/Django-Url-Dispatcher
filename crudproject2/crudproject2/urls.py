
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.add_show, name="addandshow"),
    path('', views.UserAddShowView.as_view(),name='addandshow'),

    # path('delete/<int:id>/', views.delete_data, name="deletedata"),

    path('delete/<int:id>/', views.UserDeleteView.as_view(), name="deletedata"),
    
    # path('<int:id>/', views.update_data, name="updatedata"),
    path('<int:id>/', views.UserUpdateView.as_view(), name="updatedata"),
]
