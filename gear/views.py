from django.shortcuts import render
import csv
from pathlib import Path

def home(request):
    return render(request, "gear/home.html")

def w1(request):
    return render(request, "gear/w1.html")

def w2(request):
    return render(request, "gear/w2.html")

def cw(request):
    return render(request, "gear/cw.html")

def planetary_reducer(request):
    return render(request, "gear/planetary_reducer.html")

def info(request):
    return render(request, "gear/info.html")

def stub(request):
    return render(request, "gear/stub.html")

def w1_view(request):
    data = []
    csv_path = Path(__file__).resolve().parent / "data" / "w1.csv"
    with open(csv_path, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # переименуем ключи для шаблона
            row_clean = {k.replace(":", "_").replace(".", "_"): v for k, v in row.items()}
            data.append(row_clean)
    return render(request, "gear/w1.html", {"table": data})

