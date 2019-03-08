# GCodeAdapter

Simple gcode editor, to make time lapses from 3D prints. It modifies the gcode to go to the end corner of the bed and activate the end stop switch, to trigger the camera shutter. On every change on Z layer, executes some gcode commands to go to that position, set the retraction length and wait X (ms) to take the photo.

![ecra2](https://user-images.githubusercontent.com/6796382/54046496-7004b000-41cc-11e9-9a10-e89fb255f0b0.PNG)

# Running

1-Run the .py file;

2-Select the GCode file that you want to change;

3-Click on Show File, to see your GCode;

4-Save the file;

(Optional)
-
-Use the Clear button to clear all the data and to choose a new file;

-Set up the delay time and retraction length, to your needs.
