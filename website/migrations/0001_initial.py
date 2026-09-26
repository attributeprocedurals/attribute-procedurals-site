from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [migrations.CreateModel(
        name='ContactMessage',
        fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('name', models.CharField(max_length=120)),
            ('email', models.EmailField(max_length=254)),
            ('company', models.CharField(blank=True, max_length=160)),
            ('project_type', models.CharField(choices=[('AI / Machine Learning', 'AI / Machine Learning'), ('Data Science', 'Data Science'), ('Software Development', 'Software Development'), ('Automation', 'Automation'), ('Research Collaboration', 'Research Collaboration'), ('IoT / Intelligent Systems', 'IoT / Intelligent Systems'), ('Other', 'Other')], max_length=80)),
            ('message', models.TextField(max_length=5000)),
            ('created_at', models.DateTimeField(auto_now_add=True)),
            ('is_read', models.BooleanField(default=False)),
        ],
        options={'ordering': ['-created_at'], 'verbose_name': 'Contact message', 'verbose_name_plural': 'Contact messages'},
    )]
