from django.db import models

    
class Property(models.Model):
    SALE = 'sale'
    RENT = 'rent'
    CATEGORY_CHOICES = [
        (SALE, 'بيع'),
        (RENT, 'إيجار'),
    ]
    
    PROPERTY_TYPE_CHOICES = [
        ('apartment', 'Apartment'),
        ('villa', 'Villa'),
        ('penthouse', 'Penthouse'),
        ('basement', 'Basement'),
        ('roof', 'Roof'),
        ('building', 'Building'),
        ('mall', 'Mall'),
        ('office', 'Office'),
        ('clinic', 'Clinic'),
        ('duplex', 'Duplex'),
        ('land', 'Land'),
        ('Store' , 'Store'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    area = models.PositiveIntegerField(help_text="Area in square meters")
    rooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default=SALE,
    )
    available_from = models.DateField(null=True, blank=True)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    number_of_floors = models.PositiveIntegerField(null=True, blank=True)
    units_count = models.PositiveIntegerField(null=True, blank=True)
    has_elevator = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    amenities = models.TextField(blank=True, help_text="Comma-separated amenities")
    is_available = models.BooleanField(default=True, verbose_name="availabl?")
    display_order = models.IntegerField(default=0)
   
    
    def __str__(self):
        return f"{self.title} - {self.get_category_display()}"
    

    

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {self.property.title}"    
   
