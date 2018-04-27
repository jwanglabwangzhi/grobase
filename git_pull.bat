echo starting
echo The directory is: %cd%

echo add all
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
git add -A .
echo add finish!
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

echo;
echo commit to local reposity
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
set /p declation=input commit words:
git commit -m "%declation%"
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

echo;
echo push to github
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
git push origin master
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

echo;
echo all finish!
echo;

pause
