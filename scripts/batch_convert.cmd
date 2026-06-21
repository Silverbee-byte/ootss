@echo off

set src=.\levels
set dst=..\images\levels

for %%f in ("%src%\*.png") do (
  vips webpsave "%%f" "%dst%\%%~nf.webp" --Q 70 --vips-progress
)
