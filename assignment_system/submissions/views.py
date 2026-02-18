from django.shortcuts import render, redirect
from .models import Assignment, Submission
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth import login


# ===============================
# REGISTER STUDENT
# ===============================
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('assignment_list')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


# ===============================
# SHOW ALL ASSIGNMENTS + STATUS
# ===============================
def assignment_list(request):
    assignments = Assignment.objects.all()
    submitted = []

    if request.user.is_authenticated:
        submitted = Submission.objects.filter(
            student=request.user
        ).values_list('assignment_id', flat=True)

    return render(request, 'assignment_list.html', {
        'assignments': assignments,
        'submitted': submitted
    })


# ===============================
# UPLOAD ASSIGNMENT
# ===============================
@login_required
def upload_assignment(request, id):

    assignment = Assignment.objects.get(id=id)

    # PREVENT DUPLICATE SUBMISSION
    if Submission.objects.filter(
        student=request.user,
        assignment=assignment
    ).exists():
        return render(request, 'already_submitted.html')

    if request.method == 'POST':
        file = request.FILES['file']

        Submission.objects.create(
            student=request.user,
            assignment=assignment,
            file=file
        )
        return redirect('assignment_list')

    return render(request, 'upload.html', {'assignment': assignment})
@login_required
def upload_assignment(request, id):

    assignment = Assignment.objects.get(id=id)

    # prevent duplicate submission
    if Submission.objects.filter(
        student=request.user,
        assignment=assignment
    ).exists():
        return render(request, 'already_submitted.html')

    if request.method == 'POST':
        file = request.FILES['file']

        Submission.objects.create(
            student=request.user,
            assignment=assignment,
            file=file
        )
        return redirect('assignment_list')

    return render(request, 'upload.html', {'assignment': assignment})

@login_required
def my_submissions(request):
    subs = Submission.objects.filter(student=request.user)
    return render(request, 'my_submissions.html', {'subs': subs})

