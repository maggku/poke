import anthropic
from django.shortcuts import render, get_object_or_404
from .models import Email, Task



def index(request):
    # get the first email from the database
    email = get_object_or_404(Email, pk=request.GET.get("email"))

    # send it to Anthropic
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-opus-4-7",
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
    return HttpResponse(task_description)