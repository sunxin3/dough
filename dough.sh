cd /root
git clone https://github.com/sunxin3/dough.git

cd /usr/lib/python2.6/site-packages/horizon/dashboards/nova
mv dashboard.py dashboard.py.bak_geyg

cp /root/nova/dashboard.py ./
cp -rf /root/nova/dough ./

service httpd restart



cd /usr/lib/python2.6/site-packages
mv dough-0.1.1-py2.6.egg dough-0.1.1-py2.6.egg.bak.geyg
cp -rf /root/dough-0.1.1-py2.6.egg ./
