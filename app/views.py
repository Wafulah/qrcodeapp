from django.shortcuts import render
from .models import QrCode
# Create your views here.
def home(request):
   if request.method=="POST":
      Url=request.POST['url']
      QrCode.objects.create(url=Url)

   qr_code=QrCode.objects.all()
   return render(request,"home.html",{'qr_code':qr_code})