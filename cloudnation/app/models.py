from django.db import models
import uuid

# Create your models here.

class Database(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    database_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  
        return f"{self.id} - {self.database_type}"

class Plan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plan_type = models.CharField(max_length=255)
    storage = models.PositiveIntegerField()
    bandwidth = models.PositiveIntegerField()
    memory = models.PositiveIntegerField()
    cpu = models.PositiveIntegerField()
    monthly_cost = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_hour = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  
        return f"{self.id} - {self.plan_type}"

    
class UserAppDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization_name = models.CharField(max_length=255)
    repository_name = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    app_name = models.CharField(max_length=255, unique = True)
    region = models.CharField(max_length=255)
    framework = models.CharField(max_length=255)
    database_type = models.ForeignKey(Database, on_delete=models.CASCADE)
    plan=models.ForeignKey(Plan, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  
        return f"{self.id} - {self.app_name}"
    

class EnvironmentVariable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    key = models.CharField(max_length=255)
    value = models.TextField()
    user_app = models.ForeignKey(UserAppDetails, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  
        return f"{self.key} - {self.value}"