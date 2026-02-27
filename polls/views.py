from django.http import HttpResponse

def index(request):
    return HttpResponse("""
    <h1>Django Polls Tutorial</h1>
    <p>This is my Django project submission.</p>
    <h2>My Question:</h2>
    <ul>
        <li>What's your favorite programming language?</li>
    </ul>
    <h2>Choices:</h2>
    <ul>
        <li>Python</li>
        <li>JavaScript</li>
        <li>Java</li>
        <li>C++</li>
    </ul>
    <p><em>Django version: 5.1.5</em></p>
    <p><em>Python version: 3.13.12</em></p>
    """)