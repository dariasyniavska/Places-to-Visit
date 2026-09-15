from django import forms


class PlaceForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        required=True,
        label="Назва"
    )
    category = forms.CharField(
        max_length=100,
        required=False,
        initial="Гірська вершина",
        label="Тип місця"
    )
    location = forms.CharField(
        max_length=100,
        required=False,
        label="Локація"
    )
    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        required=True,
        label="Рейтинг"
    )
    description = forms.CharField(
        widget=forms.Textarea,
        required=False,
        label="Опис"
    )
