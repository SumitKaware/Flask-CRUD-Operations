# Flask-CRUD-Operations
# First-Interaction
Start Env - ./env/Scripts/activate.bat
flask --app CRUD_Operations run
curl http://localhost:5000
curl http://localhost:5000/foo

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: no email was given and auto-detection is disabled
2023-04-24 00:45:27.912 [info] > git config --get-all user.name [104ms]
2023-04-24 00:45:28.002 [info] > git config --get commit.template [81ms]
2023-04-24 00:45:28.014 [info] > git for-each-ref --format=%(refname)%00%(upstream:short)%00%(objectname)%00%(upstream:track)%00%(upstream:remotename)%00%(upstream:remoteref) refs/heads/main refs/remotes/main [86ms]
2023-04-24 00:45:28.083 [info] > git status -z -uall [59ms]