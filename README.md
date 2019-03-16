# ICISTS Application Management System 2

ICISTS Application Management System to submit and manage applications.

## Production Deployment

### Local

Local 환경에서 실행 시 host 상에서의 code 변경이 바로 반영될 수 있도록 docker-compose.yml을 기반으로 실행해 주세요.

`docker-compose up -f docker-compose.local.yml`

로컬 개발에 필요한 command (shell 접근, migration 등)은 Makefile에 정의되어 있습니다. 
project root에서 `make {command}`로 실행해 주세요.

For more info: `make help`

### 권한 발급

secret.env 파일을 별도로 요청하세요.

~~ICISTS account에 권한이 있을 경우 `./scripts/get_secret.sh` 을 통해 아래 파일을 받을 수 있습니다. (Set-up 예정)~~

- `environments/secret.env`

## Authors

- **Park Junwoo** - *Initial work & maintenance* - [zoonoo](https://github.com/zoonoo)
- **Gunwoo Kim** - *Initial work & Core Logic* - [gunwooterry](https://github.com/gunwooterry)

See also the list of [contributors](https://github.com/icists/ams2/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

