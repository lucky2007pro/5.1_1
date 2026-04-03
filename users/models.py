from django.db import models

# Create your models here.

class User(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='course')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

class Course(models.Model):
    name = models.CharField(max_length=255)
    course_description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    media = models.FileField(upload_to='media/')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    category_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name