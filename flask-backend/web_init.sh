

#-e filename 如果 filename存在，则为真
static_DIR="/usr/src/app/project/static/"
if [ -d "$static_DIR" ]; then
  ### Take action if $DIR exists ###
  echo "already have ${static_DIR}..."
else
  ###  Control will jump here if $DIR does NOT exists ###
  mkdir ${static_DIR}
  echo "create ${static_DIR}"
fi

#-e filename 如果 filename存在，则为真
templates_DIR="/usr/src/app/project/templates/"
if [ -d "$templates_DIR" ]; then
  ### Take action if $DIR exists ###
  echo "already have ${templates_DIR}..."
else
  ###  Control will jump here if $DIR does NOT exists ###
  mkdir ${templates_DIR}
  echo "create ${templates_DIR}"
fi


#-e filename 如果 filename存在，则为真
log_DIR="/usr/src/app/log"
if [ -d "$log_DIR" ]; then
  ### Take action if $DIR exists ###
  echo "already have ${log_DIR}..."
else
  ###  Control will jump here if $DIR does NOT exists ###
  mkdir ${log_DIR}
  echo "create ${log_DIR} ."
fi




pip install --upgrade pip
pip install -r requirements.txt
export PATH=$PATH:/usr/local/bin
#ser in env.env 检测环境变量
if [ "$DATABASE" = "postgres" ] #当这句话成立时执行then
then
    echo "Waiting for postgres..."
#-z 扫描通信端口时使用。检测postgre是否开启
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ "$FLASK_if_create_database" = "YES" ]
then
    echo "Creating the database tables..."
    python3 manage.py create_and_init_db
    echo "Tables created"
fi

echo "run gunicorn"
gunicorn manage:app -c gunicorn_set.py &

exec "$@" #then run cammod  entrypoint bash,it will run bash
