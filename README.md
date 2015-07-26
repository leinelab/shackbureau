# shackbureau
the one and only (yet another) shack member managment

## howto run

### docker-compose

#### Install docker-compose
    sudo pip install -U docker-compose  

#### Make an alias
    alias dc=docker-compose  

### Build the container
    dc build

#### db reset
    dc run web reset_db

#### database reset
    dc run web migrate

#### createsuperuser
    dc run web createsuperuser

### start the containter
    dc up -d
And navigate your browser to `http://localhost:8000/admin/`

## Importing old data

Export the CSV from LibreOffice, delimiter `;` quote-char `"` and move it to the root of this git repo.   

Run `dc run web shell_plus `  

    from usermanagement.utils import import_old_shit  
    import_old_shit('/opt/code/Mitglieder.csv')  
    

## Testing

### run tests
    docker exec -ti shackbureau_web_1 py.test

[![wercker status](https://app.wercker.com/status/24858fa12027a6ad2bb5295b398a8c2b/m/master "wercker status")](https://app.wercker.com/project/bykey/24858fa12027a6ad2bb5295b398a8c2b)
