
ImageSearch,vx,vy, 0,0,1920,1080,*60 0.png
	if ErrorLevel=0
	{
		
		Click,%vx%,%vy%
		Sleep,800
		ExitApp
	}

	if ErrorLevel=1
	{
		MsgBox, image change please
	}
	
return
