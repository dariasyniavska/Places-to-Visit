import random
from django.shortcuts import render, redirect
from .forms import PlaceForm
from datetime import datetime
from .inisial_data import PLACES


def index(request):
    random_place = None
    if request.GET.get('random'):
        weights = [place['rating'] for place in PLACES]
        random_place = random.choices(PLACES, weights=weights, k=1)[0]

    return render(request, "places/index.html", {
        "places": PLACES,
        "random_place": random_place
    })


def place_list(request):
    return render(request, "places/list.html", {"places": PLACES})


def place_detail(request, place_id):
    place = next((p for p in PLACES if p["id"] == place_id), None)
    if not place:
        return redirect("place_list")
    return render(request, "places/detail.html", {"place": place})


def add_place(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            new_data = form.cleaned_data
            current_date = datetime.now().strftime("%d.%m.%Y")
            new_place = {
                "id": len(PLACES) + 1,
                "title": new_data["title"],
                "category": new_data.get("category") or "Гірська вершина",
                "location": new_data.get("location") if new_data.get("location") else None,
                "rating": new_data["rating"],
                "created_at": current_date,
                "description": new_data.get("description", "")
            }
            PLACES.append(new_place)
            return redirect("place_list")
    else:
        form = PlaceForm()

    return render(request, "places/add_place.html", {"form": form})
