from django.shortcuts import render
from django.template import Template, Context
from .forms import SimpleForm

# Create your views here.


# define our initial view
def homepage(request):

    # initialize miles to empty string
    miles = ""

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = SimpleForm(request.POST)

        # check whether the form data is valid
        if form.is_valid():

            # load the cleaned data and pass it to the convert to miles method
            kilometers = form.cleaned_data['kilometers']
            miles = miles_from(kilometers)

    # if a GET we'll create a blank from
    else:
        form = SimpleForm()

    # create the context dictionary to return the miles string
    context = {
        'form': form,
        'miles': miles,
    }

    # send the form and miles conversion to the index.html page
    return render(request, 'index.html', context)


def miles_from(kilometers):
    """Convert Kilometers to Miles"""

    miles = float(kilometers / 1.609)
    miles = round(miles, 3)  # Round to three decimal places
    return str(miles)
