from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
                              attrs={
                                  "class": "form-control"
                              }
                          ))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput( attrs={
                                  "class": "form-control"
                              }))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        "class": "form-control"
    }))
    nom = forms.CharField(max_length=30,
                          widget=forms.TextInput(
                              attrs={
                                  "class": "form-control"
                              }
                          )
                          )
    prenom = forms.CharField(max_length=30,
                             widget=forms.TextInput(
                                 attrs={
                                     "class": "form-control"
                                 }
                             ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    addresse = forms.CharField(max_length=100,
                               widget=forms.TextInput(
                                   attrs={
                                       "class": "form-control"
                                   }
                               )
                               )

    USER_TYPES = [
        ('Client', 'Client'),
        ('Organisateur', 'Organisateur'),
        ('Admin', 'Admin')
    ]
    user_type = forms.ChoiceField(choices=USER_TYPES, widget=forms.Select(
        attrs={
            "class": "form-control"
        }
    ))

    lieu = forms.CharField(max_length=100, required=False, initial='Tunisie', widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }
    ))
    description = forms.CharField(max_length=100, required=False, initial='SEO', widget=forms.Textarea(
        attrs={
            "class": "form-control"
        }
    ))

    CATEGORIES = [
        ('Coupe du tunisie', 'Coupe du tunisie'),
        ('ligue 1', 'ligue 1'),
        ('ligue 2', 'ligue 2'),
        ('Amateur League', 'Amateur League')
    ]
    categorie = forms.ChoiceField(choices=CATEGORIES, required=False, initial='Coupe du tunisie',
                                  widget=forms.Select(
                                      attrs={
                                          "class": "form-control"
                                      }
                                  ))
