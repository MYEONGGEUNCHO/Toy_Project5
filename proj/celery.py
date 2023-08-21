from celery import Celery

app = Celery('proj',
    broker='amqp://localhost',
    backend='redis://127.0.0.1:6379',
    include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()