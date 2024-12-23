from rest_framework import generics
from rest_framework.response import Response
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, SensorCreateSerializer, \
    MeasurementCreateSerializer, SensorUpdateSerializer

# Создать датчик.
class SensorCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorCreateSerializer

# Добавить измерение.
class MeasurementCreateView(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer

# Изменить датчик.
class SensorUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorUpdateSerializer

    # Получить список датчиков.
    def get(self, request, *args, **kwargs):
        queryset = Sensor.objects.get(id=kwargs['pk'])
        print(queryset)
        serializer_class = SensorDetailSerializer(queryset)
        return Response(serializer_class.data)






