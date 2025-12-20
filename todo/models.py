from django.db import models

# Create your models here.


class Task(models.Model):
    CATEGORY_CHOICES = [
        ("Work", "Work"),
        ("Study", "Study"),
        ("Health", "Health"),
        ("Personal", "Personal"),
        ("Other", "Other")
    ]
    title = models.CharField(max_length=255)
    due_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10,
        choices=[("High", "High"), ("Medium", "Medius"), ("Low", "Low")],
        default="Medium"
    )
    category = models.CharField(
        max_length=250,
        choices=CATEGORY_CHOICES,
        default="Other"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
