id=$1
atcoder-tools gen $id --workspace './' --lang python < ./scripts/.secret

code ./$id/A/main.py
cd ./$id

xdg-open https://nbviewer.jupyter.org/github/AtomScott/atcoder/blob/master/00_notebook_lib.ipynb


echo 'Just in case you forget..'
echo 'Theres no need to change dir, you can do everything from the command line'
echo 'open new main.py files from the cmd with code A/main.py'
echo 'submit only works if all the tests pass'
echo 'Debug using the vscode debug thingy on the left'
echo 'Good Luck'
