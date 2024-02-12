from django.db import models
from utils.models import BaseModel


class OptionType(models.TextChoices):
    SINGLE = "Single"
    EXTENDED = "Extended"
    CHOICE = "Choice"
    BUTTON = "Button"
    TEXT = "Text"
    NUMBER = "Number"
    MULTIPLE_CHOICE = "Multiple choice"


class Option(BaseModel):
    title = models.CharField(max_length=256)  # Марка и модель, Кузов , Объём двигателя
    type = models.CharField(max_length=15, choices=OptionType.choices)
    code = models.CharField(
        max_length=256, null=True, blank=True
    )  # year, bargain,auto_car_transm,auto-run

    is_main = models.BooleanField(default=False)
    is_filter = models.BooleanField(default=False)
    is_main_filter = models.BooleanField(default=False)
    is_advanced_filter = models.BooleanField(default=False)

    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class OptionValue(BaseModel):
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="values")
    value = models.CharField(max_length=256)  # Bentley, Sedan, Zadniy

    def __str__(self):
        return self.value


class OptionValueExtended(BaseModel):
    option_value = models.ForeignKey(
        OptionValue,
        on_delete=models.CASCADE,
        related_name="values_extended",
    )
    value = models.CharField(max_length=256)  # Continental
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="children", null=True, blank=True
    )

    def __str__(self):
        return self.value


class PostOption(BaseModel):
    post = models.ForeignKey(
        "avto.Post", on_delete=models.CASCADE, related_name="options"
    )
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="posts")
    value = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f"{self.post} {self.option}"

    @classmethod
    def generate_json_options(cls, post_id):
        data = {"year": None, "model": None, "options": []}
        post_options = (
            cls.objects.filter(post_id=post_id)
            .order_by("option__order")
            .select_related(
                "option",
            )
            .prefetch_related("values")
            .prefetch_related(
                "values", "values__option_value", "values__option_value_extended"
            )
        )
        for post_option in post_options:
            data["options"].append(
                {
                    "title": post_option.option.title,
                    "value": post_option.value,
                    "values": [
                        values.option_value.value for values in post_option.values.all()
                    ],
                }
            )
            if post_option.option.code == "year":
                data["year"] = post_option.value
            if post_option.option.code == "model":
                for value in post_option.values.all():
                    if value.option_value_extended:
                        if value.option_value_extended.parent:
                            data["model"] = (
                                f"{value.option_value.value} {value.option_value_extended.parent.value}, "
                                f"{value.option_value_extended.value}"
                            )
                        else:
                            data["model"] = (
                                f"{value.option_value.value} {value.option_value_extended.value}"
                            )
                    else:
                        data["model"] = value.option_value.value
        return data


class PostOptionValue(BaseModel):
    post_option = models.ForeignKey(
        PostOption, on_delete=models.CASCADE, related_name="values"
    )
    option_value = models.ForeignKey(OptionValue, on_delete=models.CASCADE)
    option_value_extended = models.ForeignKey(
        OptionValueExtended, on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        unique_together = ("post_option", "option_value")
