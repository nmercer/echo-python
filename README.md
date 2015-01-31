# echo-python

### Basics
```py
from amazon_echo import Echo

echo = Echo('username', 'password')

print echo.get_latest_todo()
```

### Requires
  - bs4 - (BeautifulSoup)

  - requests


### Example

``` py
from amazon_echo import Echo
import sched, time

scheduler = sched.scheduler(time.time, time.sleep)
echo = Echo('username', 'password')

# Runs Every 5 Seconds and prints out what you last said
def main(scheduler):
    print echo.get_latest_todo()
    # Todo - Whatever you want to do based on what you said
    # Turn on lights
    # Turn down heat
    # Etc...
    scheduler.enter(5, 1, main, (scheduler,))

scheduler.enter(0, 1, main, (scheduler,))
scheduler.run()
```
