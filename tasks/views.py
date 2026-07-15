import anthropic
from django.shortcuts import render, get_object_or_404
from .models import Email, Task

"""
This project summarises emails using the Anthropic API. This is done in the 
_create_task_for_email function.

The email_detail function renders the email_detail template and shows all the 
details from the original email of the chosen task. 

The tasks_display function 
checks for emails in the database without tasks and calls the function 
_create_task_for_email for all the emails without tasks, then renders all tasks 
into the tasks template.
"""


#Call Anthropic API and create a Task for a single email.
def _create_task_for_email(email):
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
    task_description = response.content[0].text
    return Task.objects.create(email=email, description=task_description)

# Get the email detail from the database. Show full details of a single email.
def email_detail(request, email_id):
    email = get_object_or_404(Email, id=email_id)
    return render(request, 'tasks/email_detail.html', {'email': email})


# Create tasks for any unprocessed emails, then render the task list.
def tasks_display(request):
    emails_without_tasks = Email.objects.filter(task__isnull=True)
    for email in emails_without_tasks:
        _create_task_for_email(email)

    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks})
