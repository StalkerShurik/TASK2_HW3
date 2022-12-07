from django import forms


class CVForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=50)
    your_birth_date = forms.DateField(label='Your birth date')
    your_education = forms.CharField(label='Your education', max_length=100)
    your_hard_skills = forms.CharField(label='Your hard skills')
    your_soft_skills = forms.CharField(label='Your soft skills')
    your_job = forms.CharField(label='Your job')
    your_exp = forms.CharField(label='Your experience')

    #your_image = forms.ImageField(label='Your image field')
