@echo off

rem Set the directory path
set dir_path=<directory_path>

rem Change to the directory
cd /d %dir_path%

rem Loop through each file in the directory
for /f "delims=" %%a in ('dir /b *.*') do (
   rem Check if the file name starts with "[SPOTIFY"
   if "%%a" == "[SPOTIFY*" (
      rem Remove the first 24 characters of the file name
      set new_name=%%a:~24%
      ren "%%a" "%new_name%"
   )
)

echo Done!
