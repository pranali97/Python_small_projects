from plyer import notification
import time

if __name__=='__main__':
    while True:
        notification.notify(title="**Take Rest**",
                        message="Give some rest to you body, to your inner peace",
                        timeout=5)
        time.sleep(20)

