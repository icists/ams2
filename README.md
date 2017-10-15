# ICISTS Application Management System 2

ICISTS Application Management System to submit and manage applications.

## Deployment (개발 가이드라인)

필요한 command는 `scripts` 디렉토리 내에 정의되어 있습니다.

`./scripts/deploy_docker.sh`
: 최초 설치 시 Image를 Build하고 Container를 실행 시킵니다.

`./scripts/shell_docker.sh`
: Container 실행 시 shell에 접속합니다.

`./scripts/migrate.sh`
: migration 실행.

`./scripts/stop_all_containers.sh`
: Container 종료.

##### 중요
실행에 필요하지만 보안상 이 repository에 포함 시키지 않은 파일이 몇개 존재합니다. 아래 파일은 개발 환경 세팅하실 때 별도로 요청해 주세요.
 - `environments/secret.env`
 - `nginx/certs/`


## Built With
* [Alpine Linux](https://alpinelinux.org/) : The Operating System. v.3.6
* [Docker](https://www.docker.com/) : v.17.09.0-ce
* [Docker Compose](https://docs.docker.com/compose/) : v.3
* [Python](https://www.python.org/) : v.3.6.3
* [Django](https://docs.djangoproject.com/en/1.11/releases/1.11/) - v.1.11
* [MySQL](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-3.html) - v.8.0.3

## Authors

* **Park Junwoo** - *Initial work & maintance* - [zoonoo](https://github.com/zoonoo)

See also the list of [contributors](https://github.com/icists/ams2/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

