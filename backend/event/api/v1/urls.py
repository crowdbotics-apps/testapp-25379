from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    VendorViewSet,
    LocationViewSet,
    FavoritesViewSet,
    VendorDetailViewSet,
    CategoryViewSet,
    FaqViewSet,
    PresenterViewSet,
    ScheduleViewSet,
    MyScheduleViewSet,
    SponsorViewSet,
)

router = DefaultRouter()
router.register("sponsor", SponsorViewSet)
router.register("myschedule", MyScheduleViewSet)
router.register("vendordetail", VendorDetailViewSet)
router.register("presenter", PresenterViewSet)
router.register("schedule", ScheduleViewSet)
router.register("favorites", FavoritesViewSet)
router.register("location", LocationViewSet)
router.register("category", CategoryViewSet)
router.register("faq", FaqViewSet)
router.register("vendor", VendorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
