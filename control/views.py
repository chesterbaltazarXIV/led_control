from django.shortcuts import render, redirect
import serial, time

com = serial.Serial("COM8")

# Create your views here.
def index(request):
    if request.method == "POST":
        if "turn_on" in request.POST:
            com.write((1).to_bytes(2, 'little'))
        elif "turn_off" in request.POST:
            com.write((2).to_bytes(2, 'little'))
        return redirect("/")
    else:
        return render(request, template_name="control/index.html", context={})