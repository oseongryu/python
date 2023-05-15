F1::
Loop
{
	ImageSearch,vx,vy, 0,0,960,1080,*0 1.png
	if ErrorLevel=0
	{
		Click,%vx%,%vy%
		
	}
	Sleep,4000

	ImageSearch,vx,vy, 0,0,960,1080,*0 2.png
	if ErrorLevel=0
	{
		Click,%vx%,%vy%
	}
	Sleep,4000
	ImageSearch,vx,vy, 0,0,960,1080,*0 3.png
	if ErrorLevel=0
	{
		Click,%vx%,%vy%
	}
	Sleep,4000
	ImageSearch,vx,vy, 0,0,960,1080,*0 4.png
	if ErrorLevel=0
	{
		Click,%vx%,%vy%
	}
		Sleep,4000
	ImageSearch,vx,vy, 0,0,960,1080,*0 5.png
	if ErrorLevel=0
	{
		Click,%vx%,%vy%
	}		
	Sleep,4000
	ImageSearch,vx,vy, 0,0,960,1080,*0 6.png
	if ErrorLevel=0
	{
		Click,%vx%,%vy%
	}	
	Sleep,4000
}
return

F2::Pause
F3::ExitApp