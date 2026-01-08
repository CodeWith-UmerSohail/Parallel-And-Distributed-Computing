from celery import Celery
import time

# Create Celery app
app = Celery(
    'emailTask',
    broker='amqp://guest@localhost//'
)

@app.task
def send_email(user_email):
    """
    Background task to send an email.
    
    Real-life scenario:
    After user registration, email is sent asynchronously.
    """
    print(f"📧 Sending email to {user_email}...")
    
    # Simulate email sending delay
    time.sleep(5)
    
    print(f"✅ Email successfully sent to {user_email}")
    return f"Email sent to {user_email}"
