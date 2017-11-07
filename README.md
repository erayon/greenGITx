Befor starting this you should do :

# create a private repo name as you like

# In your terminal :
1. ssh-keygen -t rsa -C "yourmail@gmail.com"
2. cd .ssh/
3. gedit id_rsa.pub
4. copy the whole key
5. ssh-add ~/.ssh/id_rsa

# Go to :
6. go to https://github.com/settings/keys paste the key in SSH

# Clone your private repo in your sytem

# Go to your private repo and open terminal type :
7. git remote -v 
8. git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
9. Verify new remote URL (by type git remote -v you see thoes lines below)
   1. origin  https://github.com/USERNAME/REPOSITORY.git (fetch)
   2. origin  https://github.com/USERNAME/REPOSITORY.git (push)
   
# Installation and running
```
1. clone the repo : https://github.com/erayon/greenGITx.git
2. run python gdot.py pathofprivate_repo
3. goto your private repo 
4. run:  python scheduleCron.py 

```

# Note
This is beta version, feel free to write issuse what you have faced after doing this. In next version I will modify the code such a way no need to do SSH pairing.

