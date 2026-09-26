from django.db import models
from django.utils.text import slugify


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ContactMessage(TimeStampedModel):
    PROJECT_TYPES = [
        ('AI / Machine Learning', 'AI / Machine Learning'),
        ('Data Science', 'Data Science'),
        ('Software Development', 'Software Development'),
        ('Automation', 'Automation'),
        ('Research Collaboration', 'Research Collaboration'),
        ('IoT / Intelligent Systems', 'IoT / Intelligent Systems'),
        ('Other', 'Other'),
    ]
    STATUS = [
        ('new', 'New'),
        ('in_progress', 'In progress'),
        ('replied', 'Replied'),
        ('closed', 'Closed'),
    ]
    name = models.CharField(max_length=120)
    email = models.EmailField()
    company = models.CharField(max_length=160, blank=True)
    project_type = models.CharField(max_length=80, choices=PROJECT_TYPES)
    message = models.TextField(max_length=5000)
    status = models.CharField(max_length=20, choices=STATUS, default='new')
    is_read = models.BooleanField(default=False)
    source = models.CharField(max_length=40, default='website')

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status', '-created_at']),
            models.Index(fields=['email']),
        ]
        verbose_name = 'Contact message'
        verbose_name_plural = 'Contact messages'

    def __str__(self):
        return f'{self.name} — {self.project_type}'


class Project(TimeStampedModel):
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    summary = models.TextField(max_length=600)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    technologies = models.JSONField(default=list, blank=True)
    image_url = models.URLField(blank=True)
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-is_featured', '-published_at', '-created_at']
        indexes = [
            models.Index(fields=['is_published', '-published_at']),
            models.Index(fields=['category']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ResearchProject(TimeStampedModel):
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    summary = models.TextField(max_length=700)
    research_area = models.CharField(max_length=120)
    methodology = models.TextField(blank=True)
    status = models.CharField(max_length=80, default='Ongoing')
    publication_url = models.URLField(blank=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['research_area']),
            models.Index(fields=['is_published', '-published_at']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Insight(TimeStampedModel):
    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True, blank=True)
    excerpt = models.TextField(max_length=500)
    body = models.TextField()
    author = models.CharField(max_length=120, blank=True)
    tags = models.JSONField(default=list, blank=True)
    cover_image_url = models.URLField(blank=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-published_at', '-created_at']
        indexes = [models.Index(fields=['is_published', '-published_at'])]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Technology(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100)
    website_url = models.URLField(blank=True)
    logo_url = models.URLField(blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ['sort_order', 'name']

    def __str__(self):
        return self.name


class TeamMember(TimeStampedModel):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    bio = models.TextField(blank=True)
    photo_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ['sort_order', 'name']

    def __str__(self):
        return f'{self.name} — {self.role}'


class SiteSetting(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField(blank=True)
    description = models.CharField(max_length=240, blank=True)

    class Meta:
        ordering = ['key']

    def __str__(self):
        return self.key
