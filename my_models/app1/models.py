from django.db import models

# Create your models here.

# choses for person class
shirt_sizes=[
    ('S','Small'),
    ('M','Medium'),
    ('L','Large')
]

class Person(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    dress_name=models.CharField(max_length=50, null=True)
    dress_size=models.CharField(max_length=1,choices=shirt_sizes, null=True)

    #custom methods in model class
    def shirt_size_status(self):
        if self.dress_size=='S':
            return "Preson Used Small Sized"
        elif self.dress_size=='M':
            return "Preson Used Medium Sized"
        elif self.dress_size=='L':
            return "Preson Used Large Sized"

    @property
    def full_name(self):
        return '%s %s'%(self.first_name,self.last_name)

    def __str__(self):
        return self.first_name+" "+self.last_name

# You can also use enumeration classes to define choices in a concise way:

class Runner(models.Model):
    MedalType=models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    game_name=models.CharField(max_length=50)
    medal=models.CharField(max_length=10,choices=MedalType.choices,blank=True)

    def __str__(self):
        return self.game_name

class Group(models.Model):
    group_name=models.CharField(max_length=50)
    member=models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.group_name
    

class Membership(models.Model):
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
    group=models.ForeignKey(Group, on_delete=models.CASCADE,related_name='member_group')
    date_joinded=models.DateField(auto_now_add=True)
    invite_reason=models.CharField(max_length=100)

    def __str__(self):
        return str(self.person)

    #class Meta(optional)
    class Meta:
        verbose_name = 'Membership'
        verbose_name_plural = "Membership's"

class Info(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=5)

    class Meta:
       abstract=True

class Student(Info):
    home_group = models.CharField(max_length=5)