# Ex03 Django ORM Web Application
## Date: 28/09/2004

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ER Diagram
![image](https://github.com/user-attachments/assets/92836091-ffe7-421b-8b42-542695efba04)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

## admin.py
```

from django.contrib import admin
from .models import bankloan,bankloanAdmin
admin.site.register(bankloan,bankloanAdmin)
```

## models.py
```


from django.db import models
from django.contrib import admin
class bankloan(models.Model):
    accno=models.IntegerField(primary_key=True);
    name=models.CharField(max_length=100);
    loanamt=models.IntegerField();
    loanlimit=models.IntegerField();
    phoneno=models.IntegerField();

class bankloanAdmin(admin.ModelAdmin):
    list_display=('accno','name','loanamt','loanlimit','phoneno')
```



## OUTPUT
![alt text](<Screenshot 2024-09-28 170114.png>)
![alt text](<Screenshot 2024-09-28 170551.png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
