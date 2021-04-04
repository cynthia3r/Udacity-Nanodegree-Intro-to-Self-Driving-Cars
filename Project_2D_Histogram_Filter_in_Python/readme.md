# Project overview

Writing code is important. But a big part of being on a self driving car team is working with a large existing codebase. On high stakes engineering projects like a self driving car, you will probably have to earn the trust of your managers and coworkers before they'll let you make substantial changes to the code base.

A typical assignment for someone new to a team is to make progress on a backlog of bugs. So with that in mind, **the project is designed not only to implement new functionality for Two Dimensional Histogram Filter successfully but also to debug a problem the robot was having with rectangular environments.**

## Detailed approach and instructions
1. **Implement a 2D sense function - write code that gets the robot moving correctly:**
As you can see, the robot's beliefs aren't changing. No matter how many times we call the simulation's sense method, nothing happens. The beliefs remain uniform. Follow the below instructions:
	- Open localizer.py and complete the sense function.
	- Run the code in the cell below to import the localizer module (or reload it) and then test your sense function.
	- If the test passes, you've successfully implemented your first feature! Keep going with the project. If your tests don't pass (they likely 		  won't the first few times you test), keep making modifications to the sense function until they do!

2. **Integration Testing:**
Before we call this "complete" we should perform an integration test. We've verified that the sense function works on it's own, but does the localizer work overall?
Let's perform an integration test. First you you should execute the code in the cell below to prepare the simulation environment.
Note: Implementing motion will reveal a bug which hadn't shown up before. Here you'll identify what the bug is and take steps to reproduce it. Then you'll identify the cause and fix it.

3. **Identify and Reproduce the bug:**
Software has bugs. That's okay.
A user of your robot called tech support with a complaint
"So I was using your robot in a square room and everything was fine. Then I tried loading in a map for a rectangular room and it drove around for a couple seconds and then suddenly stopped working. Fix it!"
Now we have to debug. We are going to use a systematic approach to reproduce the bug.
	- Read (and understand) the error message (when one exists)
	- Write a test that triggers the bug.
	- Generate a hypothesis for the cause of the bug.
	- Try a solution. If it fixes the bug, great! If not, go back to step 4.

## Debug and fix the Bug:
The user said that rectangular environments seem to be causing the bug.

1. **Read and Understand the error message:**
If you triggered the bug, analyze the error message

2. **Write a test that reproduces the bug:**
This will help you know when you've fixed it and help you make sure you never reintroduce it in the future. You might have to try many potential solutions, so it will be nice to have a single function to call to confirm whether or not the bug is fixed

3. **Generate a Hypothesis:**
In order to have a guess about what's causing the problem, it will be helpful to use some Python debuggin tools
The pdb module (python debugger) will be helpful here!
	- **Setting up the debugger:**
Open localizer.py and uncomment the line to the top that says import pdb
Just before the line of code that is causing the bug new_G[int(new_i)][int(new_j)] = cell, add a new line of code that says **pdb.set_trace()**
Run your test by calling your test function (run the cell below this one)
You should see a text entry box pop up! For now, type c into the box and hit enter to continue program execution. Keep typing c and enter until the bug is triggered again

	- **Using the debugger:**
The debugger works by pausing program execution wherever you write pdb.set_trace() in your code. You also have access to any variables which are accessible from that point in your code.

4. **Debugging:**
Try running your test again. This time, when the text entry box shows up, type new_i and hit enter. You will see the value of the new_i variable show up in the debugger window. Play around with the debugger: find the values of new_j, height, and width. Do they seem reasonable / correct?
When you are done playing around, type c to continue program execution. Was the bug triggered? Keep playing until you have a guess about what is causing the bug.

5. **Write a Fix:**
You have a hypothesis about what's wrong. Now try to fix it. When you're done you should call your test function again. You may want to remove (or comment out) the line you added to localizer.py that says pdb.set_trace() so your test can run without you having to type c into the debugger box.
