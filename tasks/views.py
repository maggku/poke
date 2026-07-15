import anthropic
from django.shortcuts import render, get_object_or_404, redirect
from .models import Email, Task

"""
This project summarises emails using the Anthropic API. This is done in the 
generate_task_from_email function, and we are redirected to the main tasks page. 
The email_detail function renders the email_detail template and shows all the 
details from the original email of the chosen task. The tasks_display function 
gets tasks from the database and renders them in the tasks template.
"""

# Get the email detail from the database. Show full details of a single email.
def email_detail(request, email_id):
    email = get_object_or_404(Email, id=email_id)
    return render(request, 'tasks/email_detail.html', {'email': email})

# Get all tasks from the database. List all saved tasks.
def tasks_display(request):
    task = Task.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': task})
"""
# Send an email to the Anthropic API, save the returned task, and redirect to the task list.
def generate_task_from_email(request, email_id):
    email = get_object_or_404(Email, id=email_id)

    # send the email to the Anthropic API
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""
                    Read this email and extract ONE clear task from it. Use a maximum of 40 characters.

                    Sender: {email.sender}
                    Subject: {email.subject}
                    Message: {email.message}

                    Reply with ONLY the task description, nothing else.
                """
            }
        ]
    )

    # return the result as plain text on the screen
    task_description = response.content[0].text

    # Create a new task in the database
    task = Task.objects.create(
        email=email,
        description=task_description,
    )

    return redirect('tasks')

"""