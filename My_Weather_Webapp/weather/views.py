@@ -4,7 +4,7 @@
from .forms import CityForm
# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=63ce12902fbc6632e54812e533cb4459'
    url = 'should_be_unique_for_you'
    err_msg = ''
    message = ''
    message_class = ''
@@ -49,4 +49,4 @@ def index(request):
    return render(request,'weather/weather.html', context)
def delete_city(requests, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home') 
    return redirect('home')
