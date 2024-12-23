from django.urls import path

from measurement.views import SensorCreateView, MeasurementCreateView, SensorUpdateView

urlpatterns = [
    path('sensors/', SensorCreateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    path('sensors/<pk>/', SensorUpdateView.as_view()),
    # path(),

]
