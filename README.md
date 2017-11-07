Befor starting this you should do :

# In your terminal :
1. ssh-keygen -t rsa -C "yourmail@gmail.com"
2. cd .ssh/
3. gedit id_rsa.pub
4. copy the whole key
5. ssh-add ~/.ssh/id_rsa

# Go to :
6. go to https://github.com/settings/keys paste the key in SSH

# Go to your private repo and open terminal type :
7. git remote -v 
8. git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
9. Verify new remote URL (by type git remote -v you see thoes lines below)
   origin  https://github.com/USERNAME/REPOSITORY.git (fetch)
   origin  https://github.com/USERNAME/REPOSITORY.git (push)
   
# Installation and running
```
python gdot.py pathofprivate/pubilc_repository

goto your private repo and run 

python scheduleCron.py 

```

