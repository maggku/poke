import anthropic
from django.http import HttpResponse
from .models import Email


def test_anthropic(request):
    # get the first email from the database
    email = Email.objects.get(id=1)

    # send it to Anthropic
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""
                    Read this email and extract ONE clear task from it.

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