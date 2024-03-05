from django.contrib import admin
from django.urls import path
from api.views import * 


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api/enrollee/<str:snils>/selected-specialities', 
        EnrolleeSpeciality.as_view()
    ),
    path(
        'api/enrollee/<str:snils>/rating', 
        RatingAPIView.as_view()
    ),
]
