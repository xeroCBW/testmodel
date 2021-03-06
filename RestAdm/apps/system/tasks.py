from __future__ import absolute_import
from celery import shared_task, task, Task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

class demotask(Task):

    def on_success(self, retval, task_id, args, kwargs):   # 任务成功执行
        logger.info('task id:{} , arg:{} , successful !'.format(task_id,args))

        return super(demotask, self).on_success(retval, task_id, args, kwargs)




    def on_failure(self, exc, task_id, args, kwargs, einfo):  #任务失败执行

        logger.info('task id:{} , arg:{} , failed ! erros : {}' .format(task_id,args,exc))

        return super(demotask, self).on_failure(exc, task_id, args, kwargs, einfo)


    def on_retry(self, exc, task_id, args, kwargs, einfo):    #任务重试执行


        logger.info('task id:{} , arg:{} , retry !  einfo: {}'.format(task_id, args, exc))
        return super(demotask, self).on_retry(exc, task_id, args, kwargs, einfo)

@task(base=demotask)
def add(x, y):

    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


