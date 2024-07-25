from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)

# Create your models here.
User = get_user_model()


class TeacherFinancialOverview(models.Model):
    totalRevenue = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    averageRating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    totalStudent = models.IntegerField()
    totalEarning = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    todayEarning = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pending = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    inReview = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    available = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.instructor.username


class StudentLocation(models.Model):
    country = models.CharField(max_length=64)
    amountOfStudents = models.IntegerField()
    studentLocations = models.ForeignKey(TeacherFinancialOverview, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return f"{self.country}|{self.amountOfStudents}"