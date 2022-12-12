from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
# Create your views here.
def index(request):
    return render(request, "index.html")
def postuser(request):
    name = request.POST.get("Name", "Undefined")
    email = request.POST.get("Email", "Undefined")
    phone = request.POST.get("Phone Number", "Undefined")
    service = request.POST.get("Select Service", "Undefined")
    about = request.POST.get("about", "Undefined")
    return HttpResponse(f"<h2> name: {name} email: {email} phone: {phone} service: {service} about: {about} </h2>")


def order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        country = request.POST.get('country')
        city = request.POST.get('city')
        street = request.POST.get('street')
        home = request.POST.get('home')
        return HttpResponse(f"""<p>{name} {surname}, проверьте адрес доставки заказа: <p/>
        <p>{country}<p/>
        <p>{city}<p/>
        <p>{street}<p/>
        <p>{home}<p/>
        """)
    else:
        userform = UserForm()
        return render(request, "order.html", {"form": userform})
