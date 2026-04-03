from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import Category, Course, User


class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, "users.html", {"users": users})


class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, "courses.html", {"courses": courses})

    def post(self, request):
        name = request.POST.get("name")
        course_description = request.POST.get("course_description")
        category_id = request.POST.get("category_id")
        media = request.FILES.get("media")
        category = get_object_or_404(Category, id=category_id)
        course = Course.objects.create(
            name=name,
            course_description=course_description,
            category=category,
            media=media,
        )
        return render(request, "course_detail.html", {"course": course})


class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, "categories.html", {"categories": categories})

    def post(self, request):
        name = request.POST.get("name")
        category_description = request.POST.get("category_description")
        category = Category.objects.create(
            name=name,
            category_description=category_description,
        )
        return render(request, "category_detail.html", {"category": category})


class CreateUserView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, "user_create.html", {"courses": courses})

    def post(self, request):
        full_name = request.POST.get("full_name")
        birth_date = request.POST.get("birth_date")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        course_id = request.POST.get("course_id")
        course = get_object_or_404(Course, id=course_id)
        user = User.objects.create(
            full_name=full_name,
            birth_date=birth_date,
            start_date=start_date,
            end_date=end_date,
            course=course,
        )
        return render(request, "user_detail.html", {"user": user})


class CourseCreateView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, "course_create.html", {"categories": categories})

    def post(self, request):
        name = request.POST.get("name")
        course_description = request.POST.get("course_description")
        category_id = request.POST.get("category_id")
        category = get_object_or_404(Category, id=category_id)
        media = request.FILES.get("media")
        course = Course.objects.create(
            name=name,
            course_description=course_description,
            category=category,
            media=media,
        )
        return render(request, "course_detail.html", {"course": course})


class CategoryCreateView(View):
    def get(self, request):
        return render(request, "category_create.html")

    def post(self, request):
        name = request.POST.get("name")
        category_description = request.POST.get("category_description")
        category = Category.objects.create(
            name=name,
            category_description=category_description,
        )
        return render(request, "category_detail.html", {"category": category})


class UserDetailView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        return render(request, "user_detail.html", {"user": user})


class CourseDetailView(View):
    def get(self, request, pk):
        course = get_object_or_404(Course, id=pk)
        return render(request, "course_detail.html", {"course": course})


class CategoryDetailView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        courses = Course.objects.filter(category=category)
        return render(request, "category_detail.html", {"courses": courses, "category": category})


class UserUpdateView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        courses = Course.objects.all()
        return render(request, "user_update.html", {"user": user, "courses": courses})

    def post(self, request, pk):
        user = get_object_or_404(User, id=pk)
        course_id = request.POST.get("course_id")
        user.full_name = request.POST.get("full_name")
        user.birth_date = request.POST.get("birth_date")
        user.start_date = request.POST.get("start_date")
        user.end_date = request.POST.get("end_date")
        user.course = get_object_or_404(Course, id=course_id)
        user.save()
        return render(request, "user_detail.html", {"user": user})


class CourseUpdateView(View):
    def get(self, request, pk):
        course = get_object_or_404(Course, id=pk)
        categories = Category.objects.all()
        return render(request, "course_update.html", {"course": course, "categories": categories})

    def post(self, request, pk):
        course = get_object_or_404(Course, id=pk)
        category_id = request.POST.get("category_id")
        course.name = request.POST.get("name")
        course.course_description = request.POST.get("course_description")
        course.category = get_object_or_404(Category, id=category_id)
        media = request.FILES.get("media")
        if media:
            course.media = media
        course.save()
        return render(request, "course_detail.html", {"course": course})


class CategoryUpdateView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        return render(request, "category_update.html", {"category": category})

    def post(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        category.name = request.POST.get("name")
        category.category_description = request.POST.get("category_description")
        category.save()
        return render(request, "category_detail.html", {"category": category})


class UserDeleteView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        return render(request, "user_delete.html", {"user": user})

    def post(self, request, pk):
        user = get_object_or_404(User, id=pk)
        user.delete()
        return render(request, "users.html", {"users": User.objects.all()})


class CourseDeleteView(View):
    def get(self, request, pk):
        course = get_object_or_404(Course, id=pk)
        return render(request, "course_delete.html", {"course": course})

    def post(self, request, pk):
        course = get_object_or_404(Course, id=pk)
        course.delete()
        return render(request, "courses.html", {"courses": Course.objects.all()})


class CategoryDeleteView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        return render(request, "category_delete.html", {"category": category})

    def post(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        category.delete()
        return render(request, "categories.html", {"categories": Category.objects.all()})
