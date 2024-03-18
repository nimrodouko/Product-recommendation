
from .forms import CustomUserCreationForm 
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponse
from joblib import load  #inaleta model
model = load('models/refinedproducts.joblib')

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

    


    def form_valid(self, form):
            
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            budget = form.cleaned_data['budget']
            location = form.cleaned_data['location']
            print(gender,location)
            
            if location.lower() == 'rural':
                location=0
            elif location.lower()=='urban':
                location=1

            if gender.lower()=='male':
                gender = 0
            elif gender.lower() == 'female':
                gender =1
  

            
            prediction = model.predict([[age, budget, gender,location]])
            

            
            
            form.instance.prediction_result = prediction
            print(prediction)
            

            if prediction[0] == 0:
              return redirect('furniture')
            elif prediction[0] == 1:
                return  redirect('electronics')
            elif prediction[0] == 2:
                return  redirect('clothing')
           