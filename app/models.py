from django.db import models
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class AgencyMeta(models.Model):
    page_name = models.CharField(max_length=100, unique=True)
    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField()
    keywords = models.TextField(blank=True)
    google_analytics_script = models.TextField(blank=True)
    facebook_pixel_script = models.TextField(blank=True)
    
    def __str__(self):
        return self.page_name

class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    #icon = models.CharField(max_length=50)  # Font Awesome icon name
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    def __str__(self):
        return self.title

# class BlogCategory(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True)

# class BlogTag(models.Model):
#     name = models.CharField(max_length=50)
#     slug = models.SlugField(unique=True)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/')
  #  category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
   # tags = models.ManyToManyField(BlogTag)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    meta_title = models.CharField(max_length=150, blank=True)
    meta_description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-created_at']

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    def __str__(self):
        return self.title

class Lead(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)  # Added phone number
    email = models.EmailField()
    service = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} -{self.phone}- {self.email}"

class CookieConsentSetting(models.Model):
    message = models.TextField(default="We use cookies to enhance your experience.")
    policy_link = models.URLField(blank=True)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return "Cookie Consent Setting"

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=300)
    detailed_description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    client_name = models.CharField(max_length=100, blank=True)
    project_url = models.URLField(blank=True)
    technologies_used = models.CharField(max_length=200)
    date_completed = models.DateField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='banners/')
    link = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class MultiImage(models.Model):
    # Relations to specific models (can be nullable if not used)
    service = models.ForeignKey('Service', on_delete=models.CASCADE, null=True, blank=True, related_name='multi_images')
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, null=True, blank=True, related_name='multi_images')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=True, blank=True, related_name='multi_images')

    # Actual image
    image = models.ImageField(upload_to='multi_images/')
    
    
    # Optional details
    alt_text = models.CharField(max_length=150, blank=True, help_text="SEO-friendly alt text")
    order = models.PositiveIntegerField(default=0, help_text="Image display order")

    def __str__(self):
        parent = self.service or self.blog or self.project
        return f"{parent} - {self.alt_text} ({self.image.name})"

    class Meta:
        ordering = ['order']
