from django.shortcuts import render
from django.views.generic import TemplateView
import datetime

# Create your views here.
class HomeView(TemplateView):
    # karena mewariskan dari TemplateView maka perlu ada template_name
    template_name = 'home.html'

    # method get untuk menampilkan halaman html
    def get(self, request):
        first_name = "john"
        today = datetime.datetime.today()
        return render(request, self.template_name, {'name':first_name,'today':today})

class AboutView(TemplateView):
    template_name = 'about.html'

    def get(self, request):
        team= ['wahyudi', 'adit', 'danu','alex']
        
        return render(request, self.template_name, {"my_team":team})
        #buat view untuk contack
        #tampilkan tanggal dalam bentuk monday,april 27,2020
class ContactView(TemplateView):
    template_name = 'contact.html'

    def get(self, request):
        today_contact = datetime.datetime.today().strftime(" %A, %B , %d, %Y")
        return render(request, self.template_name, {'today_contact' :today_contact})
