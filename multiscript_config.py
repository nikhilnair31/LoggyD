## CELERY AND REDIS
# Broker settings.
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
# Broker settings.
CELERY_RESULT_BACKEND='redis://127.0.0.1:6379'

## CELERY AND REDIS
SVM_KERNEL = 'rbf'
SVM_GAMMA = 'auto'
SVM_CLASS_WEIGHTS = {0:1, 1:3}

#JS
AVG_READ_SPEED = 250 # words per minute