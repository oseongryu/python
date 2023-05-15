#NoEnv

SetWorkingDir %A_ScriptDir%

#SingleInstance Force



CoordMode,Pixel, Screen

CoordMode,Mouse, Screen



CenterImgSrchCoords(File, ByRef CoordX, ByRef CoordY)

{

	static LoadedPic

	LastEL := ErrorLevel

	Gui, Pict:Add, Pic, vLoadedPic, %File%

	GuiControlGet, LoadedPic, Pict:Pos

	Gui, Pict:Destroy

	CoordX += LoadedPicW // 2

	CoordY += LoadedPicH // 2

	ErrorLevel := LastEL

}



ImageSearch, FoundX, FoundY, 0, 0, A_ScreenWidth, A_ScreenHeight, C:\캡처.PNG

CenterImgSrchCoords("C:\Users\osryu\Pictures\temp.JPG", FoundX, FoundY)

If ErrorLevel = 0

{		

	Click, %FoundX%, %FoundY% Left, 1		

}



ExitApp