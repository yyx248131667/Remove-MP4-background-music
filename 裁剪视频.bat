@echo off

:: Prompt the user for the input video folder path
set /p input_folder=请输入视频文件夹路径：

:: Ensure the output folder exists
if not exist "%output_folder%" (
    mkdir "%output_folder%"
)

:: Loop through all video files in the input folder
for %%f in ("%input_folder%\*.mp4") do (
    set input_video=%%f
    set output_video="%output_folder%\%%~nxf"

    :: Use FFmpeg to crop the video to half width
    ffmpeg -i !input_video! -vf crop=in_w/2:in_h:0:0 !output_video!
)

echo Batch cropping completed!
