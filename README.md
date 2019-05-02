Apache-1c Role
=========

Role for setup Apache for 1c publication and publicate list of bases

Requirements
------------

1. Веб сервер для размещения дистрибутивов 1с
2. Ubuntu, CentOS

Role Variables
--------------

Путь к каталогу где будет сохранен дистрибутив 1с

    onec_dist_storage: /opt/dist

Используемая версия платформы

    onec_version: "8.3.13.1644"

Список хостов откуда производится загрузка дистрибутива

    onec_mirrors: []
    # onec_mirrors:
    #   - http://172.17.0.1

Список БД с параметрами для публикации 

    databses: []

    databses:
      onec-db-1:                              # Имя БД
        base: onec-db-1-context               # Контекст для vrd файла (по-умолчанию используется Имя БД)
        server: 127.0.0.1:1541,127.0.0.2:2541 # Адрес(-а) кластера сервера(-ов) 1С
        name_in_cluster: onec-db-1-prod       # Имя БД в кластере
        usr: user                             # Имя пользователя для подключния к Бд (по умолчанию не задано)
        pwd: pass                             # Пароль пользователя для подключния к Бд (по умолчанию не задан) 
        httpServices:                         # Список публикуемых http сервисов
          service1:                           # Имя публикуемого http сервиса    
            rootUrl: service1
            enable: false
            reuseSessions: autouse
            sessionMaxAge: 20
            poolSize: 10
            poolTimeout: 5

Dependencies
------------

no dependency

Example Playbook
----------------

    - hosts: servers
      roles:
        - role: bessonovevgen.apache-1c

License
-------

BSD

Author Information
------------------

Bessonov Evgeniy (evgen@ievgen.ru)

Based on [geerlingguy/ansible-role-apache](https://github.com/geerlingguy/ansible-role-apache)

TODO
------------------

1. см. в содержимом по комменту TODO
2. В шаблон vrd конфиг для вебсервисов, odata (сделана заглушка)
3. Версия используемой библитеки (если установить несколько версий платформы на один хост)
4. Удаление не нужных виртуальных хостов
5. Использовать виртуальные хосты с поддоменом