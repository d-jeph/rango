from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category,Page
from rango.forms import CategoryForm,PageForm

# Create your views here.
def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:10]
    context_dict = {'categories':category_list,'pages':page_list}
    # Render the response and send it back!
    return render(request,'rango/index.html',context=context_dict)
def about(request):
    return render(request,'rango/about.html')


#view to show category details
def show_category(request,category_name_slug):
    # Create a context dictionary to pass to the templates
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception else return the model instance
        category = Category.objects.get(slug=category_name_slug)
        # Retrieve all of the associated pages.
        # Note that filter() will return a list of page objects or an empty list
        #
        pages = Page.objects.filter(category=category)
        # add the pages to our context dictionary
        context_dict['pages']=pages
        #add also the category
        context_dict['category']=category
    except Category.DoesNotExist:
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request,'rango/category.html',context=context_dict)


#to handle category creation
def add_category(request):
    form = CategoryForm()

    #HTTP POST?
    if request.method=='POST':
        form = CategoryForm(request.POST)
        #is the form data valid?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            return index(request) #return to index page
    else:
        # The supplied form contained errors
        print(form.errors)
    # Render the form with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)
    context_dict = {'form':form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)
