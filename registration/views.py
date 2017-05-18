from django.shortcuts import render
from registration.forms import UserForm, UserProfileForm

# Create your views here.
def register(request):
    registered = False #will be set true when the registration is successful
# If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        #grab information from the raw form information
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            # Now we hash the password with the set_password method then update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves,
            # we set commit=False. This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # If user provided a profile picture we need to get it from the input form
            # and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                # Now we save the UserProfile model instance.
                profile.save()
                # Update our variable to indicate that registration was successful.
                registered = True
        else:
            #if form is invalid
            print(user_form.errors, profile_form.errors)
    else: #Not a HTTP POST, so we render our blank form using two ModelForm instances
        user_form = UserForm()
        profile_form = UserProfileForm()
    # Render the template depending on the context.
    return render(request,'registration/register.html',{'user_form': user_form,
                                                'profile_form': profile_form,
                                                'registered': registered
                                                })
