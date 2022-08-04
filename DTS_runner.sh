cd /etlstar/users/etladminuser/star_etl/dts
PATH=$PATH:$HOME/bin
export PATH
JAVA_HOME=/usr/bin
PATH=/usr/bin:/usr/sbin:/opt/rh/rh-python36/root/usr/bin/python3.6:$PATH; export PATH
ORACLE_HOME=/etlstar/users/etladminuser/product/12.2.0/dbhome_1; export ORACLE_HOME
PATH=$ORACLE_HOME/bin:$PATH; export PATH
LD_LIBRARY_PATH=$ORACLE_HOME/lib;export LD_LIBRARY_PATH
/opt/rh/rh-python36/root/usr/bin/python3.6 /etlstar/users/etladminuser/star_etl/dts/StarETL2.0.0.py >> /etlstar/users/etladminuser/star_etl/dts/general.log
