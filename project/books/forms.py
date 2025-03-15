from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = ''
        self.fields['author'].label = ''
        self.fields['category'].label = ''
        self.fields['description'].label = ''
        self.fields['image'].label = ''
        self.fields['date'].label = ''

    class Meta:
        model = Book
        fields = ['name', 'author', 'category','description', 'date', "image"]
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder' : 'Book Title', 'autofocus' : '', 'id': 'tit'}),
            'author' : forms.TextInput(attrs={'placeholder' : 'Book Author', 'id': 'auth'}),
            
            'category' : forms.Select(attrs={'id': 'cat'}),
            'description' : forms.Textarea(attrs={'placeholder': 'Description'}),
            
            'date' : forms.DateInput(attrs={"type" : 'date', 'id': 'date'}),
            "image" : forms.FileInput(attrs={'id': 'bookCover'}),
        }