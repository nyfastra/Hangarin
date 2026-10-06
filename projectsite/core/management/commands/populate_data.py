from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
import random

from core.models import Priority, Category, Task, SubTask, Note


class Command(BaseCommand):
    help = "Populate database with initial Categories, Priorities, and fake data."

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Priority & Category setup
        priorities = ["High", "Medium", "Low", "Critical", "Optional"]
        categories = ["Work", "School", "Personal", "Finance", "Projects"]

        priority_objs = [
            Priority.objects.get_or_create(name=name)[0] for name in priorities
        ]
        category_objs = [
            Category.objects.get_or_create(name=name)[0] for name in categories
        ]

        self.stdout.write(self.style.SUCCESS("Categories and Priorities seeded."))

        # Task setup
        statuses = ["Pending", "In Progress", "Completed"]
        tasks = []

        for _ in range(15):
            naive_datetime = fake.date_time_this_month()
            aware_datetime = timezone.make_aware(naive_datetime)

            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=aware_datetime,
                status=fake.random_element(elements=statuses),
                category=random.choice(category_objs),
                priority=random.choice(priority_objs),
            )
            tasks.append(task)

        self.stdout.write(self.style.SUCCESS("Tasks seeded."))

        # SubTask & Note setup
        for task in tasks:
            for _ in range(random.randint(1, 3)):
                SubTask.objects.create(
                    parent_task=task,
                    title=fake.sentence(nb_words=4),
                    status=fake.random_element(elements=statuses),
                )

            for _ in range(random.randint(1, 2)):
                Note.objects.create(
                    task=task,
                    content=fake.paragraph(nb_sentences=2),
                )

        self.stdout.write(self.style.SUCCESS("SubTasks and Notes seeded successfully!"))