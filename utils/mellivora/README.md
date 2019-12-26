This is a messy list of what I changed on mellivora to make it suit my own purposes.

## Changes

### `Dockerfile`
Add `libonig-dev` to `apt install` list, to fix a bug

### `htdocs/actions/reset_password.php`
Comment pretty much the entire thing out, and adding `message_generic("Failure", "Password reset is disabled. Contact Kevin if you cannot login to your account.");`. Don't want people abusing the password reset stuff, and we're doing it on a small enough scale to deal with password resets manually. 

### `htdocs/home.php`
Comment out entire thing displaying news, and adding this block:
```php
if (cache_start(CONST_CACHE_NAME_HOME, Config::get('MELLIVORA_CONFIG_CACHE_TIME_HOME'))) {

    $news = db_query_fetch_all('SELECT * FROM news ORDER BY added DESC');
    foreach ($news as $item) {
        echo '<link rel="stylesheet" href="https://stackedit.io/style.css">
        <div class="news-container">';
            section_head($item['title']);
            echo '
            <div class="news-body">
                ',$item['body'],'
            </div>
        </div>
        ';
    }

    cache_end(CONST_CACHE_NAME_HOME);
}
```
I'm writing the syllabus in markdown, then exporting as HTML. The original code uses bbcode, which is less versatile.

### `htdocs/register.php`
Replace `Registration is currently closed, but you can still <a href="interest">register your interest for upcoming events</a>.` to `Registration is currently closed. Please check back later.`. No need for interest registration stuff.

### `htdocs/reset_password.php
Comment everything out, adding:
```php
head(lang_get('reset_password'));
message_inline_blue('Password reset is disabled. Contact Kevin if you cannot login to your account.');
foot();
```
Again, this is to disable password resets. This is the front facing page, while the one we did earlier is the api to process the request. Both are gone.

### `include/layout/forms.inc.php`
Removed `<option disabled selected>-- ',lang_get('please_select_country'),' --</option>`. We just don't have a use for selecting countries.

### `include/session.inc.php`
Commented out `send_email(array($email), $email_subject, $email_body);`. No need to send emails.


## Additions

### `include/config/config.inc.php` and `include/config/db.inc.php`
Configurations. Nuff said.

### `docker-compose.yml`
Custom docker configuration, not really that custom but still worth hiding since it contains some database creds.
