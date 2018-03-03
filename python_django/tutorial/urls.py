from django.conf.urls import url, include
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'courses', views.CoursesViewSet)
router.register(r'curriculums', views.CurriculumsViewSet)
router.register(r'groups', views.GroupsViewSet)
router.register(r'implements', views.ImplementsViewSet)
router.register(r'subgroups', views.subgroupsViewSet)
router.register(r'rooms', views.RoomsViewSet)
router.register(r'teachers', views.TeachersViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
