# Create your views here.from django.db import models

from django.db import models
from django.contrib.auth.models import User
import json

def location_share(request):
     u = UserProfile.objects.get(user=User.objects.get(request.POST['username']))
     u.location_lat = float(request.POST['lat'])
     u.location_lon = float(request.POST['lon'])
     u.location_text = UserProfile.objects.get(lon_text=User.objects.get(request.POST['lon_text']))
     return HttpResponse(json.dumps({'success': True}, content_type='application/json'))




