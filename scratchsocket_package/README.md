# About
<strong>ScratchSocket</strong> is a object oriented python library that can be used to make simple connections with *https://scratch.mit.edu/*!

<strong>You need to have the coding language, Python, installed on your computer to use this library.</strong>
*Download Python here if you don't have it: https://www.python.org/downloads/*

<strong> Package created by: </strong> *Abhiram*

<strong>Credits:</strong>

- @TimMcCool on scratch.mit.edu
- @TheCloudDev on scratch.mit.edu

# Installation
To install the package, run this command in your command prompt / shell:
```
pip install scratchsocket
```
<strong> *Or* </strong>

Add this at the top of your python code:
```python
import os
os.system("pip install scratchsocket")
```

# Login / Connection
There are two ways to log in:
If you are using a web editor, like replit, you will need to log in using your session id.
If you are using a desktop IDE, then you can log in regularly using the "scratchlogin" method.

## SCRATCH SESSION LOGIN
```python
import scratchsocket
socket = scratchsession("YOUR_SESSION_ID", username="USERNAME")
client = socket.connect("PROJECTID")
```
## SCRATCH REGULAR LOGIN
```python
import scratchsocket
socket = scratchlogin("USERNAME", "PASSWORD")
client = soccket.connect("PROJECTID")
```

The client portion of the code is what connects the python server with your project. For more information on the client section, check the "Extra addons" section.

# Usage
<strong>Add the scratchsocket asset to your scratch project:</strong>

Download this project file (.sb3) to your computer: <a href="https://drive.google.com/uc?export=download&id=1CEM6z6DtCYUKSkTTOK-lLFlXunKJYp31" download="https://replit.com/@abhiramtx/ScratchSocket#scratchsocket_asset.sb3">scratchsocket_asset.sb3</a>

Once the file is downloaded, go to the scratch website, and make a new project. Then upload the project file (scratchsocket_asset.sb3) into the scratch project.

<strong>How to use:</strong>

First we need to establish a connection with scratch. To do so, copy this code into your python editor under the log in section:
```python
@client.event
def on_ready():
  print("scratchsocket is ready")
client.run()  #Make sure this is ALWAYS at the bottom of your Python file!!
```

After you paste this code into your editor, you can now add more requests under the "on_ready" function.

<strong>Examples:</strong>

This is a example on how to create your own requests using this library:

>First, we need to add this bit of code to our code editor:
```python
@client.request
def ping():
  print("Ping recived.")
  return "pong"
```
>After we added the code above, our editor should look something like this:
```python
from scratchsocket import scratch
socket = scratch('SCRATCH_USERNAME', 'SCRATCH_PASSWORD')
client = socket.connect('PROJECT_ID')
@client.event
def on_ready():
  print("scratchsocket is ready")
# The code below is what we just added:
@client.request 
def ping():
  print("Ping recived.")
  return "pong"
client.run()  #Make sure this is ALWAYS at the bottom of your Python file!!
```
>Now lets move on to the Scratch part of it...
>
>In "the scratchsocket" sprite, there should be a block that looks like:
>
>[Send request ☁️| Request name: (   ) and wait] 
>
>... with no arguments.
>
>In the "Request name" section, put "ping", and drag the block until it snaps with "when 🏳️ clicked" block.
>
>After you do so, your scratch code should look something like this:
>
>[When 🏳️ clicked]: 
>
>[Send request ☁️| Request name: ("ping") and wait]
>
><strong>Testing our code:</strong>
>
>Now click the green flag and wait a few seconds. You should then see 1 item in the "response" list that says "pong". When you go to your code editor, you should see the "Ping recived." message in the console. This means our code worked!
>
><strong>*If*</strong> the code for some reason did not work, then try debugging it. If it still does not work, you can contact me on my scratch profile (@Air_heads).
## Enjoy the library!

# Extra addons
There is currently one extra addon for this package which you can use.
## Max Variables Used
If you want to delete some of the cloud vars, you can change the "maxVars" parameter for the client so that it only uses the numbered vars that were inputted.
How to set "maxVars":
```python
client = socket.connect("PROJECTID", maxVars=NUMBER)
```
Example:
```python
client = socket.connect("1234", maxVars=1)
```
We set the maxVars used to one. This means that only the "FROM_HOST_1" variable will be used, and you can delete the other 5.
Note: The less variables being used, the longer it will take for the data to return. Also, the parameter "maxVars" is set to 6 by default.

# License
> License = "MIT"
Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.