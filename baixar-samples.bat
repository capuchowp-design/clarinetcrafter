@echo off
REM Baixa as 11 gravacoes reais de clarinete (tonejs-instruments, CC-BY 3.0) para samples\clarinet\
cd /d "%~dp0"
if not exist samples\clarinet mkdir samples\clarinet
set BASE=https://raw.githubusercontent.com/nbrosowsky/tonejs-instruments/master/samples/clarinet
for %%N in (D3 F3 As3 D4 F4 As4 D5 F5 As5 D6 Fs6) do (
  echo baixando %%N.mp3
  curl -fL -o samples\clarinet\%%N.mp3 %BASE%/%%N.mp3
)
echo Pronto.
pause
