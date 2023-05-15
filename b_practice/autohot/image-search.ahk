SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

CoordMode,Pixel,Screen
CoordMode,mouse,Screen

;CoordMode, Mouse, Window

F9::
ImageSearch, vx, vy, 0, 0, A_ScreenWidth, A_ScreenHeight, test.png
if ErrorLevel = 0
{
	MsgBox, FIND
	MouseMove, vx+50, vy+50
}
else if ErrorLevel = 1
	MsgBox, can't Find

return