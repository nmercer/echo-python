# echo-python
from amazon_echo import Echo

echo = Echo('username', 'password')

print echo.get_latest_todo()
