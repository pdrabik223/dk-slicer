# drabik-slicer
Tool that creates tool paths for 3d printer to draw stuff 

# TODOS:
- [ ] Pen mounting mechanism
- [ ] Fix GCode from images generation 
- [x] Generated Gcode has empty line at the begging, remove it
- [ ] Add layer change Api
- [ ] Bounding box Api
- [ ] Function plotter
- [ ] Use pronconsole in a subprocess to print directly 
    - [link to official site](https://www.pronterface.com/)
    - [link to downloads](https://kliment.kapsi.fi/printrun/)
    - list of commands that need to be passed to printrun subprocess (on Windows)


        most likely in place of [port] will be COM4   
        ```
        connect [port]  
        load [filepath] 
        print
        ```

# Note
All points on canvas should be adjusted by:
    
    41 in y axis
    36 in x axis